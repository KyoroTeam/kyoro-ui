<script lang="ts">
  import { getContext } from "svelte";
  import {
    Column,
    Loading,
    Row,
    ToastNotification,
  } from "carbon-components-svelte";
  import type {
    AnkiConnectResponse,
    IAnkiConnect,
  } from "../services/ankiconect";
  const anki = getContext<IAnkiConnect>("anki");
  const promise = anki.version();
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
        hideCloseButton
        title="Couldn't connect to AnkiConnect"
        subtitle="Did something go wrong?"
        caption="Try making sure AnkiConnect is running, and you have read the setup instructions."
      />
    </Row>
    <Row />
  {/await}
</div>
