<script lang="ts">
  import { MultiSelect } from "carbon-components-svelte";
</script>

<MultiSelect
  size="xl"
  label="Sentence Sources"
  items={[
    { id: "0", text: "Jibiki" },
    { id: "1", text: "Custom" },
  ]}
  selectedIds={["0"]}
/>
