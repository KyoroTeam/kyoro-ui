<script lang="ts">
  import { Button, Checkbox, Column, Row, Tile } from 'carbon-components-svelte';
  import Edit16 from 'carbon-icons-svelte/lib/Edit16';
  import CheckboxChecked16 from 'carbon-icons-svelte/lib/CheckboxChecked16';
  import ArrowRight16 from "carbon-icons-svelte/lib/ArrowRight16";
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
<div class="col">
  <h5>Target Model</h5>
  <ModelSelect disabled={!editing} bind:selected={selectedModelName} />
  <div class="row" style="padding-top: 30px; padding-bottom: 10px; justify-content: space-between">
    <h5>Kyoro Field</h5>
    <h5>Target Model Field</h5>
  </div>
  <div class="row" style="justify-content: space-between">
    <div class="col" style="justify-content: center; padding-right: 20px">
      <Checkbox disabled={!editing}  labelText="Japanese" style="flex-grow: 0" />
    </div>
    <div class="col" style="justify-content: center; padding-right: 20px">
      <ArrowRight16/>
    </div>
    <div class="row select-wrapper">
      <ModelFieldSelect
        disabled={!editing}
        modelName={selectedModelName}
        bind:selected={japaneseValue}
      />
    </div>
  </div>
  <div class="row" style="justify-content: space-between">
    <div class="col" style="justify-content: center; padding-right: 20px">
      <Checkbox disabled={!editing}  labelText="Japanese" style="flex-grow: 0" />
    </div>
    <div class="col" style="justify-content: center; padding-right: 20px">
      <ArrowRight16/>
    </div>
    <div class="row select-wrapper">
      <ModelFieldSelect
        disabled={!editing}
        modelName={selectedModelName}
        bind:selected={japaneseValue}
      />
    </div>
  </div>  
</div>
</Tile>
</Row>

<style>
  .select-wrapper {
    background-color: #f4f4f4;
  }
  .row {
    display: flex;
    flex-direction: row;
  }

  .col {
    display: flex;
    flex-direction: column;
  }

  .mapping-title {
    display: flex;
    flex-direction: row;
    width: 100%;
  }
</style>
