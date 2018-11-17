module.exports = function(env){

const path = require('path');
const webpack = require('webpack');
//这是用于自动生成html的插件
const HtmlWebpackPlugin = require('html-webpack-plugin')
//这是vue-loader必须使用的插件，不使用报错
const VueLoaderPlugin = require('vue-loader/lib/plugin')

console.log('serverurl',env.serverurl);
console.log('outputPath',getAPath('../blogproject/collect_static/static/blog/pages'));

const pages = require('../page.router').pages;

function getAPath(filePath) {
    return path.join(__dirname, '../',filePath)
}

var config = {
    mode: 'production',
    entry: {},
    output: {
        filename: "[name].js",
        path: getAPath('../blogproject/collect_static/static/blog/pages'),
    },
    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader'
        },
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env'],
                    plugins: ['@babel/transform-runtime']
                }
            }
        },
        {
            test: /\.scss$/,
            use: [
                'vue-style-loader',
                'css-loader',
                {
                    loader: 'postcss-loader',
                    options: {
                        sourceMap: true,
                    }
                },
                'sass-loader'
            ]
        },
        {
            test: /\.(gif|jpg|jpeg|png|svg)$/,
            use: [{
                loader: 'url-loader',
                options: {
                    limit: 1024,
                    //输出到production文件夹下的images文件夹,引用路径变成images/filename
                    //这个images输出路径是相对outputpath的文件夹的
                    //而image的引用路径确和name一样，但是html的位置和boudle.js不同,所以html并不能引用到图片
                    name: '../images/[name].[ext]',//path.join(__dirname, '../production/static/images/[name].[ext]'),//,//'../images/[name]-aaa.[ext]'
                    //图片在html的路径是publicPath+name  ,所以自己要计算,保证html能引用到图片
                    publicPath:'/static/blog/images'
                }
            }]
        }]
    },
    plugins: [new VueLoaderPlugin(),
        new webpack.DefinePlugin({
            //定义生产模式的服务器地址
            SERVERURL:JSON.stringify(env.serverurl)
        }),
    ],
    // externals: {'vue': 'Vue'},
}
pages.forEach((v)=>{
    var name = v.split('/').pop();
    config.entry[name] = getAPath(`src/${v}.js`);
})
// console.log(config)
return config
}
// console.log(config)

