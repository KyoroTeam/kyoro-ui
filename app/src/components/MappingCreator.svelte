<script lang="ts">
  import { Button, Column, Row, Tile } from "carbon-components-svelte";
  import Edit16 from "carbon-icons-svelte/lib/Edit16";
  import CheckboxChecked16 from "carbon-icons-svelte/lib/CheckboxChecked16";
  import CloseFilled16 from "carbon-icons-svelte/lib/CloseFilled16";
  import Delete16 from "carbon-icons-svelte/lib/Delete16";
  import ModelFieldSelect from "./ModelFieldSelect.svelte";
  import ModelSelect from "./ModelSelect.svelte";

  import settingsStore from "../stores/settingsStore";

  export let mappingName: string;

  let selectedModelName: string;
  let editing: boolean = false;
</script>

<style>
  .mapping-title {
    display: flex;
    flex-direction: row;
    width: 100%;
  }
</style>

<Column md={2} style="padding-top:20px">
  <Tile>
    <Row>
      <Column>
        <Tile light>
          <Row>
            <div class="mapping-title">
              <p
                style="display:flex;align-items:center;width:100%;padding-left:10px">
                {mappingName}
              </p>
              <Button
                size={'small'}
                hasIconOnly
                iconDescription={editing ? 'Save Changes' : 'Edit'}
                tooltipPosition="top"
                icon={editing ? CheckboxChecked16 : Edit16}
                on:click={() => (editing = !editing)} />
              {#if editing}
                <Button
                  size={'small'}
                  hasIconOnly
                  kind="ghost"
                  iconDescription={'Discard Changes'}
                  tooltipPosition="top"
                  icon={CloseFilled16}
                  on:click={() => (editing = false)} />
              {/if}
              <Button
                size={'small'}
                hasIconOnly
                kind="ghost"
                iconDescription={'Delete'}
                tooltipPosition="top"
                icon={Delete16}
                on:click={() => {
                  settingsStore.update((value) => ({
                    ...value,
                    cardMappings: value.cardMappings.filter(
                      (m) => m.mappingName !== mappingName
                    ),
                  }));
                }} />
            </div>
          </Row>
        </Tile>
        <ModelSelect disabled={!editing} bind:selected={selectedModelName} />
      </Column>
      <Column>
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="English" />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Japanese" />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Source" />
        <ModelFieldSelect
          disabled={!editing}
          modelName={selectedModelName}
          label="Tags" />
      </Column>
    </Row>
  </Tile>
</Column>
