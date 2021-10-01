<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from 'carbon-components-svelte';
  import { getContext } from 'svelte';
  import type { IAnkiConnect } from 'src/services/ankiconect';

  export let selected: string;
  export let disabled: boolean = false;

  const ankiConnect = getContext<IAnkiConnect>('anki');
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
  <Select {disabled} labelText="Target Deck" bind:selected>
    {#each deckNames as deck}
      <SelectItem value={deck} text={deck} />
    {/each}
  </Select>
{/await}
