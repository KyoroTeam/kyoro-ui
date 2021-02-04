<script lang="ts">
  import {
    Row,
    Column,
    MultiSelect,
    ButtonSet,
  } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import type { ICardMapping } from "src/stores/settingsStore";
  import AnkiAddButton from "./AnkiAddButton.svelte";
  import CardMappingSelect from "./CardMappingSelect.svelte";
  import SearchBar from "./SearchBar.svelte";
  import SelectTable from "./SelectTable.svelte";

  let searchedSentences: JibikiSenteceResponse[] = [];
  let tableRows: SelectTableRow[] = [];
  let selectedMapping: ICardMapping | undefined;
  $: console.log(selectedMapping);
</script>

<Row>
  <Column>
    <SearchBar bind:sentences={searchedSentences} />
  </Column>
  <Column>
    <MultiSelect
      size="xl"
      label="Sentence Sources"
      items={[
        { id: "0", text: "Slack" },
        { id: "1", text: "Email" },
        { id: "2", text: "Fax" },
      ]}
      selectedIds={["0", "1"]}
    />
  </Column>
</Row>
<Row>
  <Column>
    <SelectTable bind:inputRows={searchedSentences} bind:tableRows />
  </Column>
</Row>
<Row>
  <Column>
    <CardMappingSelect bind:selected={selectedMapping} />
    <AnkiAddButton targetMapping={selectedMapping} {tableRows} />
  </Column>
</Row>
