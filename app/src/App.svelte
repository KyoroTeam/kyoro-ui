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
  } from 'carbon-components-svelte';

  import NewSentencesTab from './components/new-sentences-app/NewSentencesTab.svelte';

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
    <SideNavMenu expanded text="Sentence Sources" />
  </SideNavItems>
</SideNav>

<Content>
  <NewSentencesTab />
</Content>
