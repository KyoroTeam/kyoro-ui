<script lang="ts">
  import {
    Content,
    Grid,
    Row,
    Column,
    Tabs,
    TabContent,
    Header,
    Tab,
    SideNav,
    SideNavItems,
    SideNavLink,
    HeaderNav,
    HeaderNavItem,
    HeaderNavMenu,
    SideNavDivider,
  } from "carbon-components-svelte";
  import AnkiConectGate from "./components/AnkiConectGate.svelte";

  import AnkiConnectProvider from "./services/AnkiConnectProvider.svelte";
  import MappingsCreator from "./components/MappingsCreator.svelte";
  import SeachTab from "./components/SeachTab.svelte";

  let isSideNavOpen = false;
</script>

<Header company="Kyoro" platformName="Anki UI" bind:isSideNavOpen>
  <HeaderNav>
    <HeaderNavItem href="/" text="Start" />
    <HeaderNavItem href="/" text="Account" />
    <HeaderNavItem href="/" text="Local Storage" />
    <HeaderNavMenu text="About">
      <HeaderNavItem href="/" text="Kyoro" />
      <HeaderNavItem href="/" text="Kyoro Team" />
    </HeaderNavMenu>
  </HeaderNav>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavLink text="New Cards" />
    <SideNavLink text="Modify Cards" />
    <SideNavDivider />
    <SideNavLink text="Sentence Sources" />
  </SideNavItems>
</SideNav>

<Content>
  <Grid>
    <Row>
      <Column>
        <AnkiConnectProvider>
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
        </AnkiConnectProvider>
      </Column>
    </Row>
  </Grid>
</Content>
