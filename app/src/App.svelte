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
    Tag,
    Checkbox,
    Pagination,
    ButtonSet,
  } from 'carbon-components-svelte';
  import AnkiConectGate from './components/AnkiConectGate.svelte';
  import Header from './components/Header.svelte';
  import Theme from './components/Theme.svelte';
  import AnkiConnectProvider from './services/AnkiConnectProvider.svelte';
  import Add16 from 'carbon-icons-svelte/lib/Add16';
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
  const headers = ['Use', 'Sentence', 'Source', 'Tags'];
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
                    <Column lg={8}>
                      <ButtonSet>
                        <Search placeholder="Enter a phrase..." />
                        <Button>Search</Button>
                      </ButtonSet>
                    </Column>
                    <Column lg={4}>
                      <MultiSelect
                        size="xl"
                        label="Sentence Sources"
                        items={[{ id: '0', text: 'Slack' }, { id: '1', text: 'Email' }, { id: '2', text: 'Fax' }]}
                        selectedIds={['0', '1']} />
                    </Column>
                  </Row>
                  <Row class="py-4">
                    <Column md={4} lg={12}>
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
                                  <Checkbox />
                                </TableCell>
                                <TableCell>
                                  <Column class="py-1" noGutterLeft>
                                    <p class="border-gray-400">I could not persuade him that it was true.</p>
                                    <p>それが本当だと彼に<b>納得</b>させることができなかった。</p>
                                  </Column>
                                </TableCell>
                                <TableCell>Tatoeba</TableCell>
                                <TableCell>
                                  <Tag>List 907</Tag>
                                  <Tag>male name</Tag>
                                </TableCell>
                                <!-- {#each Object.keys(row).filter(key => key !== 'id') as key}
                                  <TableCell>{row[key]}</TableCell>
                                {/each} -->
                              </TableRow>
                            {/each}
                          </TableBody>
                        </Table>
                      </DataTable>
                      <Pagination/>
                    </Column>
                  </Row>
                  <Row class="pt-1">
                    <Column lg={6}>
                      <ButtonSet>
                        <Select labelText="Target Deck" selected="g10">
                          <SelectItem value="white" text="White" />
                          <SelectItem value="g10" text="Gray 10" />
                          <SelectItem value="g90" text="Gray 90" />
                          <SelectItem value="g100" text="Gray 100" />
                        </Select>
                        <Select labelText="Target Note" selected="g10">
                          <SelectItem value="white" text="White" />
                          <SelectItem value="g10" text="Gray 10" />
                          <SelectItem value="g90" text="Gray 90" />
                          <SelectItem value="g100" text="Gray 100" />
                        </Select>
                      </ButtonSet>
                    </Column>
                    <Column lg={{ span: 2, offset: 4 }}>
                      <Button icon={Add16}>Add Selected</Button>
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
