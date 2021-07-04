declare module FlexSearch {
  export interface Result {
    id: number;
    doc: Solr.Doc;
  }

  export interface RootObject {
    field: string;
    result: Result[];
  }
}
