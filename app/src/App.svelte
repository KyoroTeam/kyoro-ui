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

  import NewSentencesTab from './components/new-sentences-app/NewSentencesTab.svelte';
  import { getIndexedSources, getOnDiskSources, getTokenizedSentences } from './services/anki';

  let indexedSources = getIndexedSources();
  let localSources = getOnDiskSources();

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
    <SideNavLink isSelected text="New Cards" />
    <SideNavLink text="Modify Cards" />
    <SideNavDivider />
    <SideNavMenu expanded text="Indexed Sources">
      {#await indexedSources}
        <p>Wait...</p>
      {:then sources}
        {#each sources as source}
          <SideNavMenuItem
            on:click={() => {
              getTokenizedSentences(source[1]).then(console.log);
            }}>{source[0]}</SideNavMenuItem
          >
        {/each}
      {/await}
    </SideNavMenu>
    <SideNavMenu expanded text="Local Sources">
      {#await localSources}
        <p>Wait...</p>
      {:then sources}
        {#each sources as source}
          <SideNavMenuItem>{source.name}</SideNavMenuItem>
        {/each}
      {/await}
    </SideNavMenu>
  </SideNavItems>
</SideNav>

<Content>
  <NewSentencesTab />
</Content>
