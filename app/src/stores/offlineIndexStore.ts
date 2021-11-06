import { derived } from 'svelte/store';
import type { SentenceSource } from './sentenceSourcesStore';
import { SentenceSourceStore } from './sentenceSourcesStore';
import { Document } from 'flexsearch';
import { getTokenizedSentences } from '../services/anki';
import type { KyoTokenResult } from 'src/models/SolrResponse';

function createIndex(data?: KyoTokenResult[]) {
  const index = new Document({
    index: ['Words', 'Lemmas', 'Readings'],
    store: ['Sentence', 'Words', 'Lemmas', 'WordPositions', 'Source', 'Translation', 'Readings'],
    worker: true,
  });
  data?.forEach((doc, i) => index.add({ id: i, ...doc }));
  return index;
}

async function getNewIndexAsync(values: SentenceSource[]) {
  console.log('Running', values.length);
  const tokenPromos = values.flatMap((value) => getTokenizedSentences(value.name));
  const result = await Promise.all(tokenPromos);
  console.log('All promises');
  console.log('sort start');
  const sorted = result.flat();
  console.log('sort end');
  return sorted;
}

export const OfflineIndexStore = derived<typeof SentenceSourceStore, KyoTokenResult[]>(
  SentenceSourceStore,
  ($values, set) => {
    getNewIndexAsync($values).then(set);
  },
);

let indexData: KyoTokenResult[] = [];
export let OfflineIndex = createIndex();

OfflineIndexStore.subscribe((newIndex) => {
  indexData = newIndex;
  console.log('index start');
  OfflineIndex = createIndex(newIndex);
  console.log('index end');
});
