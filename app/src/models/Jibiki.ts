export interface Translation {
  id: number;
  language: string;
  sentence: string;
}

export type SentecePart = { part: string; highlight: boolean };

export interface JibikiSenteceResponse {
  id: number;
  language: string;
  sentence: string;
  sentenceParts: SentecePart[];
  tags: string[];
  translations: Translation[];
}
