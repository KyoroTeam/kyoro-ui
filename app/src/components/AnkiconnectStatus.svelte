<script lang="ts">
  import { onMount } from 'svelte';
  import { ToastNotification } from 'carbon-components-svelte';

  let promise: Promise<Response>;
  async function checkStatus() {
    promise = fetch('http://localhost:8679');
  }

  onMount(() => {
    checkStatus();
  });
</script>

<div>
  {#await promise then _}
    <div>OK</div>
  {:catch _}
    <ToastNotification
      kind="error"
      timeout={2000}
      hideCloseButton
      title="Couldn't connect to AnkiConnect"
      subtitle="Did something go wrong?" />
  {/await}
</div>
