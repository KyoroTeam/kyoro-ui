interface KySuccessResponse {
  err: string;
  success: boolean;
}

interface KyLocalContentInfo {
  name: string;
  filetype: string;
  is_supported: boolean;
}

export interface KyTokenResult {
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
      fetch('http://localhost:8006/getIndexedSources/')
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function getTokenizedSentences(source: string): Promise<KyTokenResult[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyTokenResult[]>(`Kyoro.getTokenizedSentences:${source}`, resolve);
    } else {
      fetch(`http://localhost:8006/getTokenizedSentences/${encodeURIComponent(source)}/`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function getOnDiskSources(): Promise<KyLocalContentInfo[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyLocalContentInfo[]>(`Kyoro.getOnDiskSources`, resolve);
    } else {
      fetch(`http://localhost:8006/getOnDiskSources/`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function tokenizeOnDiskSource(sourceName: string): Promise<KySuccessResponse> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KySuccessResponse>(`Kyoro.tokenizeOnDiskSource:${sourceName}`, resolve);
    } else {
      fetch(`http://localhost:8006/tokenizeOnDiskSource/${sourceName}/`)
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}
