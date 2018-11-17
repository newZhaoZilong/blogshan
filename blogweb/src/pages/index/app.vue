<template>
    <div>
        <blogheader :headerList="headerList" @getSearch="getArticleList"></blogheader>
        <main class="container px-1 pt-lg-3">
            <blogswiper v-if="isSwiper"></blogswiper>
            <blogcategorydesc v-else :detail="articleDetail"></blogcategorydesc>
            <div class="content mt-2 mt-lg-3">
                <blogarticlelist v-bind:articles="articles" @getAr="getArticleList"></blogarticlelist>
                <blogcloud v-bind:tags="tags" v-on:getTag="getArticleList"></blogcloud>
            </div>
        </main>
        <blogfooter></blogfooter>
    </div>
</template>
<script>
    import blogarticlelist from "../../components/blogarticlelist.vue"
    import blogcloud from "../../components/blogcloud.vue"
    import blogfooter from "../../components/blogfooter.vue"
    import blogheader from "../../components/blogheader.vue"
    import blogswiper from "../../components/blogswiper.vue"
    import blogweather from "../../components/blogweather.vue"
    import blogcategorydesc from "../../components/blogcategorydesc.vue"
    // import Utils from "../../js/Utils.js"

    export default {
        name: 'index',
        components: {
            blogarticlelist,
            blogcloud,
            blogfooter,
            blogheader,
            blogswiper,
            blogweather,
            blogcategorydesc
        },
        data() {
            return {
                myname: '赵青ge山',
                articles: [],
                tags: [],
                articleDetail: {},
                isSwiper:true,
                headerList: [{
                    isActive: true,
                    href: 'index.html?',
                    icon: 'fa-home',
                    name: '首页'
                }, {
                    isActive: false,
                    href: 'index.html?category_id=1',
                    icon: 'fa-paypal',
                    name: 'Python'
                }, {
                    isActive: false,
                    href: 'index.html?category_id=2',
                    icon: 'fa-scribd',
                    name: 'Javascript'
                }, {
                    isActive: false,
                    href: 'index.html?category_id=3',
                    icon: 'fa-cutlery',
                    name: '关于网站'
                }]
            }
        },
        created() {
            var queryObj = Utils.getQueryObj(location.search);
            //获取文章列表
            this.getArticleList(queryObj);
            //获取标签列表
            this.getTagList();
        },
        //方法要都写在这里面,包括自定义的和事件函数
        methods: {


            //获取tag列表
            getTagList() {
                API.getTagList()
                    .then((res) => {
                        this.tags = res;
                    })
            },
            //获取Article列表
            getArticleList(queryObj) {
                console.log('data的值是', queryObj);
                if (queryObj.category_id) {
                    this.headerList.forEach((v) => {
                        v.isActive = false;
                    })
                    this.headerList[queryObj.category_id].isActive = true;
                    this.isSwiper = false;
                    this.getCategoryDetail(queryObj);
                }

                if(queryObj.search){
                    queryObj.search = decodeURIComponent(queryObj.search)
                }

                if(queryObj.tag_id){
                    this.isSwiper = false;
                    this.getTagDetail(queryObj)
                }

                API.getArticleList(queryObj)
                    .then((res) => {
                        this.articles = res;
                    })
            },
            //获取分类详情
            getCategoryDetail(data) {
                API.getCategoryDetail(data)
                    .then((res) => {
                        this.articleDetail = {
                            name: res.name,
                            desc: res.category_desc,
                            type: '分类'
                        }
                    })
            },
            //获取标签详情
            getTagDetail(data) {
                API.getTagDetail(data)
                    .then((res) => {
                        this.articleDetail = {
                            name: res.name,
                            desc: res.tag_desc,
                            type: '标签'
                        }
                    })
            },
        },
    }
</script>
<style lang="scss">
    .content {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        flex-wrap: nowrap;
    }
</style>