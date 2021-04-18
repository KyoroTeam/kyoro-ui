<script lang="ts">
  import { Row, Tabs, TabContent, Tab } from "carbon-components-svelte";
  import MappingsCreator from "./MappingsCreator.svelte";
  import SeachTab from "./SeachTab.svelte";
</script>

<Tabs aria-label="Tab navigation">
  <Tab label="Search" />
  <Tab label="Sources" />
  <Tab label="Settings" />
  <div slot="content" class="tabbed-content">
    <TabContent>
      <SeachTab />
    </TabContent>
    <TabContent>
      <Row />
    </TabContent>
    <TabContent>
      <MappingsCreator />
    </TabContent>
  </div>
</Tabs>
