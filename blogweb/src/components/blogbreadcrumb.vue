<template>
    <!--// class="d-none d-sm-block"-->
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb fs-2 fs-sm-3 mb-0 mb-lg-1">
            <li class="breadcrumb-item"><a href="index.html"><i class="fa fa-home"></i>首页</a></li>
            <li class="breadcrumb-item"><a :href="'index.html?category_id='+category_id">{{category}}</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{title}}</li>
        </ol>
    </nav>
</template>

<script>
    export default {
        props: ['category_id','category','title'],
        name: "blogbreadcrumb"
    }
</script>

<style lang="scss" scoped>
    .breadcrumb {
        background-color: hsla(120, 100%, 100%, 0.5);
        box-shadow: 0px 0px 10px white;
        flex-wrap:nowrap;
        li{

            white-space: nowrap;
            &:last-child{
                overflow: hidden;
                text-overflow: ellipsis;
            }
            a{
                color:green;
            }
        }
    }
</style>