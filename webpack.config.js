const path = require('path');

module.exports = {
  entry: './static/src/index.js',
  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, 'static/dist'),
  },
};