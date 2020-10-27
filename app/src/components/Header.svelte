<script lang="ts">
  import {
    SkipToContent,
    Header,
    HeaderUtilities,
  } from "carbon-components-svelte";
  import { getContext } from "svelte";

  const ctx: { dark: any; light: any; updateVar: any } = getContext("Theme");

  $: if (ctx) {
    ctx.dark.subscribe((value: any) => {
      console.log("dark mode?", value);
    });
    ctx.light.subscribe((value: any) => {
      console.log("light mode?", value);
    });
    ctx.updateVar("--cds-productive-heading-06-font-size", "4rem");
  }
</script>

<Header company="Kyoro" platformName="Carbon Components Svelte" href="/">
  <div slot="skip-to-content">
    <SkipToContent />
  </div>
  <HeaderUtilities />
</Header>
