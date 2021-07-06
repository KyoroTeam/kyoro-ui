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
    sentenceParts: row.sentenceParts,
    english: row.translations[0]?.sentence,
    tags: row.tags,
    source: "Jibiki",
  }));

  function onSelected(index: number) {
    tableRows[index].selected = !tableRows[index].selected;
  }

  const headers = ["", "Sentence", "Source", ""];
</script>

<div class="highlight" />
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
            {#each row.sentenceParts as part}
              <span class={part.highlight ? "highlight" : ""}>{part.part}</span>
            {/each}
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
  .highlight {
    border-radius: 4px;
    background-color: aquamarine;
  }
</style>
