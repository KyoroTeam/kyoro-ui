<script lang="ts">
  import { Select, SelectItem } from "carbon-components-svelte";
  import { cardMappingStore } from "../../stores/settingsStore";
  import type { ICardMapping } from "../../stores/settingsStore";

  export let selected: ICardMapping | undefined;

  let cardMappings: ICardMapping[];
  let selectedMappingName: string;

  cardMappingStore.subscribe((value) => {
    cardMappings = value;
    if (!selectedMappingName) {
      selectedMappingName = value?.[0]?.mappingName;
    }
  });

  $: {
    selected = cardMappings.find((c) => c.mappingName == selectedMappingName);
  }
</script>

{#if cardMappings?.length > 0}
  <Select bind:selected={selectedMappingName}>
    {#each cardMappings as mapping}
      <SelectItem value={mapping.mappingName} />
    {/each}
  </Select>
{:else}
  <p>No Mappings</p>
{/if}
