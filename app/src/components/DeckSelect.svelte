<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from 'carbon-components-svelte';
  import { getContext } from 'svelte';
  import type { IAnkiConnect } from '../services/ankiconect';

  const ankiConnect = getContext<IAnkiConnect>('anki');
  const decks = ankiConnect.deckNames();
</script>

{#await decks}
  <SelectSkeleton />
{:then deckNames}
  <Select labelText="Target Deck">
    {#each deckNames as deck}
      <SelectItem value={deck} text={deck} />
    {/each}
  </Select>
{/await}
