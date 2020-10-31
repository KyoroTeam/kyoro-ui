<script lang="ts">
  import { Button } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import settingsStore from "../stores/settingsStore";
  import MappingCreator from "./MappingCreator.svelte";

  let settings: any;
  settingsStore.subscribe((value) => (settings = value));
</script>

<p>Test</p>

<Button
  size={'small'}
  hasIconOnly
  iconDescription={'Add New'}
  tooltipPosition="top"
  icon={Add16}
  on:click={() => {}} />
