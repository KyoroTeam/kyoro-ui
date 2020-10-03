module.exports = {
  singleQuote: true,
  trailingComma: 'all',
  printWidth: 120,
  proseWrap: 'always',
  tabWidth: 2,
  useTabs: false,
  bracketSpacing: true,
  semi: true,
  arrowParens: 'avoid',
  overrides: [
    {
      files: ['.prettierrc', '.eslintrc', '.babelrc', '.tern-project', '.stylelintrc', '.lighthouserc'],
      options: {
        parser: 'json',
      },
    },
    {
      files: ['package.json'],
      options: {
        printWidth: 180,
      },
    },
  ],
};
