declare module FlexSearch {
  export interface Result {
    id: number;
    doc: Solr.KyoTokenResult;
  }

  export interface RootObject {
    field: string;
    result: Result[];
  }
}
