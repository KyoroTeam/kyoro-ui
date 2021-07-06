import { Docs } from "./SenteceData";

export function getLocalContentList(): Promise<string[]> {
  return new Promise((resolve) => {
    const sources = Docs.map((d) => d.Source);
    const uniqueSources = new Set(sources);
    resolve(Array.from(uniqueSources.values()));
    // pycmd<string[]>("getLocalContentList", (files) => resolve(files));
  });
}

export function getTokenizedSentences(
  source: string
): Promise<Solr.KyoTokenResult[]> {
  return new Promise((resolve) => {
    const sources = Docs.filter((d) => d.Source === source);
    resolve(sources);
    // pycmd<string[]>("getLocalContentList", (files) => resolve(files));
  });
}
