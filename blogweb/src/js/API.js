// var serverUrl = 'http://127.0.0.1:8000/';
// var serverUrl = 'http://23.105.195.226:8000/';
//serverURL已经在webpack.DefinePlugin里定义了,所以这里就不用定义了
console.log('API SERVERURL',SERVERURL)
var serverUrl = SERVERURL;

function API(serverUrl) {
    this.serverUrl = serverUrl
}
API.prototype.CallApi = function(url, postData) {
    return new Promise(function (resolve, reject) {
        $.ajax({
            url: url,
            type: 'POST',
            data: postData,
            success: function (res) {
                console.log('post请求结果', res, postData)
                if (res.code == 0) {
                    //如果请求成功,判断successCF是否是函数,是的话,将res.data传进去
                    resolve(res.result)
                } else {
                    reject(res.errmsg)
                }
            },
            error: reject
        })
    })
}


var api = new API(serverUrl)
var routeObj = {
    getArticleList: 'blog/getArticleList',
    getArticleDetail: 'blog/getArticleDetail',
    getTagList: 'blog/getTagList',
    getTagDetail: 'blog/getTagDetail',
    getCategoryDetail: 'blog/getCategoryDetail',
    getCarrouselList: 'blog/getCarrouselList',
}

for (let i in routeObj) {
    if (typeof routeObj[i] === 'string') {
        api[i] = function (postData = {}) {
            var url = `${serverUrl}${routeObj[i]}/`;
            return this.CallApi(url, postData);
        }
    }
}

global.API = api;


