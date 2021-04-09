<script lang="ts">
  import {
    Row,
    Button,
    ToastNotification,
    Column,
  } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import settingsStore from "../stores/settingsStore";
  import type { IUserSettings } from "../stores/settingsStore";
  import MappingCreator from "./MappingCreator.svelte";
  import MappingAddModal from "./MappingAddModal.svelte";

  let settings: IUserSettings;
  settingsStore.subscribe((value) => (settings = value));

  let modalOpen: boolean = false;
</script>

{#if settings.cardMappings?.length > 0}
  <Row>
    {#each settings.cardMappings as mapping}
      <Column padding md={4}>
        <MappingCreator mappingName={mapping.mappingName} />
      </Column>
    {/each}
  </Row>
{:else}
  <ToastNotification
    kind="info"
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
  onSubmitted={(possibleName) => {
    modalOpen = false;
    if (possibleName !== undefined) {
      settingsStore.update((v) => ({
        ...v,
        cardMappings: [
          ...v.cardMappings,
          {
            deckName: "",
            mappingName: possibleName,
            modelName: "",
            modelFieldMappings: {},
          },
        ],
      }));
    }
  }}
/>
