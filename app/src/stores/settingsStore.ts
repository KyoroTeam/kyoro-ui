import { writable } from "svelte/store";

export interface ICardMapping {
  mappingName: string;
  deckName: string;
  modelName: string;
  modelFieldMappings: Record<string, string>;
}

export interface IUserSettings {
  cardMappings: ICardMapping[];
}

export type KyoroFieldName = "English" | "Japanese" | "Source" | "Tags"

export default writable<IUserSettings>({ cardMappings: [] });
