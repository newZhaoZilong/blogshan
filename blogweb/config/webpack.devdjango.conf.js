/**
 * webpack-dev-server生成的图片,html，js都放在了服务器上，并不会看到实际的文件
 * 根据这一特性,现在将图片,html.js都放在根目录下,至于html如何引用到，生成方式和产品相同，生产顺序不同
 * 至于如何引用到vue,jquery，可以将production下的静态资源加载到服务器
 * :8080/index.html/../static/css/bootstrap.css = :8080/static/css/bootstrap.css
 * 为什么http计算路径的方法和文件夹是不同的,
 * 其实是相同的,路径算法应该是这样,:8080/../=:8080/是个关键点
 * :8080/index.html+../static/css/bootstrap.css = :8080/../static/css/bootstrap.css = :8080/static/css/bootstrap.css
 * file:///D:/important/blogweb/production/static/css/bootstrap.css
 * file:///D:/important/blogweb/production/templates/index.html+../static/css/bootstrap.css
 * =file:///D:/important/blogweb/production/templates/../static/css/bootstrap.css
 * =file:///D:/important/blogweb/production/static/css/bootstrap.css
 * npm run devh后生成了index.html main.js slide1-aaa.png我并没有指定他们的路径
 * 先生成index.html 再生成main.js 最后生成图片 publicPath可以修改html中的访问路径,path是真实路径？
 */
const path = require('path');
const webpack = require('webpack');
//这是用于自动生成html的插件
const HtmlWebpackPlugin = require('html-webpack-plugin')
//这是vue-loader必须使用的插件，不使用报错
const VueLoaderPlugin = require('vue-loader/lib/plugin')

const pages = require('../page.router').pages;

function getAPath(filePath) {
    return path.join(__dirname, '../',filePath)
}
console.log("path",getAPath('../blogproject/collect_static'))

var config = {
    mode: 'development',
    //打包的入口文件
    entry: {},
    output: {
        filename: "[name].js",
    },
    module: {
        //vue-loader用于解析.vue文件
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader'
        },
            // 它会应用到普通的 `.js` 文件
            // 以及 `.vue` 文件中的 `<script>` 块
            {
                test: /\.js$/,
                //这是正则表达式匹配node_modulesh或bower_components
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                        plugins: ['@babel/transform-runtime']
                    }
                }
            },
            // 普通的 `.scss` 文件和 `*.vue` 文件中的
            // `<style lang="scss">` 块都应用它
            {
                test: /\.scss$/,
                use: [
                    //这个vue-style-loader没有的话就不会生成style标签
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
            //url-loader 功能类似于 file-loader，但是在文件大小（单位 byte）低于指定的限制时，可以返回一个 DataURL
            {
                test: /\.(gif|jpg|jpeg|png|svg)$/,
                use: [{
                    loader: 'url-loader',
                    options: {
                        limit: 1024,
                        name: '[name].[ext]',
                    }
                }]
            }]
    },
    plugins: [
        //请确保引入这个插件来施展魔法
        new VueLoaderPlugin(),
        new webpack.DefinePlugin({
            //定义生产模式的服务器地址
            SERVERURL:JSON.stringify("http://www.shangeblog.com/")
        }),
        //模块热更新
        new webpack.HotModuleReplacementPlugin()
    ],
    // externals: {
    //     'vue': 'Vue',
    // },
    devtool: '#cheap-module-eval-source-map',
    devServer: {
        //会将production下的文件都加载到服务器里http://localhost:8080/templates
        //将production下的文件加载到服务器路径为http://localhost:8080/static/css/bootstrap.css
        //就是静态资源路径,转为指向django的静态资源路径
        contentBase: getAPath('../blogproject/collect_static'),
        //0.0.0.0手机也能用
        host: '0.0.0.0',
        overlay: {
            //错误全屏显示
            errors: true
        },
        hot: true
    },
}
pages.forEach((v)=>{
    var name = v.split('/').pop();
    config.entry[name] = getAPath(`src/${v}.js`);
    config.plugins.push(new HtmlWebpackPlugin({
        //输出文件目录
        filename: `${name}.html`,
        //模板html的路径
        template: getAPath('templates/baseA.html'),
        //输出html的标题
        title: name,
        //所包含的代码块即entry中的name
        chunks:[name],

    }))
})

module.exports = config