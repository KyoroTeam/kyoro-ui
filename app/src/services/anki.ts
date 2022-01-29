interface KyoSuccessResponse {
  err: string;
  success: boolean;
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

export function getIndexedSources(): Promise<string[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<string[]>('Kyoro.getIndexedSources', resolve);
    } else {
      fetch('http://localhost:8006/getIndexedSources')
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function getTokenizedSentences(source: string): Promise<KyoTokenResult[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyoTokenResult[]>(`Kyoro.getTokenizedSentences:${source}`, resolve);
    } else {
      fetch(`http://localhost:8006/getTokenizedSentences/${encodeURIComponent(source)}`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function getOnDiskSources(): Promise<string[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<string[]>(`Kyoro.getOnDiskSources`, resolve);
    } else {
      fetch(`http://localhost:8006/getOnDiskSources/`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function tokenizeOnDiskSource(sourceName: string): Promise<KyoSuccessResponse> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyoSuccessResponse>(`Kyoro.tokenizeOnDiskSource:${sourceName}`, resolve);
    } else {
      fetch(`http://localhost:8006/tokenizeOnDiskSource/${sourceName}`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}
