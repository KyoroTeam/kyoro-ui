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
