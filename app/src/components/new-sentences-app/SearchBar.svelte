<script lang="ts">
  import { Search, Button, ButtonSet } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import SentenceSourceSelect from "../SentenceSourceSelect.svelte";

  export let sentences: JibikiSenteceResponse[];

  let loading = false;
  let searchValue = "";

  async function fetchSentences() {
    const searchQuery = encodeURIComponent(
      `Words:${searchValue} OR Lemmas:${searchValue}`
    );
    const url = `http://localhost:8983/solr/kanji/select?q=${searchQuery}`;

    loading = true;
    fetch(url)
      .then((r) => r.json())
      .then(
        (r: Solr.SolrSearchResponse) =>
          (sentences = r.response.docs.map((s, i) => {
            return {
              id: i,
              language: "JA",
              sentence: "TODO",
              tags: ["A", "B"],
              translations: [
                {
                  id: 13,
                  language: "ENG",
                  sentence: "This is a Translation",
                },
              ],
            } as JibikiSenteceResponse;
          }))
      )
      .catch((e) => console.log(e))
      .finally(() => (loading = false));
  }

  function debounce<T extends any[]>(
    fn: (...args: T) => void,
    timeout: number
  ) {
    let timeout_id: NodeJS.Timeout;
    return (...args: Parameters<typeof fn>) => {
      clearTimeout(timeout_id);
      timeout_id = setTimeout(() => fn(...args), timeout);
    };
  }

  // const debouncedSearch = debounce(fetchSentences, 1000);
</script>

<ButtonSet style={"width:100%"}>
  <Search
    bind:value={searchValue}
    on:input={fetchSentences}
    placeholder="Enter a phrase..."
  />
  <SentenceSourceSelect />
  <Button skeleton={loading} on:click={fetchSentences}>Search</Button>
</ButtonSet>
