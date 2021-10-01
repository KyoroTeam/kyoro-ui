import { writable } from 'svelte/store';

export interface ICardMapping {
  mappingName: string;
  modelName: string;
  modelFieldMappings: Partial<Record<KyoroFieldName, string>>;
}

export interface IUserSettings {
  cardMappings: ICardMapping[];
}

export type KyoroFieldName = 'English' | 'Japanese' | 'Source' | 'Tags';

export const cardMappingStore = writable<ICardMapping[]>([]);
