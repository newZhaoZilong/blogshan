<template>
    <div>
        <blogheader :headerList="headerList"></blogheader>
        <main class="container px-1 content px-0">
            <blogbreadcrumb :category="article.category" :title="article.title" :category_id="article.category_id"></blogbreadcrumb>
            <blogarticle :article="article"></blogarticle>
        </main>
        <blogfooter></blogfooter>
    </div>
</template>

<script>
    import blogarticle from "../../components/blogarticle.vue"
    import blogheader from "../../components/blogheader.vue"
    import blogbreadcrumb from "../../components/blogbreadcrumb.vue"
    import blogfooter from "../../components/blogfooter.vue"

    export default {
        name: "app",
        components: {
            blogarticle,
            blogheader,
            blogbreadcrumb,
            blogfooter
        },
        data() {
            return {
                article:{},
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
            this.getArticleDetail(queryObj)
            console.log(location.search);
        },
        methods:{
            getArticleDetail(data){
                API.getArticleDetail(data)
                    .then((res)=>{
                        this.headerList.forEach((v) => {
                            v.isActive = false;
                        })
                        this.headerList[res.category_id].isActive = true;
                        this.article = res;
                    })
            }
        }
    }
</script>

<style lang="scss" scoped>
    .content {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
</style>