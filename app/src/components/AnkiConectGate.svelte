<script lang="ts">
  import { getContext, onMount } from "svelte";
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

  let promise: Promise<AnkiConnectResponse>;
  const anki = getContext<IAnkiConnect>("anki");

  onMount(() => {
    promise = anki.version();
  });
</script>

<div>
  <slot />
</div>
