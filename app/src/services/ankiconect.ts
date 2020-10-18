export interface IAnkiConnect {
  version: () => Promise<AnkiConnectResponse>;
  getNumCardsReviewedToday: () => Promise<AnkiConnectResponse>;
  deckNames: () => Promise<string[]>;
  modelNames: () => Promise<string[]>;
  modelFieldNames: (modelName: string) => Promise<string[]>;
}

export class AnkiConnect implements IAnkiConnect {
  private http: { fetch(url: RequestInfo, init?: RequestInit): Promise<Response> };
  private baseUrl: string;

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

  deckNames() {
    return Promise.resolve(["A", "B", "C"]);
  }

  modelNames() {
    return Promise.resolve(["A", "VCD", "C"]);
  }

  modelFieldNames(modelName: string) {
    return  Promise.resolve([modelName, "Front", "Back", "Other"]);
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
