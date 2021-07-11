import { SentenceData } from './all_v11_out';

export function getLocalContentList(): Promise<string[]> {
  return new Promise(resolve => {
    if (window.pycmd !== undefined) {
      window.pycmd<string[]>('Kyoro.getLocalContentList', files => resolve(files));
    } else {
      const sources = SentenceData.map(d => d.Source);
      const uniqueSources = new Set(sources);
      resolve(Array.from(uniqueSources.values()));
    }
  });
}

export function getTokenizedSentences(source: string): Promise<Solr.KyoTokenResult[]> {
  return new Promise(resolve => {
    if (window.pycmd !== undefined) {
      window.pycmd<Solr.KyoTokenResult[]>(`Kyoro.getLocalContentList:${source}`, sentences =>
        resolve(sentences),
      );
    } else {
      const sources = SentenceData.filter(d => d.Source === source);
      resolve(sources);
    }
  });
}
