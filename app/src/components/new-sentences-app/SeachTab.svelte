<script lang="ts">
  import {
    DataTable,
    Toolbar,
    ToolbarContent,
    ToolbarMenu,
    ToolbarMenuItem,
    ToolbarBatchActions,
    Button,
  } from 'carbon-components-svelte';
  import Save16 from 'carbon-icons-svelte/lib/Save16';
  import MiniSearchBar from './MiniSearchBar.svelte';

  const headers = [
    { key: 'sentence', value: 'Sentence' },
    { key: 'source', value: 'Source' },
  ];

  interface KySentenceChunk {
    str: string;
    highlight: boolean;
  }

  interface Row {
    id: number;
    sentence: KySentenceChunk[];
    source: string;
  }

  let rows: Row[] = [];

  let selectedRowIds: any[] = [];

  function generateHighlightHtml(sentenceChunks: KySentenceChunk[]): string {
    function getString(chunk: KySentenceChunk) {
      if (chunk.highlight) {
        return `<span class='sentence-highlight'>${chunk.str}</span>`;
      } else {
        return `<span>${chunk.str}</span>`;
      }
    }
    return sentenceChunks.reduce((prev, cur) => `${prev}${getString(cur)}`, '');
  }

  $: console.log('selectedRowIds', selectedRowIds);
</script>

<DataTable sortable batchSelection size="short" bind:selectedRowIds {headers} {rows}>
  <svelte:fragment slot="cell" let:row let:cell>
    {#if cell.key === 'sentence'}
      {@html generateHighlightHtml(row['sentence'])}
    {:else}
      {cell.value}
    {/if}
  </svelte:fragment>
  <Toolbar>
    <ToolbarBatchActions>
      <Button
        icon={Save16}
        on:click={() => {
          console.log(selectedRowIds);
        }}
      >
        Save
      </Button>
    </ToolbarBatchActions>
    <ToolbarContent>
      <MiniSearchBar
        onSearchResults={(results) => {
          rows = results.map((result, i) => ({
            id: i,
            sentence: result.sentenceChunks,
            source: result.source,
          }));
        }}
      />
      <ToolbarMenu>
        <ToolbarMenuItem primaryFocus>Restart all</ToolbarMenuItem>
        <ToolbarMenuItem href="https://cloud.ibm.com/docs/loadbalancer-service">API documentation</ToolbarMenuItem>
        <ToolbarMenuItem danger>Stop all</ToolbarMenuItem>
      </ToolbarMenu>
    </ToolbarContent>
  </Toolbar>
</DataTable>

<style global>
  .sentence-highlight {
    background-color: lightblue;
    border-radius: 6px;
  }
</style>
