<script lang="ts">
  import { setContext } from "svelte";
  import * as Anki from "./ankiconect";
  setContext<Anki.IAnkiConnect>("anki", new Anki.AnkiConnect());
</script>

<slot />
