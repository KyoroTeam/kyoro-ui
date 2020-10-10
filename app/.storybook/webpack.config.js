const path = require('path');
const webpack = require('webpack');

module.exports = ({ config, mode }) => {
  const svelteLoader = config.module.rules.find(r => r.loader && r.loader.includes('svelte-loader'));

  svelteLoader.options = {
    ...svelteLoader.options,
    emitCss: true,
    hotReload: false,
    preprocess: require('svelte-preprocess')({}),
  };

  config.module.rules.push({
    test: /\.css$/,
    loaders: [
      {
        loader: 'postcss-loader',
        options: {
          sourceMap: true,
          config: {
            path: './.storybook/',
          },
        },
      },
    ],

    include: path.resolve(__dirname, '../storybook/'),
  });

  return config;
};
