import { Base64Binary } from '../base64-binary';
import { inflate } from 'pako';

interface KySuccessResponse {
  err: string;
  success: boolean;
}

interface KyLocalContentInfo {
  name: string;
  filetype: string;
  is_supported: boolean;
}

export interface KyWordPosition {
  Start: number;
  End: number;
}

export interface KyTokenResult {
  Source: string;
  Sentence: string;
  Translation?: string;
  Words: string[];
  WordPositions: KyWordPosition[];
  Lemmas: string[];
  Readings: string[];
}

type KyIndexSourceInfo = [string, number, string];

export function getIndexedSources(): Promise<KyIndexSourceInfo[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyIndexSourceInfo[]>('Kyoro.getIndexedSources', resolve);
    } else {
      fetch('http://localhost:8006/getIndexedSources/')
        .then((r) => r.json())
        .then((json) => resolve(json));
    }
  });
}

export function getTokenizedSentences(sourceTid: number): Promise<KyTokenResult[]> {
  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<KyTokenResult[]>(`Kyoro.getTokenizedSentences:${sourceTid}`, resolve);
    } else {
      fetch(`http://localhost:8006/getTokenizedSentences/${sourceTid}/`)
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

export function getMinisearchJsonIndex(): Promise<string> {
  function decodeData(base64Data: string): string {
    const uint8array = Base64Binary.decode(base64Data);
    const jsonByteArray = inflate(uint8array);
    const jsonString = new TextDecoder().decode(jsonByteArray);
    return jsonString;
  }

  return new Promise((resolve) => {
    if (window.pycmd !== undefined) {
      window.pycmd<string>(`Kyoro.getMinisearchIndexGzip`, (base64Data) => {
        const json = decodeData(base64Data);
        resolve(json);
      });
    } else {
      fetch(`http://localhost:8006/getMinisearchIndexGzip/`)
        .then((r) => r.text())
        .then((base64Data) => {
          const json = decodeData(base64Data);
          console.log('Ok');
          resolve(json);
        });
    }
  });
}
