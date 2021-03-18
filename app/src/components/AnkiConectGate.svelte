<script lang="ts">
  import { getContext } from "svelte";
  import {
    Column,
    Loading,
    Row,
    ToastNotification,
  } from "carbon-components-svelte";
  import type { IAnkiConnect } from "../services/ankiconect";
  import Retrier from "./Retrier.svelte";
  const anki = getContext<IAnkiConnect>("anki");
  let promise = anki.version();
</script>

<div>
  {#await promise}
    <Row>
      <Column>
        <p>Connecting to AnkiConnect...</p>
      </Column>
    </Row>
  {:then _}
    <slot />
  {:catch _}
    <Column>
      <ToastNotification
        kind="error"
        hideCloseButton
        title="Couldn't connect to AnkiConnect"
        subtitle="Did something go wrong?"
        caption="Try making sure AnkiConnect is running, and you have read the setup instructions."
      />
      <Row>
        <Retrier
          retryTime={1000}
          maxCounts={5}
          onTimeoutEnded={anki.version}
          let:timeUntilNextTry={time}
          let:loading
        >
          <p>> Retrying in ({time}) ...</p>
          {#if loading}
            <Loading small withOverlay={false} />
          {/if}
        </Retrier>
      </Row>
    </Column>
    <Row />
  {/await}
</div>
