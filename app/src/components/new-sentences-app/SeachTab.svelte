<script lang="ts">
  import { Row, Column } from "carbon-components-svelte";
  import { slide, fade } from "svelte/transition";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "../../stores/settingsStore";
  import AnkiAddButton from "./AnkiAddButton.svelte";
  import CardMappingSelect from "./CardMappingSelect.svelte";
  import SearchBar from "./SearchBar.svelte";
  import SelectTable from "./SelectTable.svelte";
  import Search32 from "carbon-icons-svelte/lib/Search32";

  let searchedSentences: JibikiSenteceResponse[] = [];
  let selectedMapping: ICardMapping | undefined;
  let allTableRows: SelectTableRow[] = [];
  $: selectedTableRows = allTableRows.filter((r) => r.selected);
</script>

<Row style={"margin-bottom: 20px"}>
  <SearchBar bind:sentences={searchedSentences} />
</Row>

{#if searchedSentences?.length > 0}
  <div in:fade out:slide>
    <Row padding>
      <SelectTable
        bind:inputRows={searchedSentences}
        bind:tableRows={allTableRows}
      />
    </Row>
    <Row>
      <Column>
        <CardMappingSelect bind:selected={selectedMapping} />
        <AnkiAddButton
          targetMapping={selectedMapping}
          disabled={selectedTableRows.length === 0}
          disabledHint={"No sentences are selected"}
          tableRows={selectedTableRows}
        />
      </Column>
    </Row>
  </div>
{:else}
  <div class="box">
    <Search32 />
    <h4>Sentence results will appear here</h4>
  </div>
{/if}

<style>
  .box {
    margin-top: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
</style>
