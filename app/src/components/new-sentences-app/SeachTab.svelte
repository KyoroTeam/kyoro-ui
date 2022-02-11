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

  interface Row {
    id: number;
    sentence: string;
    source: string;
  }

  let rows: Row[] = [];

  let selectedRowIds: any[] = [];

  $: console.log('selectedRowIds', selectedRowIds);
</script>

<DataTable sortable batchSelection size="short" bind:selectedRowIds {headers} {rows}>
  <Toolbar>
    <ToolbarBatchActions>
      <Button
        icon={Save16}
        on:click={() => {
          console.log(selectedRowIds);
        }}>Save</Button
      >
    </ToolbarBatchActions>
    <ToolbarContent>
      <MiniSearchBar
        onSearchResults={(results) => {
          rows = results.map((result, i) => ({
            id: i,
            sentence: result.sentence,
            source: result.source,
          }));
        }}
      />
      <ToolbarMenu>
        <ToolbarMenuItem primaryFocus>Restart all</ToolbarMenuItem>
        <ToolbarMenuItem href="https://cloud.ibm.com/docs/loadbalancer-service">
          API documentation
        </ToolbarMenuItem>
        <ToolbarMenuItem danger>Stop all</ToolbarMenuItem>
      </ToolbarMenu>
    </ToolbarContent>
  </Toolbar>
</DataTable>
