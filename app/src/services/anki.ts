import { Base64Binary } from '../base64-binary';
import { inflate } from 'pako';

export interface KyTokenResult {
  Source: string;
  Sentence: string;
  Translation?: string;
  Words: string[];
  WordPositions: KyWordPosition[];
  Lemmas: string[];
  Readings: string[];
}

export interface KyWordPosition {
  Start: number;
  End: number;
}

export interface KyTokenizedStatInfo {
  name: string;
  index_state: 'needs-reindex' | 'fully-indexed' | 'not-indexed';
}

export function getCurrentIndexState(): Promise<KyTokenizedStatInfo[]> {
  return receivePyCmd<KyTokenizedStatInfo[]>('getCurrentIndexState');
}

export function tokenizeOnDiskSource(sourceName: string): Promise<KyTokenResult[]> {
  return receivePyCmd<KyTokenResult[]>('tokenizeOnDiskSource', sourceName);
}

export function getMinisearchJsonIndex(): Promise<string> {
  function decodeData(base64Data: string): string {
    const uint8array = Base64Binary.decode(base64Data);
    const jsonByteArray = inflate(uint8array);
    const jsonString = new TextDecoder().decode(jsonByteArray);
    return jsonString;
  }

  return receivePyCmd<string>('getMinisearchIndexGzip').then(decodeData);
}

interface KyPyCmdResponse<T> {
  error: string | null;
  result: T | undefined;
}

function receivePyCmd<T>(command: string, argument?: string): Promise<T> {
  return new Promise((resolve, reject) => {
    function onData(data: KyPyCmdResponse<T>) {
      if (!data.error) {
        resolve(data.result!);
      } else {
        reject(data.error);
      }
    }

    if (window.pycmd !== undefined) {
      const argument_s = argument ? `:${argument}` : '';
      window.pycmd<KyPyCmdResponse<T>>(`Kyoro.${command}${argument_s}`, onData);
    } else {
      const argument_s = argument ? `${argument}/` : '';
      fetch(`http://localhost:8006/${command}/${argument_s}`)
        .then((r) => r.json())
        .then(onData);
    }
  });
}
