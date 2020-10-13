export interface IAnkiConnect {
  version: () => Promise<AnkiConnectResponse>;
  getNumCardsReviewedToday: () => Promise<AnkiConnectResponse>;
}

export class AnkiConnect implements IAnkiConnect {
  private http: { fetch(url: RequestInfo, init?: RequestInit): Promise<Response> };
  private baseUrl: string;
  protected jsonParseReviver: ((key: string, value: any) => any) | undefined = undefined;

  constructor(baseUrl?: string, http?: { fetch(url: RequestInfo, init?: RequestInit): Promise<Response> }) {
    this.http = http ? http : <any>window;
    this.baseUrl = baseUrl ? baseUrl : '';
  }

  version() {
    return Promise.resolve<AnkiConnectResponse>({ result: 5, error: null });
  }

  getNumCardsReviewedToday() {
    return Promise.resolve<AnkiConnectResponse>({ result: 5, error: null });
  }
}

export interface AnkiConnectRequest {
  action: string;
  version: number;
  params: object;
  key?: number;
}

export interface AnkiConnectResponse {
  result: any;
  error: string | null;
}
