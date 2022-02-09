<script lang="ts">
  import { ToolbarSearch } from 'carbon-components-svelte';
  import MiniSearch from 'minisearch';
  import type { Options } from 'minisearch';
  import { getMinisearchJsonIndex, type KyTokenResult } from '../../services/anki';
  import { onMount } from 'svelte';

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
    const boxContent: string = event.target.value;
    console.log(boxContent);
    if (miniSearch) {
      const results = miniSearch.search(boxContent);
      console.log(results);
    }
  }

  let miniSearch: MiniSearch<MiniKyTokenResult>;

  onMount(() => {
    getMinisearchJsonIndex().then((index) => {
      miniSearch = MiniSearch.loadJSON(index, indexOptions);
    });
  });
</script>

<ToolbarSearch persistent on:input={onSearchChanged} />
