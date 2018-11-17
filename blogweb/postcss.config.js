const autoprefixer = require('autoprefixer');
//这个配置文件不写的话就会报错,autoprefixer首先要安装
module.exports = {
    plugins:[
        autoprefixer()
    ]
}