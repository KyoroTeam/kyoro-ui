<script lang="ts">
  import { Button, Column, Row, Tile } from 'carbon-components-svelte';
  import Edit16 from 'carbon-icons-svelte/lib/Edit16';
  import CheckboxChecked16 from 'carbon-icons-svelte/lib/CheckboxChecked16';
  import CloseFilled16 from 'carbon-icons-svelte/lib/CloseFilled16';
  import Delete16 from 'carbon-icons-svelte/lib/Delete16';
  import ModelFieldSelect from './ModelFieldSelect.svelte';
  import ModelSelect from './ModelSelect.svelte';

  import { cardMappingStore } from '../../stores/settingsStore';
  import type { ICardMapping } from '../../stores/settingsStore';

  export let mappingName: string;

  let selectedModelName: string;
  let englishValue: string;
  let japaneseValue: string;
  let tagsValue: string;
  let sourceValue: string;

  let newMapping: ICardMapping;
  $: newMapping = {
    mappingName: mappingName,
    modelName: selectedModelName,
    modelFieldMappings: {
      English: englishValue,
      Japanese: japaneseValue,
      Tags: tagsValue,
      Source: sourceValue,
    },
  };

  function updateThisCardMapping() {
    cardMappingStore.update((value) => {
      const thisIndex = value.findIndex((m) => (m.mappingName = mappingName));
      if (thisIndex != -1) {
        value[thisIndex] = newMapping;
      } else {
        value.push(newMapping);
      }
      console.log(value);
      return value;
    });
  }

  let editing: boolean = false;
</script>

<Row>
  <Tile>
    <Row>
      <div class="mapping-title">
        <h4 style={'padding-right: 10px; padding-left: 10px'}>
          {mappingName}
        </h4>
        <Button
          size={'small'}
          hasIconOnly
          iconDescription={editing ? 'Save Changes' : 'Edit'}
          tooltipPosition="top"
          icon={editing ? CheckboxChecked16 : Edit16}
          on:click={() => {
            if (editing) {
              updateThisCardMapping();
            }
            editing = !editing;
          }}
        />
        {#if editing}
          <Button
            size={'small'}
            hasIconOnly
            kind="ghost"
            iconDescription={'Discard Changes'}
            tooltipPosition="top"
            icon={CloseFilled16}
            on:click={() => (editing = false)}
          />
        {/if}
        <Button
          size={'small'}
          hasIconOnly
          kind="ghost"
          iconDescription={'Delete'}
          tooltipPosition="top"
          icon={Delete16}
          on:click={() => {
            cardMappingStore.update((value) => value.filter((m) => m.mappingName !== mappingName));
          }}
        />
      </div>
    </Row>
  </Tile>
</Row>
<Row>
  <Tile>
    <Row>
      <Column style={'border-right: solid 1px'}>
        <h5>Model To Map</h5>
        <br />
        <ModelSelect disabled={!editing} bind:selected={selectedModelName} />
      </Column>
      <Column>
        <h5>Model Field Mappings</h5>
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="English"
          bind:selected={englishValue}
        />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Japanese"
          bind:selected={japaneseValue}
        />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Source"
          bind:selected={sourceValue}
        />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Tags"
          bind:selected={tagsValue}
        />
      </Column>
    </Row>
  </Tile>
</Row>

<style>
  .mapping-title {
    display: flex;
    flex-direction: row;
    width: 100%;
  }
</style>
