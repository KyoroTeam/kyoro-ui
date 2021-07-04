import type { SentecePart } from "./Jibiki";

export interface SelectTableRow {
  selected: boolean;
  sentenceParts: SentecePart[];
  english: string;
  source: string;
  tags: string[];
}
