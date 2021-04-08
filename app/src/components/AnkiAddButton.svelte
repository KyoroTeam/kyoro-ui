<script lang="ts">
  import { Button, InlineLoading } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "../stores/settingsStore";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";

  export let tableRows: SelectTableRow[] = [];
  export let targetMapping: ICardMapping | undefined;

  const anki = getContext<IAnkiConnect>("anki");

  let loading: boolean = false;
  let errorMessage: string;

  function onClicked() {
    const { deckName, modelName, modelFieldMappings } = targetMapping!;
    console.log(targetMapping);
    loading = true;
    anki
      .addNote(deckName, modelName, modelFieldMappings)
      .then((r) => {
        if (r.error) {
          errorMessage = r.error;
        }
      })
      .catch((c) => (errorMessage = "Couldn't connect to Anki"))
      .finally(() => (loading = false));
  }
</script>

<div>
  <Button
    disabled={!targetMapping || loading}
    icon={Add16}
    kind="primary"
    on:click={onClicked}
  >
    Add Selected
  </Button>
  {#if loading}
    <InlineLoading />
  {/if}
</div>

<style>
  div {
    display: flex;
  }
</style>
