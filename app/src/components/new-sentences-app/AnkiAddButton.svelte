<script lang="ts">
  import {
    Button,
    InlineLoading,
    TooltipDefinition,
  } from "carbon-components-svelte";
  import type { ButtonProps } from "carbon-components-svelte/types/Button/Button";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "../../stores/settingsStore";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "src/services/ankiconect";

  export let tableRows: SelectTableRow[] = [];
  export let targetMapping: ICardMapping | undefined;
  export let disabled: boolean = false;
  export let disabledHint: string | undefined = undefined;

  const anki = getContext<IAnkiConnect>("anki");

  let loading: boolean = false;
  let errorMessage: string;

  function onClicked() {
    const { deckName, modelName, modelFieldMappings } = targetMapping!;
    console.log(targetMapping);
    loading = true;
    // TODO: Warn or something if the primary fiels is empoty, otherwise
    // "cannot create note because it is empty" will occur
    const resolvedValues = {
      [modelFieldMappings["English"]!]: tableRows[0].english,
      [modelFieldMappings["Japanese"]!]: tableRows[0].sentence,
      [modelFieldMappings["Source"]!]: tableRows[0].source,
      [modelFieldMappings["Tags"]!]: tableRows[0].tags.join(","),
    };
    anki
      .addNote(deckName, modelName, resolvedValues)
      .then((r) => {
        if (r.error) errorMessage = r.error;
      })
      .catch(() => (errorMessage = "Couldn't connect to Anki"))
      .finally(() => (loading = false));
  }

  let buttonBaseProps: ButtonProps;
  $: buttonBaseProps = {
    disabled: !targetMapping || loading || disabled,
    icon: Add16,
    kind: "primary",
  };
</script>

<div>
  {#if disabled && disabledHint}
    <TooltipDefinition tooltipText={disabledHint}>
      <Button {...buttonBaseProps}>Add Selected</Button>
    </TooltipDefinition>
  {:else}
    <Button on:click={onClicked} {...buttonBaseProps}>Add Selected</Button>
  {/if}

  {#if loading}
    <InlineLoading />
  {/if}
</div>

<style>
  div {
    display: flex;
  }
</style>
