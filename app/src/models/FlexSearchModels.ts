import type { KyoTokenResult } from './SolrResponse';

export interface Result {
  id: number;
  doc: KyoTokenResult;
}

export interface RootObject {
  field: string;
  result: Result[];
}
