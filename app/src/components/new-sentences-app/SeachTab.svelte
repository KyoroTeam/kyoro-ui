<script lang="ts">
  import {
    DataTable,
    Toolbar,
    ToolbarContent,
    ToolbarSearch,
    ToolbarMenu,
    ToolbarMenuItem,
    ToolbarBatchActions,
    Button,
  } from 'carbon-components-svelte';
  import Save16 from 'carbon-icons-svelte/lib/Save16';
  import MiniSearchBar from './MiniSearchBar.svelte';

  const headers = [
    { key: 'name', value: 'Sentence' },
    { key: 'port', value: 'English' },
    { key: 'rule', value: 'Source' },
  ];

  const rows = [
    { id: 'a', name: 'Load Balancer 3', port: 3000, rule: 'Round robin' },
    { id: 'b', name: 'Load Balancer 1', port: 443, rule: 'Round robin' },
    { id: 'c', name: 'Load Balancer 2', port: 80, rule: 'DNS delegation' },
    { id: 'd', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: 'e', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
  ];

  let selectedRowIds: any[] = [];

  $: console.log('selectedRowIds', selectedRowIds);
</script>

<DataTable size="short" batchSelection bind:selectedRowIds {headers} {rows}>
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
      <MiniSearchBar />
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
