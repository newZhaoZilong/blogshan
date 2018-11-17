<template>
    <div id="carouselExampleIndicators"
         class="carousel slide carousel-size container-bg d-sm-block container-bs-green" data-ride="carousel">
        <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
        </ol>
        <div class="carousel-inner">
            <!--<template v-for="item in swiperList">-->
                <!--<div class="carousel-item" :data-addclassname="item.addclassname">-->
                    <!--<img class="d-block w-100" :src="item.imgUrl" alt="First slide">-->
                <!--</div>-->
            <!--</template>-->
            <div class="carousel-item active" data-addclassname="container-bs-green">
                <img class="d-block w-100" src="../images/blogslide1.png" alt="First slide">
            </div>
            <div class="carousel-item" data-addclassname="container-bs-yellow">
                <img class="d-block w-100" src="../images/blogslide2.png" alt="Second slide">
            </div>
            <div class="carousel-item" data-addclassname="container-bs-purple">
                <img class="d-block w-100" src="../images/blogslide3.png" alt="Third slide">
            </div>
            <div class="carousel-item" data-addclassname="container-bs-blue">
                <img class="d-block w-100" src="../images/blogslide4.png" alt="Third slide">
            </div>
        </div>
        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
        </a>
        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
        </a>
    </div>
</template>

<script>
    export default {
        name: "blogswiper",
        data(){
            return{
                swiperList:[{
                    imgUrl:'../images/blogslide1.png',
                    addclassname:'container-bs-green'
                }, {
                    imgUrl:'../images/blogslide2.png',
                    addclassname:'container-bs-green'
                }, {
                    imgUrl:'../images/blogslide3.png',
                    addclassname:'container-bs-green'
                }, {
                    imgUrl:'../images/blogslide4.png',
                    addclassname:'container-bs-green'
                }]
            }
        }
    }
</script>

<style lang="scss">
    .carousel-indicators{
        /*bottom: 0;*/
        margin-bottom:0;
    }
    @media (min-width: 576px){
        .carousel-indicators{
            /*bottom: 10px;*/
            margin-bottom:1rem;
        }

    }

</style>