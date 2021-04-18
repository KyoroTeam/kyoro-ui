<script lang="ts">
  import {
    Row,
    Button,
    ToastNotification,
    Column,
  } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import { cardMappingStore } from "../stores/settingsStore";
  import type { ICardMapping } from "../stores/settingsStore";
  import MappingCreator from "./MappingCreator.svelte";
  import MappingAddModal from "./MappingAddModal.svelte";

  let cardMappings: ICardMapping[];
  cardMappingStore.subscribe((value) => (cardMappings = value));

  let modalOpen: boolean = false;
</script>

{#if cardMappings?.length > 0}
  <Row>
    {#each cardMappings as mapping}
      <Column padding md={4}>
        <MappingCreator mappingName={mapping.mappingName} />
      </Column>
    {/each}
  </Row>
{:else}
  <ToastNotification
    lowContrast
    kind="info-square"
    hideCloseButton
    title="No Mappings Defined"
    caption="Click Add New to create a model mapping."
  />
{/if}

<Button
  hasIconOnly
  iconDescription={"Add New"}
  tooltipPosition="top"
  icon={Add16}
  on:click={() => {
    modalOpen = true;
  }}
/>

<MappingAddModal
  open={modalOpen}
  onSubmitted={(mappingName) => {
    modalOpen = false;
    if (mappingName !== undefined) {
      cardMappingStore.update((value) => [
        ...value,
        {
          deckName: "",
          mappingName: mappingName,
          modelName: "",
          modelFieldMappings: {},
        },
      ]);
    }
  }}
/>
