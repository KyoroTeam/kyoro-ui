<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from "carbon-components-svelte";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";
  export let modelName: string = "";
  export let disabled: boolean = false;
  export let label: string = "Target Thing";
  const ankiConnect = getContext<IAnkiConnect>("anki");
  let modelNames: string[];
  $: {
    console.log(modelName);
    if (modelName?.length > 0) {
      ankiConnect
        .modelFieldNames(modelName)
        .then((names) => (modelNames = names));
    }
  }
</script>

{#if modelNames?.length > 0}
  <Select inline {disabled} helperText={label} size={"xl"}>
    {#each modelNames as model}
      <SelectItem value={model} text={model} />
    {/each}
  </Select>
{:else}
  <SelectSkeleton />
{/if}
