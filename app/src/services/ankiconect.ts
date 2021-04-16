import type { KyoroFieldName } from "src/stores/settingsStore";

export interface IAnkiConnect {
  version: () => Promise<number>;
  getNumCardsReviewedToday: () => Promise<AnkiConnectResponse>;
  deckNames: () => Promise<string[]>;
  modelNames: () => Promise<string[]>;
  modelFieldNames: (modelName: string) => Promise<string[]>;
  addNote: (
    deckName: string,
    modelName: string,
    resolvedValues: Record<string, string>
  ) => Promise<AnkiConnectResponse>;
}

export class AnkiConnect implements IAnkiConnect {
  private http: {
    fetch(url: RequestInfo, init?: RequestInit): Promise<Response>;
  };
  private baseUrl: string;

  constructor(
    baseUrl?: string,
    http?: { fetch(url: RequestInfo, init?: RequestInit): Promise<Response> }
  ) {
    this.http = http ? http : <any>window;
    this.baseUrl = baseUrl ? baseUrl : "";
  }

  version(): Promise<number> {
    return new Promise((resolve, reject) => {
      fetch("http://localhost:8765", {
        method: "POST",
        body: JSON.stringify({
          "action": "version",
          "version": 6
        }),
      })
        .then((resp) => resp.json())
        .then((json: AnkiConnectResponse) => resolve(json.result))
        .catch(() => reject(-1));
    });
  }

  getNumCardsReviewedToday() {
    return Promise.resolve<AnkiConnectResponse>({ result: 5, error: null });
  }

  deckNames(): Promise<string[]> {
    const request = {
      action: "deckNames",
      version: 6,
    };
    return new Promise((resolve) => {
      fetch("http://localhost:8765", {
        method: "POST",
        body: JSON.stringify(request),
      })
        .then((resp) => resp.json())
        .then((json: AnkiConnectResponse) => resolve(json.result))
        .catch(() => resolve([]));
    });
  }

  modelNames(): Promise<string[]> {
    const request = {
      action: "modelNames",
      version: 6,
    };
    return new Promise((resolve) => {
      fetch("http://localhost:8765", {
        method: "POST",
        body: JSON.stringify(request),
      })
        .then((resp) => resp.json())
        .then((json: AnkiConnectResponse) => resolve(json.result))
        .catch(() => resolve([]));
    });
  }

  modelFieldNames(modelName: string): Promise<string[]> {
    const request = {
      action: "modelFieldNames",
      version: 6,
      params: {
        modelName: modelName,
      },
    };
    return new Promise((resolve) => {
      fetch("http://localhost:8765", {
        method: "POST",
        body: JSON.stringify(request),
      })
        .then((resp) => resp.json())
        .then((json: AnkiConnectResponse) => resolve(json.result))
        .catch(() => resolve([]));
    });
  }

  addNote(
    deckName: string,
    modelName: string,
    resolvedValues: Record<string, string>
  ): Promise<AnkiConnectResponse> {
    const request = {
      action: "addNote",
      version: 6,
      params: {
        note: {
          deckName: deckName,
          modelName: modelName,
          fields: resolvedValues,
          options: {
            allowDuplicate: false,
          },
          tags: ["kyoro"],
        },
      },
    };

    return new Promise((resolve) => {
      fetch("http://localhost:8765", {
        method: "POST",
        body: JSON.stringify(request),
      })
        .then((resp) => resp.json())
        .then((json) => resolve(json))
        .catch(() =>
          resolve({ result: null, error: "Error submitting to Anki" })
        );
    });
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
