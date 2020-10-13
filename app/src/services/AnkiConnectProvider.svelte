<script lang="ts">
  import { setContext } from 'svelte';
  import { AnkiConnect, IAnkiConnect } from './ankiconect';
  setContext<IAnkiConnect>('anki', new AnkiConnect());
</script>

<slot/>
