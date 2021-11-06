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
  import AnkiConectGate from './components/AnkiConectGate.svelte';

  import AnkiConnectProvider from './services/AnkiConnectProvider.svelte';
  import NewSentencesTab from './components/new-sentences-app/NewSentencesTab.svelte';
  import { SentenceSourceStore } from './stores/sentenceSourcesStore';

  let isSideNavOpen = false;

  let offlineSources: string[] = [];
  SentenceSourceStore.subscribe(
    (items) => (offlineSources = items.filter((i) => i.offline === true).map((s) => s.name)),
  );
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
    <SideNavMenu expanded text="Sentence Sources">
      {#each offlineSources as source}
        <SideNavMenuItem href="/" text={source} />
      {/each}
    </SideNavMenu>
  </SideNavItems>
</SideNav>

<Content>
  <AnkiConnectProvider>
    <AnkiConectGate>
      <NewSentencesTab />
    </AnkiConectGate>
  </AnkiConnectProvider>
</Content>
