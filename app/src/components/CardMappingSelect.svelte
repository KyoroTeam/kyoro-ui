<script lang="ts">
  import { Select, SelectItem } from "carbon-components-svelte";
  import settingsStore from "../stores/settingsStore";
  import type { IUserSettings, ICardMapping } from "../stores/settingsStore";

  export let selected: ICardMapping | undefined;

  let settings: IUserSettings;
  let selectedMappingName: string;

  settingsStore.subscribe((value) => {
    settings = value;
    if (!selectedMappingName) {
      selectedMappingName = value?.cardMappings?.[0]?.mappingName;
    }
  });

  $: {
    selected = settings.cardMappings.find(
      (c) => c.mappingName == selectedMappingName
    );
  }
</script>

{#if settings.cardMappings?.length > 0}
  <Select bind:selected={selectedMappingName}>
    {#each settings.cardMappings as mapping}
      <SelectItem value={mapping.mappingName} />
    {/each}
  </Select>
{:else}
  <p>No Mappings</p>
{/if}
