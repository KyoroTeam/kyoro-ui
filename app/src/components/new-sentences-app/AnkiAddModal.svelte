<script lang="ts">
  import { Modal, Select, SelectItem } from 'carbon-components-svelte';
  import { cardMappingStore } from '../../stores/settingsStore';
  import type { ICardMapping } from '../../stores/settingsStore';
  import DeckSelect from './DeckSelect.svelte';

  export let open: boolean = false;
  export let onSubmitted: (name: string | undefined) => void;

  let settings: ICardMapping[];
  cardMappingStore.subscribe((value) => (settings = value));

  let selectedDeckName: string;
  let selectedModelMapping: string;
</script>

<Modal
  size="xs"
  hasForm
  {open}
  modalHeading="Add To Anki"
  primaryButtonText="Confirm"
  secondaryButtonText="Cancel"
  on:close={() => onSubmitted(undefined)}
  on:submit={() => onSubmitted(undefined)}
>
  <DeckSelect disabled={false} bind:selected={selectedDeckName} />
  <br />
  <Select labelText="Field Mapping" bind:selected={selectedModelMapping}>
    {#each settings as setting}
      <SelectItem value={setting.mappingName} text={setting.mappingName} />
    {/each}
  </Select>
</Modal>
