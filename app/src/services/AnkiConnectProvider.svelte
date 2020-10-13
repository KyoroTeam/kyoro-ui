<script lang="ts">
  import { setContext } from 'svelte';
  import { AnkiConnect, IAnkiConnect } from './ankiconnect';

  setContext<IAnkiConnect>('', {
    ankiConnect: () => new AnkiConnect(),
  });
</script>
