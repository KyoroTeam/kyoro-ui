<script lang="ts">
  import {
    Button,
    ButtonSet,
    Column,
    Row,
    TextArea,
    TextInput,
    Tile,
  } from "carbon-components-svelte";
  import ModelFieldSelect from "./ModelFieldSelect.svelte";
  import ModelSelect from "./ModelSelect.svelte";

  let modelSelecton: string;
</script>

<Column md={2}>
  <Row>New Model Mapping</Row>
  <Row>
    <!-- <ModelSelect bind:selected={modelSelecton} /> -->
  </Row>
  <Row>
    <Column>English</Column>
    <Column>
      <ModelFieldSelect modelName={modelSelecton} />
    </Column>
  </Row>
  <Row>
    <Column>Japanese</Column>
    <Column>
      <ModelFieldSelect modelName={modelSelecton} />
    </Column>
  </Row>
  <Row>
    <Column>Tags</Column>
    <Column>
      <ModelFieldSelect modelName={modelSelecton} />
    </Column>
  </Row>
  <Row>
    <Column />
    <Column>
      Mapping Name
      <TextInput />
    </Column>
  </Row>
  <Row>
    <ButtonSet>
      <Button>Cancel</Button>
      <Button>Save</Button>
    </ButtonSet>
  </Row>
</Column>
