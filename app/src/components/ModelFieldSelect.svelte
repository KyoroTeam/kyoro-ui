<script lang="ts">
  import { Select, SelectItem, SelectSkeleton } from "carbon-components-svelte";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";

  export let modelName: string = "";
  export let noLabel: boolean = true;
  export let label: string = "Field";
  export let disabled: boolean;

  const ankiConnect = getContext<IAnkiConnect>("anki");
</script>

<Select inline {disabled} helperText={label} size={'xl'} selected="Front" />
