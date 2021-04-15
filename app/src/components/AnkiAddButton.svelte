<script lang="ts">
  import {
    Button,
    InlineLoading,
    Tooltip,
    TooltipDefinition,
  } from "carbon-components-svelte";
  import type { ButtonProps } from "carbon-components-svelte/types/Button/Button";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "../stores/settingsStore";
  import { getContext } from "svelte";
  import type { IAnkiConnect } from "../services/ankiconect";

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

  let buttonProps: ButtonProps;
  $: buttonProps = {
    disabled: !targetMapping || loading || disabled,
    icon: Add16,
    kind: "primary",
    onclick: onClicked,
  };
</script>

<div>
  {#if disabled && disabledHint}
    <TooltipDefinition tooltipText={disabledHint}>
      <Button {...buttonProps}>Add Selected</Button>
    </TooltipDefinition>
  {:else}
    <Button {...buttonProps}>Add Selected</Button>
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
