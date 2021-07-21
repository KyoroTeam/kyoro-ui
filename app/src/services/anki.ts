// import { SentenceData } from './all_v11_out';

export function getLocalContentList(): Promise<string[]> {
  return new Promise(resolve => {
    if (window.pycmd !== undefined) {
      window.pycmd<string[]>('Kyoro.getLocalContentList', files => resolve(files));
    } else {
      fetch('http://localhost:8006/getLocalContentList')
        .then(r => r.json())
        .then(json => resolve(json));
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
      fetch(`http://localhost:8006/getTokenizedSentences/${encodeURIComponent(source)}`)
        .then(r => r.json())
        .then(json => resolve(json));
    }
  });
}
