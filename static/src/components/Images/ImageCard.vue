<template>
    <a :href="image.url" target="_blank">
        <div class="text-black-50 p-2 position-relative image-management">
            <img v-if="image.url" class="w-100 rounded" :src="image.url" />
            <div v-if="image.url" class="bg-white rounded-circle circle text-center position-absolute" @click.stop.prevent="$emit('remove', image.id)">x</div>
        </div>
    </a>
</template>

<script>
    export default {
        name: "ImageCard",
        props: {
            image: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped lang="scss">
    .circle{
        width: 50px!important;
        height: 50px!important;
        font-size: 30px;
        font-weight: bold;
        padding-bottom: 10px;
        top: calc(50% - 22px);
        left: calc(50% - 22px);
        box-shadow: #909090 0 0 10px;
        transition: .5s ease-in-out;
        cursor: pointer;
        opacity: 0.3;
        &:hover{
            transform: scale(1.2);
            opacity: 0.8;
        }
    }
</style>