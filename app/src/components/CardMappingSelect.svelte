<script lang="ts">
  import { Select, SelectItem } from "carbon-components-svelte";
  import settingsStore from "../stores/settingsStore";
  import type { IUserSettings, ICardMapping } from "../stores/settingsStore";

  export let selected: ICardMapping;

  let mappings: IUserSettings;
  settingsStore.subscribe((value) => (mappings = value));
</script>

{#if mappings.cardMappings?.length > 0}
  <Select>
    {#each mappings.cardMappings as mapping}
      <SelectItem>{mapping.mappingName}</SelectItem>
    {/each}
  </Select>
{/if}
