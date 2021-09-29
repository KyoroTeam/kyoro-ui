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
  } from 'carbon-components-svelte';
  import type { JibikiSenteceResponse } from 'src/models/Jibiki';
  import type { SelectTableRow } from 'src/models/SelectTableRow';

  export let inputRows: JibikiSenteceResponse[];
  export let tableRows: SelectTableRow[];

  $: tableRows = inputRows.map(row => ({
    selected: false,
    sentenceParts: row.sentenceParts,
    english: row.translations[0]?.sentence,
    tags: row.tags,
    source: row.source,
  }));

  function onSelected(index: number) {
    tableRows[index].selected = !tableRows[index].selected;
  }

  const headers = ['Sentence', 'Source'];
</script>

<DataTable size="tall">
  <Table>
    <TableHead>
      <TableRow>
        {#each headers as header}
          <TableHeader>{header}</TableHeader>
        {/each}
      </TableRow>
    </TableHead>
    <TableBody>
      <div class="test">
        {#each tableRows as row, i}
          <TableRow on:click={() => onSelected(i)}>
            <TableCell>
              <Checkbox bind:checked={row.selected} />
            </TableCell>
            <TableCell>
              {#each row.sentenceParts as part}
                <span class={part.highlight ? 'highlight' : ''}>{part.part}</span>
              {/each}
              {row.english ?? ''}
            </TableCell>
            <TableCell>{row.source}</TableCell>
            <TableCell />
          </TableRow>
        {/each}
      </div>
    </TableBody>
  </Table>
</DataTable>

<style>
  .highlight {
    border-radius: 5px;
    background-color: aquamarine;
  }
  .test {
    max-height: 90vh;
    overflow-y: scroll;
  }
</style>
