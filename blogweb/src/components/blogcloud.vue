<template>
    <div class="card border-0 rounded-0 px-3 col-lg-3 d-none d-lg-block container-bg container-bs-green" id="tag-card">
        <div class="card-header bg-white px-0">
            <img class="tag mr-1" src="../images/tag.svg"/>
            <strong> 标&nbsp;签&nbsp;云</strong>
        </div>
        <div class="card-body px-0 py-3">
            <div class="tag-cloud">
                <template v-for="item in tagList">
                    <a href="#" v-bind:class="['badge','badge-'+item.color, 'p-2','m-1']" :data-id="item.tag_id" v-on:click.prevent="clickTag">{{item.name}}</a>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name:'blogcloud',
        props: {
            tags: {
                type: Array,
                required: true
            }
        },
        data() {
            return {
                colors: ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
            }
        },
        computed: {
            tagList() {
                var count = 0;
                //对tag标签重新组装附上新的颜色
                return this.tags.map(v=>{
                    v.color = this.colors[count];
                    count++;
                    count = count % this.colors.length;
                    return v
                })
            }
        },
        methods:{
            clickTag(e){
                var tag_id = e.currentTarget.dataset.id;
                this.$emit('getTag',{
                    tag_id:tag_id
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

    .card{
        align-self: flex-start;
    }
    .card-header {
        display: flex;
        align-items: center;
        /*border-bottom: 1px solid ;*/
        .tag {
            width: 1.25rem;
            height: 1.25rem;
        }

    }
    .badge{
        border-radius:unset;
    }

</style>