export type KyoroPyCmd =
  | 'Kyoro.getIndexedSources'
  | 'Kyoro.getTokenizedSentences'
  | 'Kyoro.getLocalSources'
  | 'Kyoro.tokenizeSource';

declare function pycmd<T>(command: KyoroPyCmd, callback?: (value: T) => void);
