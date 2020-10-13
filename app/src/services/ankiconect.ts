export interface IAnkiConnect {
  version: () => Promise<Response>;
  getNumCardsReviewedToday: () => Promise<Response>;
}

export class AnkiConnect implements IAnkiConnect {
  version() {
    return Promise.resolve<Response>({ result: 5, error: null });
  }
  getNumCardsReviewedToday() {
    return Promise.resolve<Response>({ result: 5, error: null });
  }
}

export interface Request {
  action: string;
  version: number;
  params: object;
  key?: number;
}

export interface Response {
  result: any;
  error: string | null;
}
