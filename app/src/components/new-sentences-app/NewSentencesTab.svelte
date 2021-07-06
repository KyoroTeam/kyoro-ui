<script lang="ts">
  import { Tabs, TabContent, Tab } from 'carbon-components-svelte';
  import MappingsCreator from './MappingsCreator.svelte';
  import SeachTab from './SeachTab.svelte';
</script>

<Tabs aria-label="Tab navigation">
  <Tab label="Search" />
  <Tab label="Field Mappings" />
  <div slot="content" class="tabbed-content">
    <TabContent>
      <SeachTab />
    </TabContent>
    <TabContent>
      <MappingsCreator />
    </TabContent>
  </div>
</Tabs>
