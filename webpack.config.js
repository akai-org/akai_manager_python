const path = require('path');

module.exports = {
  module: {
    rules: [
      {
        test:/\.(s*)css$/,
        use: ['style-loader', 'css-loader', 'sass-loader'],

      }
    ],
  },
  entry: './static/src/',
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
};