<script>
  import {
    DataTable,
    Toolbar,
    ToolbarContent,
    ToolbarSearch,
    ToolbarMenu,
    ToolbarMenuItem,
    ToolbarBatchActions,
    Button,
    Pagination,
  } from 'carbon-components-svelte';
  import Save16 from 'carbon-icons-svelte/lib/Save16';
  import type { JibikiSenteceResponse } from 'src/models/Jibiki';
  import type { SelectTableRow } from 'src/models/SelectTableRow';

  // export let inputRows: JibikiSenteceResponse[];
  // export let tableRows: SelectTableRow[];

  const headers = [
    { key: 'name', value: 'Name' },
    { key: 'port', value: 'Port' },
    { key: 'rule', value: 'Rule' },
  ];

  interface row {
    id: string;
    name: string;
    port: number;
    rule: string;
  }

  const rows: row[] = [
    { id: 'a', name: 'Load Balancer 3', port: 3000, rule: 'Round robin' },
    { id: 'b', name: 'Load Balancer 1', port: 443, rule: 'Round robin' },
    { id: 'c', name: 'Load Balancer 2', port: 80, rule: 'DNS delegation' },
    { id: 'd', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: 'e', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
    { id: 'a2', name: 'Load Balancer 3', port: 3000, rule: 'Round robin' },
    { id: 'b2', name: 'Load Balancer 1', port: 443, rule: 'Round robin' },
    { id: 'c2', name: 'Load Balancer 2', port: 80, rule: 'DNS delegation' },
    { id: 'd2', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: 'e2', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f2', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
    { id: 'a3', name: 'Load Balancer 3', port: 3000, rule: 'Round robin' },
    { id: 'b3', name: 'Load Balancer 1', port: 443, rule: 'Round robin' },
    { id: 'c3', name: 'Load Balancer 2', port: 80, rule: 'DNS delegation' },
    { id: 'd3', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: 'e3', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f3', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
    { id: 'd4', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: 'e4', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f4', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
    { id: '1f3', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
    { id: '1d4', name: 'Load Balancer 6', port: 3000, rule: 'Round robin' },
    { id: '1e4', name: 'Load Balancer 4', port: 443, rule: 'Round robin' },
    { id: 'f14', name: 'Load Balancer 5', port: 80, rule: 'DNS delegation' },
  ];

  let selectedRowIds: string[] = [];

  let value: string = '';

  $: console.log('selectedRowIds', selectedRowIds);
</script>

<Pagination />
<DataTable
  on:click:row={a => {
    // TODO: Select/unselect row
    console.log(a);
  }}
  size="short"
  expandable
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
      <ToolbarSearch bind:value persistent placeholder="Narrow the results..." />
    </ToolbarContent>
  </Toolbar>
  <div slot="expanded-row" let:row>
    <pre>
      {JSON.stringify(row, null, 2)}
    </pre>
  </div>
</DataTable>
