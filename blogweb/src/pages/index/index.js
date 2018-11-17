// import Vue from 'vue';


import app from './app.vue'
//导入API对象，一个用于ajax的对象
import '../../js/API.js';
//工具
import "../../js/Utils.js"
//一些用于全局动画的js
import globaljs from '../../js/global.js';

//导入scss文件时直接导入路径的
import '../../scss/global.scss'




const root = document.createElement('div');
document.body.append(root);

console.log('process.env.NODE_ENV', process.env.NODE_ENV);
//创建一个vue组件并将其挂载到root div上，render方法
new Vue({
    name: 'root',
    render(createElement) {
        return createElement(app);
    },
    mounted() {
        console.log('主键的mounted')
        //执行global中的方法,主要是一些动画,这样能保证在元素生成之后执行
        //否则可能找不到元素,其实无所谓,马上要修改
        globaljs()
    }
}).$mount(root)






