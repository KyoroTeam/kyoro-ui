<script lang="ts">
  type Theme = 'white' | 'g10' | 'g90' | 'g100';

  export let theme: Theme = 'white';
  export const themes: Theme[] = ['white', 'g10', 'g90', 'g100'];

  import { onMount, afterUpdate, setContext } from 'svelte';
  import { writable, derived } from 'svelte/store';

  const isValidTheme = value => themes.includes(value);
  const isDark = value => isValidTheme(value) && (value === 'g90' || value === 'g100');

  const dark = writable(isDark(theme));
  const light = derived(dark, _ => !_);

  setContext('Theme', {
    updateVar: (name: string, value: string) => {
      document.documentElement.style.setProperty(name, value);
    },
    dark,
    light,
  });

  onMount(() => {
    // TODO: Load from somewhere
    theme = 'g10';
  });

  afterUpdate(() => {
    if (isValidTheme(theme)) {
      document.documentElement.setAttribute('theme', theme);
    } else {
      console.warn(`"${theme}" is not a valid Carbon theme. Choose from available themes: ${JSON.stringify(themes)}`);
    }
  });

  $: dark.set(isDark(theme));
</script>

<slot />
