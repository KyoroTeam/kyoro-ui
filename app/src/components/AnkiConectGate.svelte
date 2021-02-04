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
  const promise: Promise<AnkiConnectResponse> = anki.version();
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
        subtitle="Did something go wrong?"
      />
    </Row>
    <Row />
  {/await}
</div>
