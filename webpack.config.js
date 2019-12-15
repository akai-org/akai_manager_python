const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js'
    }
  },
  entry: {
    index: ['./static/src/index.js', './static/src/index.scss']
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/dist'),
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "index.css"
    })
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
      }
    ]
  },
};