<template>
    <div class="article-container">
        <div class="article-main col-lg-9 container-bg px-sm-4 container-bs-green">
            <div class="article-timeread mt-2 mt-lg-3 text-info">
                <div class="article-time fs-1 fs-sm-2"><i class="fa fa-calendar-minus-o"></i> 更新时间 : {{article.update_date}}</div>
                <div class="article-readtimes fs-1 fs-sm-2"><i class="fa fa-eye"></i> 阅读次数 : {{article.read_times}}</div>
            </div>
            <article class="article-body mt-2" v-html="article.html_body"></article>
            <section class="article-tag ml-3">
                <span class="strong mr-1"> 文章标签 : </span>
                <template v-for="item in tagList">
                    <a :href="'index.html?tag_id='+item.tag_id" v-bind:class="['badge','badge-'+item.color, 'p-2','m-1']">{{item.name}}</a>
                </template>
            </section>
            <section class="article-next m-3"><a :href="'detail.html?article_id='+article.next_id">下一篇 : {{article.next_title}} <i class="fa fa-hand-o-right"></i></a></section>
        </div>
        <section class="article-toc fs-sm-3 d-none d-lg-block p-0 container-bg container-bs-green"
                 v-html="article.toc"></section>
    </div>
</template>
<script>
    export default {
        props: ["article"],
        name: "blogarticle",
        data(){
            return {
                colors: ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
            }
        },
        computed: {
            tagList() {
                var count = 0;
                if(this.article.tags){
                    //对tag标签重新组装附上新的颜色
                    return this.article.tags.map(v=>{
                        v.color = this.colors[count];
                        count++;
                        count = count % this.colors.length;
                        return v
                    })
                }

            }
        }
    }
</script>
<style lang="scss">
    @import "../scss/native.scss";
    .article-container {
        width:100%;
        display: flex;
        /*justify-content: center;*/
    }
    .article-timeread{
        display:flex;
        justify-content: space-between;
        align-items: center;
    }
    .article-body {
        h1 {
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: deepskyblue;
            margin-bottom: 1rem;
        }
        h2 {
            padding:0.5rem 1rem;
            font-size: 1.25rem;
            font-weight: bold;
            border-left: 5px solid #20c997;
            background-color: #efefef;
        }
        h3 {
            padding: 0.3rem 1rem;
            font-size: 1.1rem;
            font-weight: bold;
            border-left: 5px solid #d0d0d0;
            background-color: #f7f7f7;
        }
        p{
            font-size:0.95rem;
            text-indent: 1rem;
        }
        pre {
            padding: 1rem;
        }
        img{
            max-width:80%;
        }
        strong{
            color:red;
        }
    }
    .article-tag{
        color:orangered;
        display: flex;
        align-items:center;
    }
    .article-next{
        text-align: left;
        font-weight: bold;
    }


    @media (min-width: 576px) {
        .article-body {
            h1 {
                text-align: center;
                font-size: 1.75rem;
                font-weight: bold;
                color: deepskyblue;
                margin-bottom: 2rem;
            }
            h2 {
                padding:0.8rem 1rem;
                font-size: 1.5rem;
                font-weight: bold;
                border-left: 5px solid #20c997;
                background-color: #f7f7f7;
            }
            h3{
                padding: 0.5rem 1rem;
                font-size: 1.25rem;
                font-weight: bold;
                border-left: 5px solid #d0d0d0;
                background-color: #f7f7f7;
            }

            p{
                text-indent: 1rem;
            }
            pre {
                padding: 1.2rem;
            }
        }
    }

    //导航条的样式
    .article-toc {
        max-width:16rem;
        margin-left: 1.5rem;
        align-self: flex-start;
        /*flex: 1;*/
        .toc {
            padding-left: 1.5rem;
            ul {
                list-style-type: none;
                padding: 0.75rem;
            }
            a {
                display: inline-block;
                font: normal normal normal 14px/1 FontAwesome;
                font-size: inherit;
                text-rendering: auto;
                -webkit-font-smoothing: antialiased;
                color: black;
                &:hover {
                    color: orangered;
                }
            }
        }
        .toc > ul > li >a{
            font-size: 1rem;
            &:before {
                content: "\f0a9 "
            }
        }
        .toc > ul > li > ul > li>a{
            font-size: 0.9rem;
            &:before {
                content: "\f101 "
            }
        }
        .toc a{
            font-size: 0.8rem;
            &:before {
                content: "\f105 "
            }
        }
    }
</style>