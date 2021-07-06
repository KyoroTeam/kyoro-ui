import { getLocalContentList } from "../services/anki";
import { readable } from "svelte/store";

export type SentenceSource = {
  name: string;
  offline: boolean;
};

export const SentenceSourceStore = readable<SentenceSource[]>([], (set) => {
  const interval = setInterval(() => {
    getLocalContentList().then((sources) => {
      const onlineNames = [
        "jlpt-tango",
        "tofugu",
        "tatoeba",
        "satori_reader",
        "ninjal",
        "lingodeer",
        "jpod101_word-list",
        "jpod101_lessons-examples",
        "jap_online_br",
        "iknow_words",
        "humanJapanese",
        "glossika",
        "bunpro",
        "ankiGenki",
        "anki5k",
        "anki10k",
      ];
      const onlineSources = onlineNames.map((name) => ({
        name: name,
        offline: false,
      }));
      getLocalContentList().then((contentList) => {
        const offlineSources = contentList.map((c) => ({
          name: c,
          offline: true,
        }));
        set([...onlineSources, ...offlineSources]);
      });
    });
  }, 1000);

  return () => clearInterval(interval);
});
