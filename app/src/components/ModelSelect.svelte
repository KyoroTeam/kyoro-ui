<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from "carbon-components-svelte";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";

  export let selected: string;
  export let disabled: boolean = false;

  const ankiConnect = getContext<IAnkiConnect>("anki");
  const models = ankiConnect.modelNames();
</script>

{#await models}
  <SelectSkeleton />
{:then modelNames}
  <Select inline {disabled} labelText="Target Model" size={"xl"} bind:selected>
    {#each modelNames as model}
      <SelectItem value={model} text={model} />
    {/each}
  </Select>
{/await}
