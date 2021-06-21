declare module Solr {
  export interface Params {
    q: string;
  }

  export interface ResponseHeader {
    status: number;
    QTime: number;
    params: Params;
  }

  export interface Doc {
    Words: string[];
    Lemmas: string[];
    Readings: string[];
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
}
