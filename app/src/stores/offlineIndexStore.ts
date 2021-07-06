import { derived } from "svelte/store";
import { SentenceSourceStore } from "./sentenceSourcesStore";
import { Document } from "flexsearch";
import { getTokenizedSentences } from "src/services/anki";

const initialindex = new Document({
  document: {
    index: ["Words", "Lemmas", "Readings"],
    store: ["Sentence", "Words", "Lemmas", "WordPositions"],
  },
});

export const OfflineIndexStore = derived<
  typeof SentenceSourceStore,
  Solr.KyoTokenResult[]
>(SentenceSourceStore, ($values, set) => {
  const tokenPromos = $values.flatMap((value) =>
    getTokenizedSentences(value.name)
  );
  Promise.all(tokenPromos).then((tokenResults) => set(tokenResults.flat()));
});
