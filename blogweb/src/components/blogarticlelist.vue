<template>
    <ul class="list-unstyled px-0 col-lg-8">
        <template v-for="item in acBlogList">
            <li class="media mb-2 p-lg-2 container-bg container-bs-green">
                <div class="item-img-container w-25 mr-3" :data-id="item.article_id" v-on:click="navigateToDetail">
                    <img class="w-100" v-bind:src="item.imgUrl" alt="Generic placeholder image">
                </div>
                <div class="media-body">
                    <div class="item-content-title mt-2 my-lg-2">
                        <h5 class="strong fs-3 fs-sm-4">
                            <a href="#" v-on:click.prevent="navigateToDetail"
                               :data-id="item.article_id">{{item.title}}</a>
                        </h5>
                        <div class="blogtime ml-1 ml-lg-2">
                            <img src="../images/calendar.svg"/>
                            <span class="ml-sm-1 fs-1 fs-sm-2 mr-1">{{isPhone?'':'更新时间: '}}{{item.update_date}}</span>
                        </div>
                    </div>
                    <p class="item-content-body mb-1 mb-sm-2 fs-1 fs-sm-3">
                        {{item.summary}}
                    </p>
                    <div class="item-content-category mb-1" :data-id="item.category_id" @click.stop="getCategory">
                        <div class="category-container text-danger fs-1 fs-sm-3">
                            <i class="fa fa-list-alt"></i>
                            <span class="category">分类: {{item.category}}</span>
                        </div>
                        <div class="readtimes-container mr-2 fs-1 fs-sm-2">
                            <i class="fa fa-eye"></i>
                            <span class="readtimes">阅读次数: {{item.read_times}}</span>
                        </div>
                    </div>
                </div>
            </li>
        </template>
    </ul>
</template>

<script>
    export default {
        name: "blogarticlelist",
        props: ['articles'],
        data() {
            return {
                blogArticleList: [],
                windowWidth: document.body.clientWidth,
                isPhone:false
            }
        },
        computed: {
            acBlogList() {
                return this.articles.map((v) => {
                    var title_num, content_num;
                    if (this.windowWidth > 576) {
                        title_num = 25;
                        content_num = 100;
                        this.isPhone = false;
                    } else {
                        title_num = 18;
                        content_num = 80;
                        this.isPhone = true;
                    }
                    if (v.title.length - 3 > title_num) {
                        v.title = v.title.substr(0, title_num) + '...'
                    }
                    if (v.summary.length - 3 > content_num) {
                        v.summary = v.summary.substr(0, content_num) + '...'
                    }
                    return v
                })
            }
        },
        created() {
            window.onresize = () => {
                clearTimeout(this.windowWidthTimeoutId);
                this.windowWidthTimeoutId = setTimeout(() => {
                    this.windowWidth = document.body.offsetWidth;
                }, 500)
            }
        },
        methods: {
            //跳转到文章页面
            navigateToDetail(event) {
                var article_id = event.currentTarget.dataset.id;
                // console.log('article_id',article_id)
                //跳转到article页面
                location.href = `detail.html?article_id=${article_id}`;
            },
            //点击跳转触发一个函数，被父组件接受，父组件更新props数据
            getCategory(event) {
                // console.log('category_id',event.currentTarget.dataset.id);
                var category_id = event.currentTarget.dataset.id;
                // this.$emit('getAr',{
                //     category_id:category_id
                // });
                location.href = `index.html?category_id=${category_id}`;
            }
        }
    }
</script>

<style lang="scss" scoped>
    .media {
        align-items: center;
    }

    .item-content-title {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: baseline;

        .blogtime {
            display: flex;
            flex-direction: row;
            align-items: center;
            /*flex-wrap: wrap-reverse;*/
            img {
                width: 0.8rem;
                height: 0.8rem;
            }
            span {
                white-space: nowrap;
            }
        }
    }

    .item-content-body {
        min-height: 4rem;
    }

    .item-content-category {
        display: flex;
        justify-content: space-between;
        .category-container{
            &:hover {
                color: darkred !important;
            }
        }
    }

    @media (min-width: 576px) {
        .blogtime > img {
            width: 1rem !important;
            height: 1rem !important;
        }
    }
</style>