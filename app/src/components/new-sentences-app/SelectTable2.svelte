<script>
  import {
    DataTable,
    Toolbar,
    ToolbarContent,
    ToolbarSearch,
    ToolbarBatchActions,
    Button,
  } from 'carbon-components-svelte';
  import Save16 from 'carbon-icons-svelte/lib/Save16';
  import type { SentecePart, JibikiSenteceResponse } from 'src/models/Jibiki';

  export let inputRows: JibikiSenteceResponse[];

  const headers = [
    { key: 'sentence', value: 'Sentence' },
    { key: 'source', value: 'Source' },
  ];

  interface row {
    id: string;
    english: string | undefined;
    sentenceParts: SentecePart[];
    source: string;
  }

  let rows: row[];
  $: rows = inputRows.map((r, i) => ({
    id: `${i}`,
    english: r.translations[0].sentence,
    sentenceParts: r.sentenceParts,
    source: r.source,
  }));

  let selectedRowIds: string[] = [];
  let searchValue: string = '';
</script>

<DataTable
  sortable
  on:click:row={a => {
    // TODO: Select/unselect row
    console.log(a);
  }}
  size="short"
  stickyHeader
  batchSelection
  bind:selectedRowIds
  {headers}
  {rows}
>
  <Toolbar>
    <ToolbarBatchActions>
      <Button icon={Save16}>Add To Anki</Button>
    </ToolbarBatchActions>
    <ToolbarContent>
      <ToolbarSearch bind:value={searchValue} persistent placeholder="Narrow the results..." />
    </ToolbarContent>
  </Toolbar>
  <div slot="expanded-row" let:row>
    <pre>
      {JSON.stringify(row, null, 2)}
    </pre>
  </div>
  <span slot="cell" let:row let:cell>
    {#if cell.key === 'sentence'}
      <div class="sentenceCell">
        {#each row.sentenceParts as part}
          <span class={part.highlight ? 'highlight' : ''}>{part.part}</span>
        {/each}
        {row.english}
      </div>
    {:else if cell.key === 'source'}
      <div class="sourceCell">
        {row.source}
      </div>
    {:else}{cell.value}{/if}
  </span>
</DataTable>

<style>
  .sourceCell {
    padding-left: 5px;
  }
  .highlight {
    border-radius: 5px;
    background-color: aquamarine;
  }
  :global(tr > th:nth-of-type(3)) {
    padding-left: 2px;
    width: 33% !important;
  }
  :global(tr > td:nth-of-type(3)) {
    width: 33% !important;
  }
</style>
