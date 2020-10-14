<script lang="ts">
  import {
    Content,
    Breadcrumb,
    BreadcrumbItem,
    Grid,
    Row,
    Column,
    Tabs,
    TabContent,
    Tab,
    Select,
    SelectItem,
    Table,
    TableHeader,
    TableContainer,
    TableRow,
    TableCell,
    TableHead,
    TableBody,
    Search,
    Button,
    DataTable,
    MultiSelect,
  } from 'carbon-components-svelte';
  import AnkiConectGate from './components/AnkiConectGate.svelte';
  import Header from './components/Header.svelte';
  import Theme from './components/Theme.svelte';
  import AnkiConnectProvider from './services/AnkiConnectProvider.svelte';
  let theme: 'g10' = 'g10';

  const rows = [
    {
      id: 'load-balancer-1',
      name: 'Load Balancer 1',
      rule: 'Round robin',
      Status: 'Starting',
    },
    {
      id: 'load-balancer-2',
      name: 'Load Balancer 2',
      rule: 'DNS delegation',
      status: 'Active',
    },
    {
      id: 'load-balancer-3',
      name: 'Load Balancer 3',
      rule: 'Round robin',
      status: 'Disabled',
    },
  ];
  const headers = ['Name', 'Rule', 'Status'];
</script>

<Theme bind:theme>
  <Header />
  <Content style="background: none; padding: 1rem">
    <Grid>
      <Row>
        <Column noGutter>
          <Tabs aria-label="Tab navigation">
            <Tab label="Search" />
            <Tab label="Sources" />
            <Tab label="Settings" />
            <div slot="content" class="tabbed-content">
              <Grid as fullWidth let:props>
                <TabContent {...props}>
                  <Row>
                    <Column md={4} lg={7}>
                      <Search placeholder="Enter a phrase..." />
                    </Column>
                    <Column>
                      <MultiSelect
                        size="xl"
                        label="Sentence Sources"
                        items={[{ id: '0', text: 'Slack' }, { id: '1', text: 'Email' }, { id: '2', text: 'Fax' }]}
                        selectedIds={['0', '1']} />
                    </Column>
                    <Column>
                      <Button>Search</Button>
                    </Column>
                  </Row>
                  <Row>
                    <Column md={4} lg={8}>
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
                              <TableRow>
                                {#each Object.keys(row).filter(key => key !== 'id') as key}
                                  <TableCell>{row[key]}</TableCell>
                                {/each}
                              </TableRow>
                            {/each}
                          </TableBody>
                        </Table>
                      </DataTable>
                    </Column>
                  </Row>
                </TabContent>
                <TabContent {...props}>
                  <Row />
                </TabContent>
                <TabContent {...props}>
                  <Row>
                    <Column md={4} lg={7}>
                      <AnkiConnectProvider>
                        <AnkiConectGate>OK</AnkiConectGate>
                      </AnkiConnectProvider>
                    </Column>
                  </Row>
                </TabContent>
              </Grid>
            </div>
          </Tabs>
        </Column>
      </Row>
    </Grid>
  </Content>
</Theme>
