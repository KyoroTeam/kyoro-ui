<script lang="ts">
  import { MultiSelect } from "carbon-components-svelte";
  import type { SentenceSource } from "../stores/sentenceSourcesStore";
  import { SentenceSourceStore } from "../stores/sentenceSourcesStore";

  let sentenceSources: SentenceSource[];
  SentenceSourceStore.subscribe((s) => (sentenceSources = s));
</script>

<MultiSelect
  size="xl"
  label="Sentence Sources"
  items={sentenceSources.map((item, i) => ({ id: `${i}`, text: item.name }))}
  selectedIds={["0"]}
/>
