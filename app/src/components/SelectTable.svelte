<script lang="ts">
  import {
    Column,
    Table,
    TableHeader,
    TableRow,
    TableCell,
    TableHead,
    TableBody,
    DataTable,
    Tag,
    Checkbox,
    Pagination,
  } from "carbon-components-svelte";
  import type { SelectTableRow } from "src/models/SelectTableRow";

  export let rows: SelectTableRow[];

  const headers = ["Selected", "Sentence", "Source", "Tags"];
</script>

<DataTable>
  <Table>
    <TableHead>
      <TableRow>
        {#each headers as header}
          <TableHeader>{header}</TableHeader>
        {/each}
      </TableRow>
    </TableHead>
    <TableBody>
      {#each rows as row}
        <TableRow on:click={() => console.log('nice')}>
          <TableCell>
            <Checkbox bind:checked={row.selected} />
          </TableCell>
          <TableCell>
            <Column noGutterLeft>{row.sentece}</Column>
          </TableCell>
          <TableCell>{row.source}</TableCell>
          <TableCell>
            {#each row.tags as tag}
              <Tag>{tag}</Tag>
            {/each}
          </TableCell>
        </TableRow>
      {/each}
    </TableBody>
  </Table>
  <Pagination />
</DataTable>
