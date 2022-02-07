<script lang="ts">
  import { ToolbarSearch } from 'carbon-components-svelte';
  import MiniSearch from 'minisearch';
  import type { Options } from 'minisearch';
  import type { KyTokenResult } from 'src/services/anki';

  type MiniKyTokenResult = Omit<KyTokenResult, 'Readings' | 'Translation'>;

  const indexOptions: Options<MiniKyTokenResult> = {
    fields: ['Lemmas', 'Words'],
    storeFields: ['Sentence', 'WordPositions', 'Source'],
    extractField: (document, fieldName) => {
      const kyFieldName = fieldName as keyof MiniKyTokenResult;
      if (kyFieldName === 'Words') {
        return document.Words.join(' ');
      } else if (kyFieldName === 'Lemmas') {
        return document.Lemmas.join(' ');
      }
      return MiniSearch.getDefault('extractField')(document, fieldName);
    },
  };

  function onSearchChanged(event: any) {
    console.log(event.target?.value);
  }
</script>

<ToolbarSearch persistent on:input={onSearchChanged} />
