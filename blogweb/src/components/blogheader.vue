<template>
        <!--navbar navbar-expand-lg navbar-light bg-light-->

        <nav class="navbar navbar-expand-lg navbar-light container-bg py-0 py-md-2 container-bs-green fixed-top head-romm headroom--pinned">
            <a class="navbar-brand mx-0 mx-sm-4 fs-5 fs-sm-7 strong" href="index.html"><i class="fa fa-medium mr-1 mr-lg-2"></i>阿山博客</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03"
                    aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                <ul class="navbar-nav ml-auto mt-2 mt-lg-0 mr-lg-3">
                    <template v-for="item in headerList">
                        <li class="nav-item" v-bind:class="{active:item.isActive}">
                            <a class="nav-link px-lg-2 fs-sm-3" v-bind:href="item.href"><i v-bind:class="['fa',item.icon, 'mr-lg-1']"></i>{{item.name}}</a>
                        </li>
                    </template>
                    <!--<li class="nav-item active">-->
                        <!--<a class="nav-link px-lg-2 fs-sm-3" href="#"><i class="fa fa-home mr-lg-1"></i>首页</a>-->
                    <!--</li>-->
                    <!--<li class="nav-item">-->
                        <!--<a class="nav-link px-lg-2 fs-sm-3" href="#"><i class="fa fa fa-paypal mr-lg-1"></i>Python</a>-->
                    <!--</li>-->
                    <!--<li class="nav-item">-->
                        <!--<a class="nav-link px-lg-2 fs-sm-3" href="#"><i class="fa fa-scribd mr-lg-1"></i>Javascript</a>-->
                    <!--</li>-->
                    <!--<li class="nav-item">-->
                        <!--<a class="nav-link px-lg-2 fs-sm-3 mr-lg-3" href="#"><i class="fa fa fa-cutlery fa-fw mr-lg-1"></i>关于网站</a>-->
                    <!--</li>-->
                </ul>
                <form action="index.html" class="form-inline my-2 my-lg-0" method="get" >
                    <input class="form-control mr-sm-2" type="search" placeholder="请输入关键字" aria-label="Search" name="search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">搜索</button>
                </form>
            </div>
        </nav>



</template>
<script>
    export default {
        name:'blogheader',
        props:['headerList'],
        data() {
            return {
                name: '赵青山',
                isMouseUp:true,
                search:''
            }
        },
        created(){
            console.log('created')
        },
        mounted(){
            console.log('第三键的mounted')
        },
        methods:{
            searchArt(){
                this.$emit('getSearch',{
                    search:this.search
                })
            }
        }


    }
</script>
<style lang="scss" scoped>
    //对于选中的文字，如首页，颜色变为橙色，加粗
    .navbar-light .navbar-nav .active .nav-link{
        color: #dc3545;
        font-weight: bold;
    }
    //右上角的响应式toggler边框加黑
    .navbar-light .navbar-toggler {
        color: rgba(0, 0, 0, 0.5);
        border-color: rgba(0, 0, 0, 0.5);
    }
    .head-romm{
        transition: transform 200ms linear;
    }
    .headroom--pinned {
        transform: translateY(0%);
    }
    .headroom--unpinned{
        transform: translateY(-100%);
    }

</style>