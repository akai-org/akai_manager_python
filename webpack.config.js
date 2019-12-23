const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  mode: 'production',
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  entry: {
    index: ['./static/src/index.js', './static/src/index.scss'],
    cms: ['./static/src/cms.js']
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].css"
    }),
    new VueLoaderPlugin(),

  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            'sass-loader'
        ]
      },
      {
        test: /\.css$/,
        use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
        ]
      },
      {
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel-loader',
      },
      {
          test: /\.vue$/,
          loader: 'vue-loader'
      }
    ]
  },
};