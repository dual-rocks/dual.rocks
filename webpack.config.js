const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: './src/index.js',
  resolve: {
    alias: {
      vue: 'vue/dist/vue.common.js'
    }
  },
  output: {
    path: path.resolve(__dirname, 'assets'),
    filename: 'dual.rocks.js'
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'dual.rocks.css'
    })
  ],
  module: {
    rules: [
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.(png|jpe(g)?|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              outputPath: 'images'
            }
          },
        ],
      },
      {
        test: /\.(woff(2)?|eot|ttf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              outputPath: 'fonts'
            }
          }
        ],
      },
    ],
  }
};
