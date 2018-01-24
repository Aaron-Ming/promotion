var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
function resolve(dir) {
  return path.resolve(__dirname, dir)
}


var config = {
    entry: {
        main: './src/main'
    },
    output: {
        path: path.join(__dirname, 'statics/js'),
        filename: '[name].js'
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
                    fallback: 'style-loader'
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
                    name: '../img/[name].[hash:8].[ext]'
                }
            },
            {
                test: /\.(woff2?|eot|ttf|otf|svg)(\?.*)?$/,
                loader: 'url-loader',
                options: {
                  limit: 10000,
                  name: '../fonts/[name].[hash:8].[ext]'
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin("../css/main.css")
    ]
};

module.exports = config;