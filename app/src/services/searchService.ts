export interface Translation {
  id: number;
  language: string;
  sentence: string;
}

export interface JibikiSenteceResponse {
  id: number;
  language: string;
  sentence: string;
  tags: string[];
  translations: Translation[];
}

export interface ISentenceSource {
  name: string;
  searchSentences: (keyword: string) => Promise<JibikiSenteceResponse[]>;
}

export function searchSentences(keyword: string, sources: ISentenceSource[]) {}
