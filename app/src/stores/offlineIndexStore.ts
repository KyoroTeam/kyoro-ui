import { derived } from 'svelte/store';
import type { SentenceSource } from './sentenceSourcesStore';
import { SentenceSourceStore } from './sentenceSourcesStore';
import { Document } from 'flexsearch';
import { getTokenizedSentences } from '../services/anki';
import greenlet from 'greenlet';

function createIndex(data?: Solr.KyoTokenResult[]) {
  const index = new Document({
    index: ['Words', 'Lemmas', 'Readings'],
    store: ['Sentence', 'Words', 'Lemmas', 'WordPositions', 'Source'],
    worker: true,
  });
  data?.forEach((doc, i) => index.add({ id: i, ...doc }));
  return index;
}

async function getNewIndexAsync(values: SentenceSource[]) {
  console.log('Running', values.length);
  const tokenPromos = values.flatMap(value => getTokenizedSentences(value.name));
  const result = await Promise.all(tokenPromos);
  console.log('All promises');
  console.log('sort start');
  const sorted = result.flat();
  console.log('sort end');
  return sorted;
}

const getNewIndexAsyncGreen = greenlet(getNewIndexAsync);

export const OfflineIndexStore = derived<typeof SentenceSourceStore, Solr.KyoTokenResult[]>(
  SentenceSourceStore,
  ($values, set) => {
    getNewIndexAsync($values).then(set);
  },
);

let indexData: Solr.KyoTokenResult[] = [];
export let OfflineIndex = createIndex();

OfflineIndexStore.subscribe(newIndex => {
  indexData = newIndex;
  console.log('index start');
  OfflineIndex = createIndex(newIndex);
  console.log('index end');
});
