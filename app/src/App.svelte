<script lang="ts">
  import {
    Content,
    Grid,
    Row,
    Column,
    Tabs,
    TabContent,
    Tab,
  } from "carbon-components-svelte";
  import AnkiConectGate from "./components/AnkiConectGate.svelte";
  import Header from "./components/Header.svelte";
  import Theme from "./components/Theme.svelte";

  import AnkiConnectProvider from "./services/AnkiConnectProvider.svelte";
  import MappingsCreator from "./components/MappingsCreator.svelte";
  import SeachTab from "./components/SeachTab.svelte";
  let theme: "g10" = "g10";
</script>

<Theme bind:theme>
  <Header />
  <AnkiConnectProvider>
    <Content>
      <AnkiConectGate>
        <Grid>
          <Row>
            <Column noGutter>
              <Tabs aria-label="Tab navigation">
                <Tab label="Search" />
                <Tab label="Sources" />
                <Tab label="Settings" />
                <div slot="content" class="tabbed-content">
                  <Grid as fullWidth>
                    <TabContent>
                      Hello
                      <SeachTab />
                    </TabContent>
                    <TabContent>
                      <Row />
                    </TabContent>
                    <TabContent>
                      <MappingsCreator />
                    </TabContent>
                  </Grid>
                </div>
              </Tabs>
            </Column>
          </Row>
        </Grid>
      </AnkiConectGate>
    </Content>
  </AnkiConnectProvider>
</Theme>
