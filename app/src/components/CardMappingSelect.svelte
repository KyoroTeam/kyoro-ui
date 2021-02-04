<script lang="ts">
  import { Select, SelectItem } from "carbon-components-svelte";
  import settingsStore from "../stores/settingsStore";
  import type { IUserSettings, ICardMapping } from "../stores/settingsStore";

  export let selected: ICardMapping | undefined;

  let settings: IUserSettings;
  settingsStore.subscribe((value) => (settings = value));

  let selectedMappingName = "";

  // Select first mapping if none selected
  $: {
    if (selectedMappingName.length === 0 && settings.cardMappings.length > 0) {
      selectedMappingName = settings.cardMappings[0].mappingName;
    }
  }

  // Update the prop with the mapping object with the name selected
  $: {
    selected = settings.cardMappings.find(
      (m) => m.mappingName === selectedMappingName
    );
  }
</script>

{#if settings.cardMappings?.length > 0}
  <Select bind:selected={selectedMappingName}>
    {#each settings.cardMappings as mapping}
      <SelectItem value={mapping.mappingName ?? "What"} />
    {/each}
  </Select>
{:else}
  <p>No Mappings</p>
{/if}
