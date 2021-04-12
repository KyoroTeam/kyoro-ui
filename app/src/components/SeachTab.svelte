<script lang="ts">
  import { Row, Column, MultiSelect } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "src/stores/settingsStore";
  import AnkiAddButton from "./AnkiAddButton.svelte";
  import CardMappingSelect from "./CardMappingSelect.svelte";
  import SearchBar from "./SearchBar.svelte";
  import SelectTable from "./SelectTable.svelte";

  let searchedSentences: JibikiSenteceResponse[] = [];
  let selectedMapping: ICardMapping | undefined;
  let allTableRows: SelectTableRow[] = [];
  $: selectedTableRows = allTableRows.filter((r) => r.selected);
</script>

<Row padding>
  <Column>
    <SearchBar bind:sentences={searchedSentences} />
  </Column>
</Row>
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
