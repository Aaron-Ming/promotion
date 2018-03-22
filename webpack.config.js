const path = require('path')
const webpack = require('webpack')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
function resolve(dir) {
  return path.resolve(__dirname, dir)
}


var config = {
    entry: {
      main: './src/main'
    },
    output: {
      path: resolve('statics'),
      filename: 'js/[name].[hash:8].js'
    },
    resolve: {
      extensions: ['.js', '.vue', '.json'],
      alias: {
        'vue$': 'vue/dist/vue.common.js',
        'src': resolve('src'),
        'components': resolve('src/components'),
        'pages': resolve('src/pages')
      }
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: 'vue-loader',
          options: {
            loaders: {
              css: ExtractTextPlugin.extract({
                use: 'css-loader',
                fallback: 'vue-style-loader'
              })
            }
          }
        },
        {
          test: /\.js$/,
          loader: 'babel-loader',
          exclude: /node_modules/
        },
        {
          test: /\.css$/,
          use: ExtractTextPlugin.extract({
              use: 'css-loader',
              fallback: 'style-loader',
              publicPath: '../'
          })
        },
        {
          test: /\.less$/,
          loader: "less-loader"
        },
        {
          test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
          loader: 'url-loader',
          options: {
              limit: 10000,
              name: 'img/[name].[hash:8].[ext]'
          }
        },
        {
          test: /\.(woff2?|eot|ttf|otf|svg)(\?.*)?$/,
          loader: 'url-loader',
          options: {
            limit: 10000,
            name: 'fonts/[name].[hash:8].[ext]'
          }
        }
      ]
    },
    plugins: [
      new CleanWebpackPlugin(['statics/css/main.*.css']),
      new CleanWebpackPlugin(['statics/js/main.*.js']),
      new ExtractTextPlugin("css/main.[hash:8].css"),
      new HtmlWebpackPlugin({
        filename: '../templates/dashboard.html',
        title: '钱方运维平台',
        inject: false,
        chunks: ['main'], // 加载哪些js 等 静态文件
        template: './src/index.html',
        minify: {
          removeComments: true,
          collapseWhitespace: false
        }
      })
    ]
};

module.exports = config;