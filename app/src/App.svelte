<script lang="ts">
  import {
    Content,
    Header,
    SideNav,
    SideNavItems,
    SideNavLink,
    HeaderNav,
    HeaderNavItem,
    HeaderNavMenu,
    SideNavDivider,
    SideNavMenu,
    SideNavMenuItem,
  } from 'carbon-components-svelte';
  import Checkmark16 from 'carbon-icons-svelte/lib/Checkmark16';
  import RecentlyViewed16 from 'carbon-icons-svelte/lib/RecentlyViewed16';
  import NewTab16 from 'carbon-icons-svelte/lib/NewTab16';
  import WarningAlt16 from 'carbon-icons-svelte/lib/WarningAlt16';
  import Error16 from 'carbon-icons-svelte/lib/Error16';

  import NewSentencesTab from './components/new-sentences-app/NewSentencesTab.svelte';
  import { getCurrentIndexState } from './services/anki';

  const indexIconStyles = 'vertical-align: text-bottom; margin-right: 3px';

  let indexState = getCurrentIndexState();
  let isSideNavOpen = false;
</script>

<Header company="Kyoro" platformName="Anki UI" bind:isSideNavOpen>
  <HeaderNav>
    <HeaderNavItem href="/" text="Start" />
    <HeaderNavItem href="/" text="Local Storage" />
    <HeaderNavMenu text="About">
      <HeaderNavItem href="/" text="Kyoro" />
      <HeaderNavItem href="/" text="Kyoro Team" />
    </HeaderNavMenu>
  </HeaderNav>
</Header>

<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavLink isSelected text="New Cards" />
    <SideNavLink text="Modify Cards" />
    <SideNavDivider />
    <SideNavMenu expanded text="Content Folder">
      {#await indexState}
        <p>Wait...</p>
      {:then sources}
        {#each sources as source}
          <SideNavMenuItem>
            <span>
              {#if source.index_state == 'fully-indexed'}
                <Checkmark16 title="Up to Date" style={`color: green; ${indexIconStyles}`} />
              {:else if source.index_state == 'needs-reindex'}
                <RecentlyViewed16 title="Needs Re-Index" style={indexIconStyles} />
              {:else if source.index_state == 'not-indexed'}
                <NewTab16 title="New Unindexed Content" style={`color: blue; ${indexIconStyles}`} />
              {:else}
                <Error16 style={indexIconStyles} />
              {/if}
              {source.name}
            </span>
          </SideNavMenuItem>
        {/each}
      {:catch error}
        <SideNavMenuItem>
          <span>
            <WarningAlt16 title={error} style={`color: red; ${indexIconStyles}`} /> Failed to load content list
          </span>
        </SideNavMenuItem>
      {/await}
    </SideNavMenu>
  </SideNavItems>
</SideNav>

<Content>
  <NewSentencesTab />
</Content>
