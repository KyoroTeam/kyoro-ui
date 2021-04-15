<script lang="ts">
  import { Row, Column } from "carbon-components-svelte";
  import { slide, fly } from "svelte/transition";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "src/stores/settingsStore";
  import AnkiAddButton from "./AnkiAddButton.svelte";
  import CardMappingSelect from "./CardMappingSelect.svelte";
  import SearchBar from "./SearchBar.svelte";
  import SelectTable from "./SelectTable.svelte";
  import Search32 from "carbon-icons-svelte/lib/Search32";

  let searchedSentences: JibikiSenteceResponse[] = [];
  let selectedMapping: ICardMapping | undefined;
  let allTableRows: SelectTableRow[] = [];
  $: selectedTableRows = allTableRows.filter((r) => r.selected);
  $: {
    console.log(allTableRows);
  }
</script>

<Row>
  <Column>
    <SearchBar bind:sentences={searchedSentences} />
  </Column>
</Row>

{#if searchedSentences?.length > 0}
  <div in:fly out:slide>
    <Row>
      <Column>
        <SelectTable
          bind:inputRows={searchedSentences}
          bind:tableRows={allTableRows}
        />
      </Column>
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
