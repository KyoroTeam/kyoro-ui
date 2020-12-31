<script lang="ts">
  import {
    Row,
    Column,
    Select,
    SelectItem,
    Button,
    MultiSelect,
    ButtonSet,
  } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";
  import DeckSelect from "./DeckSelect.svelte";
  import SearchBar from "./SearchBar.svelte";
  import SelectTable from "./SelectTable.svelte";

  let searchedSentences: JibikiSenteceResponse[] = [];

  let rows: SelectTableRow[] = [];
  $: {
    rows = searchedSentences.map((s) => ({
      selected: false,
      sentece: s.translations[0]?.sentence,
      tags: s.tags,
      source: "Jibiki",
    }));
  }

  console.log(searchedSentences, rows);
</script>

<Row>
  <Column>
    <SearchBar bind:sentences={searchedSentences} />
  </Column>
  <Column>
    <MultiSelect
      size="xl"
      label="Sentence Sources"
      items={[{ id: '0', text: 'Slack' }, { id: '1', text: 'Email' }, { id: '2', text: 'Fax' }]}
      selectedIds={['0', '1']} />
  </Column>
</Row>
<Row>
  <Column>
    <SelectTable bind:rows />
  </Column>
</Row>
<Row>
  <Column>
    <ButtonSet>
      <DeckSelect />
      <Select labelText="Target Note" selected="g10">
        <SelectItem value="white" text="White" />
        <SelectItem value="g10" text="Gray 10" />
        <SelectItem value="g90" text="Gray 90" />
        <SelectItem value="g100" text="Gray 100" />
      </Select>
    </ButtonSet>
  </Column>
  <Column lg={{ span: 2, offset: 4 }}>
    <Button icon={Add16} disabled={rows.filter((r) => r.selected).length == 0}>
      Add Selected
    </Button>
  </Column>
</Row>
