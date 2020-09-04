<script lang="ts">
  import "smelte/src/tailwind.css";
  export let name: string;
  let ankiConnectText: string;

  async function onClick() {
    name = "Shion";
    const response = await fetch("http://localhost:8765", {
      mode: "cors",
      cache: "no-cache",
    });
    ankiConnectText = await response.text();
  }
</script>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

<p>AnkiConnect: {ankiConnectText}</p>

<main class="md:flex shadow-lg md:text-xs">
  <h1 class="shadow-md">Hello {name}!</h1>
  <button on:click={onClick}>Button Text</button>
  <p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>
