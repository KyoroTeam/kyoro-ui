<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from 'carbon-components-svelte';
  import { getContext } from 'svelte';
  import type { IAnkiConnect } from '../services/ankiconect';

  export let modelName: string = '';
  export let noLabel: boolean = true;

  const ankiConnect = getContext<IAnkiConnect>('anki');

  let models: ReturnType<IAnkiConnect['modelFieldNames']>;
  $: {
    models = ankiConnect.modelFieldNames(modelName);
  }
</script>

{#await models}
  <SelectSkeleton />
{:then modelNames}
  <Select labelText={!noLabel ? 'Target Model' : ''}>
    {#each modelNames as model}
      <SelectItem value={model} text={model} />
    {/each}
  </Select>
{/await}
