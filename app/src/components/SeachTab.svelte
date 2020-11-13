<script lang="ts">
  import {
    Row,
    Column,
    Select,
    SelectItem,
    Table,
    TableHeader,
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
  } from "carbon-components-svelte";
  import Add16 from "carbon-icons-svelte/lib/Add16";
  import DeckSelect from "./DeckSelect.svelte";
  const rows = [
    {
      id: "load-balancer-1",
      name: "Load Balancer 1",
      rule: "Round robin",
      Status: "Starting",
    },
    {
      id: "load-balancer-2",
      name: "Load Balancer 2",
      rule: "DNS delegation",
      status: "Active",
    },
    {
      id: "load-balancer-3",
      name: "Load Balancer 3",
      rule: "Round robin",
      status: "Disabled",
    },
  ];
  const headers = ["Use", "Sentence", "Source", "Tags"];
</script>

<div>
  <Row>
    <Column>
      <ButtonSet>
        <Search placeholder="Enter a phrase..." />
        <Button>Search</Button>
      </ButtonSet>
    </Column>
    <Column>
      <MultiSelect
        size="xl"
        label="Sentence Sources"
        items={[{ id: '0', text: 'Slack' }, { id: '1', text: 'Email' }, { id: '2', text: 'Fax' }]}
        selectedIds={['0', '1']} />
    </Column>
  </Row>
  <Row>
    <Column>
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
            {#each rows as _}
              <TableRow on:click={() => console.log('nice')}>
                <TableCell>
                  <Checkbox />
                </TableCell>
                <TableCell>
                  <Column noGutterLeft>
                    <p class="border-gray-400">
                      I could not persuade him that it was true.
                    </p>
                    <p>
                      それが本当だと彼に<b>納得</b>させることができなかった。
                    </p>
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
      <Pagination />
    </Column>
  </Row>
  <Row>
    <Column>
      <ButtonSet>
        <DeckSelect />
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
</div>
