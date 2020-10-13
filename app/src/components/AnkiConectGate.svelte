<script lang="ts">
  import { getContext, onMount } from 'svelte';
  import { Column, Loading, Row, ToastNotification } from 'carbon-components-svelte';
  import type { AnkiConnectResponse, IAnkiConnect } from '../services/ankiconect';

  let promise: Promise<AnkiConnectResponse>;
  const anki = getContext<IAnkiConnect>('anki');

  onMount(() => {
    promise = anki.version();
  });
</script>

<div>
  {#await promise}
    <Row>
      <Column>
        <Loading />
      </Column>
      <Column>
        <p>Connecting to AnkiConnect...</p>
      </Column>
    </Row>
  {:then _}
    <slot />
  {:catch _}
    <Row>
      <ToastNotification
        kind="error"
        timeout={2000}
        hideCloseButton
        title="Couldn't connect to AnkiConnect"
        subtitle="Did something go wrong?" />
    </Row>
    <Row />
  {/await}
</div>
