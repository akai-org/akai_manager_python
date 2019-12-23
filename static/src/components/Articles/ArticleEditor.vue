<template>
    <div class="row">
        <div class="col-12 bg-light rounded p-2">
            <a href="/cms/articles" class="btn btn-danger d-block m-1 float-right">Anuluj</a>
            <button class="btn btn-primary d-block m-1 float-right" @click="addArticle">Zapisz</button>
        </div>

        <div class="col-xlg-10 col-lg-9 col-md-8 col-12">
            <div class="p-1">
                    <label for="title">Tytuł:</label>
                    <b-form-input placeholder="Tytuł artykułu" v-model="title" id="title" />
            </div>
            <div class="p-1">
                <label for="description">Opis:</label>
                <b-form-textarea placeholder="Krótki opis" v-model="description" id="description" />
            </div>
            <div class="p-1">
                <vue-editor v-model="content"/>
            </div>
        </div>

        <div class="col-xlg-2 col-lg-3 col-md-4 col-12 pt-5">
            <div class="card text-white bg-dark mb-3">
                <div class="card-header">Tags</div>
                <div class="card-body">
                    <multiselect v-model="tags" :options="avaliable_tags" :multiple="true" label="name" track-by="id" />
                </div>
            </div>

            <div class="card text-white bg-dark mb-3">
                <div class="card-header">Cover image</div>
                <img class="card-img-top" src="https://i.ytimg.com/vi/NCZ0eg1zEvw/maxresdefault.jpg" alt="Card image cap">
            </div>
            <div class="card text-white bg-dark mb-3">
                <div class="card-header">
                    Images:
                    <label for="img_add" class="float-right font-weight-bold" >+</label>
                    <input type="file" ref="img_add" class="d-none" id="img_add" multiple @change="addImage">
                </div>
                <ImageCard v-for="img in images" :key="img.id" :image="img" @remove="removeImg"/>
            </div>
        </div>
    </div>
</template>

<script>
	import { VueEditor } from 'vue2-editor';
    import { get } from 'js-cookie';
    import axios from 'axios';
    import Multiselect from 'vue-multiselect'
    import ImageCard from '../Images/ImageCard';
    export default {
        name: "ArticleEditor.vue",
        components: {
            VueEditor,
            ImageCard,
            Multiselect,
        },
        data(){
            return {
                content: "",
                description: "",
                title: "",
                cover_image: {},
                images: [
                    {
                        id: 1,
                        url: 'https://i.ytimg.com/vi/NCZ0eg1zEvw/maxresdefault.jpg'
                    },
                    {
                        id: null
                    }
                ],
                tags: [],
                avaliable_tags: ['a','b','c']
            }
        },
        methods: {
            removeImg(img_id){
                this.images = this.images.filter(({id}) => img_id != id)
            },
            addImage(){
                let data = new FormData();
                this.$refs.img_add.files.map((img, id) => data.append(`files[${id}]`, img));
                axios.post('/cms/api/images',
                    data,
                    {
                        headers:{
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                )
                .then(result => this.images = [...this.images, result])
                .catch(error => console.log(error))
            },
            addArticle(){
                let data = new FormData();
                data.append('title', this.title);
                data.append('content', this.content);
                data.append('description', this.description);
                data.append('cover_image', this.cover_image.id);
                this.images.map(({ext_id}, id) => data.append(`files[${id}]`, ext_id));
                axios.post(`/cms/api/articles/`,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data',
                            'X-CSRFToken': get('csrftoken')
                        }
                    })
                    .then(({data}) => window.location.href=`/cms/articles/${data.id}`)
                    .catch(error => console.log(error))
            }
        },
        mounted() {
            axios.get('/cms/api/tags')
            .then(({data}) => this.avaliable_tags = data)
            .catch(error => console.log(error))
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"/>

<style scoped>
</style>