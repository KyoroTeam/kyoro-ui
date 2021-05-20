<script lang="ts">
  import {
    Table,
    TableHeader,
    TableRow,
    TableCell,
    TableHead,
    TableBody,
    DataTable,
    Checkbox,
    Pagination,
  } from "carbon-components-svelte";
  import type { JibikiSenteceResponse } from "src/models/Jibiki";
  import type { SelectTableRow } from "src/models/SelectTableRow";

  export let inputRows: JibikiSenteceResponse[];
  export let tableRows: SelectTableRow[];

  $: tableRows = inputRows.map((row) => ({
    selected: false,
    sentence: row.translations[0]?.sentence,
    english: row.sentence,
    tags: row.tags,
    source: "Jibiki",
  }));

  function onSelected(index: number) {
    tableRows[index].selected = !tableRows[index].selected;
  }

  const headers = ["", "Sentence", "Source", ""];
</script>

<DataTable style={"width:100%"}>
  <Table>
    <TableHead>
      <TableRow>
        {#each headers as header}
          <TableHeader>{header}</TableHeader>
        {/each}
      </TableRow>
    </TableHead>
    <TableBody>
      {#each tableRows as row, i}
        <TableRow on:click={() => onSelected(i)}>
          <TableCell>
            <Checkbox bind:checked={row.selected} />
          </TableCell>
          <TableCell>
            <div class="box">
              <p>{row.sentence}</p>
              <p>{row.english}</p>
            </div>
          </TableCell>
          <TableCell>{row.source}</TableCell>
          <TableCell />
        </TableRow>
      {/each}
    </TableBody>
  </Table>
  <Pagination />
</DataTable>

<style>
  .box {
    display: flex;
    flex-direction: column;
  }
</style>
