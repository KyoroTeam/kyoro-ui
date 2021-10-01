<script lang="ts">
  import { Button } from 'carbon-components-svelte';
  import ChevronRight32 from 'carbon-icons-svelte/lib/ChevronRight16';
  import AnkiAddModal from './AnkiAddModal.svelte';

  let menuOpen: boolean = false;
</script>

<Button on:click={() => (menuOpen = true)} icon={ChevronRight32}>Add Selected To Anki</Button>

<AnkiAddModal
  open={menuOpen}
  onSubmitted={() => {
    menuOpen = false;
  }}
/>
