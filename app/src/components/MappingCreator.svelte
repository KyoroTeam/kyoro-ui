<script lang="ts">
  import { Button, ButtonSet, Column, Row, TextArea, Tile } from 'carbon-components-svelte';
  import ModelFieldSelect from './ModelFieldSelect.svelte';
  import ModelSelect from './ModelSelect.svelte';

  let modelSelecton: string;
</script>

<Tile>
  <Row>New Model Mapping</Row>
  <Row>
    <ModelSelect bind:selected={modelSelecton} />
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
      <TextArea />
    </Column>
  </Row>
  <Row>
    <Column />
    <Column>
      <ButtonSet>
        <Button>Cancel</Button>
        <Button>Save</Button>
      </ButtonSet>
    </Column>
  </Row>
</Tile>
