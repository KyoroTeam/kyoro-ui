<script lang="ts">
  import "smelte/src/tailwind.css";
  import Button from "smelte/src/components/Button";
  import Image from "smelte/src/components/Image";
  import List from "smelte/src/components/List";
  import Icon from "smelte/src/components/Icon";
  import DataTable from "smelte/src/components/DataTable";
  import { Card } from "smelte/src";

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

  const listOneLine = [
    {
      text: "Item 1",
      icon: "favorite",
    },
    {
      text: "Item 2",
      icon: "favorite",
    },
    {
      text: "Item 3",
      icon: "favorite",
    },
  ];
</script>

<p>AnkiConnect: {ankiConnectText}</p>

<main class="md:flex shadow-lg text-left md:border">
  <Card.Card class="m-5">
    <div slot="title">
      <Card.Title title="The three little kittens" subheader="A kitten poem" avatar="https://placekitten.com/64/64" />
    </div>
    <div slot="media">
      <Image class="w-full" src="https://placekitten.com/300/200" alt="kitty" />
    </div>
    <div slot="text" class="p-5 pb-0 pt-3 text-gray-700 body-2">
      The three little kittens, they lost their mittens,
      <br />
      And they began to cry,
      <br />
      "Oh, mother dear, we sadly fear,
      <br />
      That we have lost our mittens."
    </div>
    <div slot="actions">
      <div class="p-4">
        <Button color={'success'}>OK</Button>
        <Button text>Meow</Button>
      </div>
    </div>
  </Card.Card>
  <h1 class="shadow-md text-orange-700">Hello {name}!</h1>
  <div class="p-4">
    <Button on:click={onClick}>Button Text</Button>
  </div>
  <p class="text-blue-500">
    Visit the
    <a href="https://svelte.dev/tutorial">Svelte tutorial</a>
    to learn how to build Svelte apps.
  </p>

</main>
<h6 class="mb-3 mt-6">One-line</h6>
<List items={listOneLine} />
