import { getLocalContentList } from '../services/anki';
import { readable } from 'svelte/store';

export type SentenceSource = {
  name: string;
  offline: boolean;
};

export const SentenceSourceStore = readable<SentenceSource[]>([], set => {
  getLocalContentList().then(sources => {
    const onlineNames = ['my-name-1'];
    const onlineSources = onlineNames.map(name => ({
      name: name,
      offline: false,
    }));
    const offlineSources = sources.map(name => ({
      name: name,
      offline: true,
    }));
    set([...onlineSources, ...offlineSources]);
  });
});
