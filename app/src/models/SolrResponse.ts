export interface Params {
  q: string;
}

export interface ResponseHeader {
  status: number;
  QTime: number;
  params: Params;
}

export interface KyoTokenResult {
  Source: string;
  Sentence: string;
  Translation?: string;
  Words: string[];
  WordPositions: { Start: number; End: number }[];
  Lemmas: string[];
  Readings: string[];
}

export interface Doc extends KyoTokenResult {
  id: string;
  _version_: any;
}

export interface Response {
  numFound: number;
  start: number;
  numFoundExact: boolean;
  docs: Doc[];
}

export interface SolrSearchResponse {
  responseHeader: ResponseHeader;
  response: Response;
}
