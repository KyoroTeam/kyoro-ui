<script lang="ts">
  import { ToolbarSearch } from 'carbon-components-svelte';
  import MiniSearch, { type SearchResult } from 'minisearch';
  import type { Options } from 'minisearch';
  import {
    getMinisearchJsonIndex,
    type KyTokenResult,
    type KyWordPosition,
  } from '../../services/anki';
  import { onMount } from 'svelte';

  export let onSearchResults: (result: KySearchResult[]) => void;
  export let maxResults: number = 100;

  interface KySentenceChunk {
    str: string;
    highlight: boolean;
  }

  interface KySearchResult {
    sentence: string;
    source: string;
    sentenceChunks: KySentenceChunk[];
  }

  type MiniKyTokenResult = Omit<KyTokenResult, 'Readings' | 'Translation'>;

  const indexOptions: Options<MiniKyTokenResult> = {
    fields: ['Lemmas', 'Words'],
    storeFields: ['Sentence', 'Lemmas', 'Words', 'WordPositions', 'Source'],
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

  function findAllIndiciesOfString(string: string, search: string): number[] {
    const incidies: number[] = [];
    let startIndex = 0;
    while (true) {
      const newIndex = string.indexOf(search, startIndex);
      if (newIndex === -1) {
        break;
      }
      startIndex = newIndex + search.length;
      incidies.push(newIndex);
    }
    return incidies;
  }

  function get0BasedWordPositionForTerms(term: string, result: SearchResult) {
    const matchLocation = result.match[term][0];
    const searchString = result[matchLocation];

    const termLocations = findAllIndiciesOfString(searchString, term);
    const spaceLocations = findAllIndiciesOfString(searchString, ' ');

    const wordIndicies = termLocations.map(
      (termIdx) => spaceLocations.filter((spaceIdx) => spaceIdx < termIdx).length,
    );

    return wordIndicies;
  }

  function getSentenceChunks(sentence: string, wordPositions: KyWordPosition[]): KySentenceChunk[] {
    const results: KySentenceChunk[] = [];
    let startIndex = 0;
    for (const position of wordPositions) {
      const preStringSlice = sentence.substring(startIndex, position.Start);
      const termSlice = sentence.substring(position.Start, position.End);
      results.push({ str: preStringSlice, highlight: false });
      results.push({ str: termSlice, highlight: true });
      startIndex = position.End;
    }
    const lastStringSlice = sentence.substring(wordPositions[wordPositions.length - 1].End);
    results.push({ str: lastStringSlice, highlight: false });
    return results;
  }

  function convertSearchResult(term: string, result: SearchResult): KySearchResult {
    const wordIndicies = get0BasedWordPositionForTerms(term, result);
    const wordPositionArray: KyWordPosition[] = result['WordPositions'];
    const wordPositions = wordIndicies.map((index) => wordPositionArray[index]);
    const sentence: string = result['Sentence'];
    const chunks = getSentenceChunks(sentence, wordPositions);
    return {
      sentence: sentence,
      source: result['Source'],
      sentenceChunks: chunks,
    };
  }

  function onSearchChanged(event: any) {
    const boxContent: string = event.target.value;
    console.log(boxContent);
    if (miniSearch) {
      const results = miniSearch.search(boxContent).slice(0, maxResults);
      const kyResult = results.map((r) => convertSearchResult(boxContent, r));
      onSearchResults(kyResult);
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
