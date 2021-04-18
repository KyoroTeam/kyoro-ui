<script lang="ts">
  import { Modal, TextInput } from "carbon-components-svelte";
  import { cardMappingStore } from "../../stores/settingsStore";
  import type { ICardMapping } from "../../stores/settingsStore";

  export let open: boolean = false;
  export let onSubmitted: (name: string | undefined) => void;

  let settings: ICardMapping[];
  cardMappingStore.subscribe((value) => (settings = value));

  let mappingName: string;

  function validateMappingName(name: string): [boolean, string] {
    if (!mappingName || mappingName?.length === 0) {
      return [false, "Please enter a name"];
    } else if (settings?.find((m) => m.mappingName === mappingName)) {
      return [false, "A mapping already exists with that name."];
    }
    return [true, ""];
  }

  $: validResults = validateMappingName(mappingName);
</script>

<Modal
  size="xs"
  hasForm
  {open}
  modalHeading="Create Model Mapping"
  primaryButtonText="Confirm"
  primaryButtonDisabled={!validResults[0]}
  secondaryButtonText="Cancel"
  on:open={() => (mappingName = "")}
  on:click:button--secondary={() => onSubmitted(undefined)}
  on:close={() => onSubmitted(undefined)}
  on:submit={() => onSubmitted(mappingName)}
>
  <TextInput
    required
    invalid={!validResults[0]}
    invalidText={validResults[1]}
    placeholder="Enter mapping name"
    bind:value={mappingName}
  />
</Modal>
