import { writable } from "svelte/store";

export interface ICardMapping {
  mappingName: string;
  modelName: string;
  fieldMappings: Record<string, string>;
}

export interface IUserSettings {
  cardMappings: ICardMapping[];
}

export default writable({ cardMappings: [] } as IUserSettings);
