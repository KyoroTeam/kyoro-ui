<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from 'carbon-components-svelte';
  import type { KyoroFieldName } from '../../stores/settingsStore';
  import { getContext } from 'svelte';
  import type { IAnkiConnect } from 'src/services/ankiconect';

  export let modelName: string = '';
  export let disabled: boolean = false;
  export let label: KyoroFieldName;
  export let selected: string;

  const ankiConnect = getContext<IAnkiConnect>('anki');
  let modelNames: string[];

  $: if (modelName?.length > 0) {
    ankiConnect.modelFieldNames(modelName).then((names) => (modelNames = names));
  }
</script>

{#if modelNames?.length > 0}
  <Select bind:selected inline {disabled} helperText={label} size={'xl'}>
    {#each modelNames as model}
      <SelectItem value={model} text={model} />
    {/each}
  </Select>
{:else}
  <SelectSkeleton />
{/if}
