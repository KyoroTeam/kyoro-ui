<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from "carbon-components-svelte";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";

  export let selected: string;

  const ankiConnect = getContext<IAnkiConnect>("anki");
  const decks = ankiConnect.deckNames();

  decks.then((names) => {
    if (names.length > 0) {
      selected = names[0];
    }
  });
</script>

{#await decks}
  <SelectSkeleton />
{:then deckNames}
  <Select labelText="Target Deck" bind:selected>
    {#each deckNames as deck}
      <SelectItem value={deck} text={deck} />
    {/each}
  </Select>
{/await}
