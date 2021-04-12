<script lang="ts">
  import { Search, Button, ButtonSet } from "carbon-components-svelte";
  import { MultiSelect } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";

  export let sentences: JibikiSenteceResponse[];

  let loading = false;
  let searchValue = "";

  async function fetchSentences() {
    const searchQuery = encodeURIComponent(searchValue);
    const url = `https://cors.bridged.cc/https://api.jibiki.app/sentences?query=${searchQuery}`;

    loading = true;
    fetch(url)
      .then((r) => r.json())
      .then((r: JibikiSenteceResponse[]) => (sentences = r))
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

  const debouncedSearch = debounce(fetchSentences, 1000);
</script>

<ButtonSet>
  <Search
    bind:value={searchValue}
    on:input={debouncedSearch}
    placeholder="Enter a phrase..."
  />
  <MultiSelect
    size="xl"
    label="Sentence Sources"
    items={[
      { id: "0", text: "Slack" },
      { id: "1", text: "Email" },
      { id: "2", text: "Fax" },
    ]}
    selectedIds={["0", "1"]}
  />
  <Button skeleton={loading} on:click={fetchSentences}>Search</Button>
</ButtonSet>
