<template>
    <div class="card bg-light mb-2 mb-lg-3 container-bg container-bs-green">
        <div class="card-header strong fs-3 fs-sm-4">文章{{detail.type}} :  {{detail.name}}</div>
        <div class="card-body fs-2 fs-sm-3">
            <!--<h5 class="card-title">Light card title</h5>-->
            <p class="card-text">{{detail.desc}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props:['detail'],
        name: "blogcategorydesc"
    }
</script>

<style lang="scss" scoped>
</style>