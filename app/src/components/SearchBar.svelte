<script lang="ts">
  import { Search, Button, ButtonSet } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";

  let searchValue = "";
  export let sentences: JibikiSenteceResponse[];

  async function fetchSentences() {
    const searchQuery = encodeURIComponent(searchValue);
    const url = `https://api.jibiki.app/sentences?query=${searchQuery}`;

    fetch(url, {
      credentials: "include",
    })
      .then((r) => r.json())
      .then((r: JibikiSenteceResponse[]) => {
        sentences = r;
      })
      .catch((e) => {
        // TODO: Error handling
        console.log(e);
      });
  }
</script>

<ButtonSet>
  <Search bind:value={searchValue} placeholder="Enter a phrase..." />
  <Button on:click={fetchSentences}>Search</Button>
</ButtonSet>
