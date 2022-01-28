export interface KyoTokenResult {
  Source: string;
  Sentence: string;
  Translation?: string;
  Words: string[];
  WordPositions: { Start: number; End: number }[];
  Lemmas: string[];
  Readings: string[];
}
