<template>
    <div>
        <table role="table" aria-colcount="3" class="table b-table table-striped table-hover table-light table-responsive-md article-list">
            <thead role="rowgroup" class="thead-dark">
                <tr role="row">
                    <th role="columnheader">Title</th>
                    <th role="columnheader" class="d-none d-lg-table-cell">Description</th>
                    <th role="columnheader">Author</th>
                    <th role="columnheader">Updated at</th>
                    <th role="columnheader"></th>
                    <th role="columnheader"></th>
                </tr>
            </thead>
            <tbody role="rowgroup" v-if="articles.length">
                <ArticleListItem v-for="article in articles" :key="article.id" :article="article" @remove="removeArticleModal"/>
            </tbody>
            <h4 class="text-center" v-else>
                Brak zawartości do wyświetlenia
            </h4>
            <b-tfoot class="thead-dark">
                <th></th>
                <th class="d-none d-lg-table-cell"></th>
                <th></th>
                <th></th>
                <th></th>
                <th><b-link class="btn btn-success" href="/cms/articles/create">Nowy</b-link></th>
            </b-tfoot>
        </table>
        <b-modal ref="del_article" hide-footer title="Usuwanie artykuły">
          <div class="d-block text-center">
            <h3 v-if="!modalError">Czy na pewno chcesz usunąć artykuł "{{activeArticle.title}}"?</h3>
            <h3 v-else>Nie udało się usunąć artykułu "{{activeArticle.title}}"</h3>
          </div>
          <b-button class="mt-3" variant="outline-danger" block @click="removeArticle" >Usuń</b-button>
          <b-button class="mt-2" variant="outline-warning" block @click="hideModal">Cofnij</b-button>
        </b-modal>

    </div>
</template>

<script>
    import axios from 'axios';
    import ArticleListItem from "./ArticleListItem";
    import { get } from 'js-cookie';
    export default {
        name: "ArticleList",
        components: {
            ArticleListItem
        },
        data(){
            return{
                articles: [],
                activeArticle: {},
                modalError: false
            }
        },
        created() {
            axios.get('/cms/api/articles')
                .then(({data}) => {
                    this.articles = data
                })
                .catch(error => {
                    console.log(error);
                })
        },
        methods: {
            removeArticleModal(idToRemove){
                this.modalError = false;
                this.activeArticle = this.articles.filter(({id})=> id == idToRemove)[0];
                this.$refs['del_article'].show();
            },
            removeArticle(){
              axios.delete(`/cms/api/articles/${this.activeArticle.id}`,
                  {
                      headers: {
                          'X-CSRFToken': get('csrftoken')
                      }
                  })
                .then((data) => {
                    this.articles = this.articles.filter(article => article !== this.activeArticle);
                    this.activeArticle = {};
                    this.hideModal();
                })
                .catch(error => {
                    console.log(error);
                    this.modalError = true;
                })
            },
            hideModal() {
                this.$refs['del_article'].hide();
                this.modalError = false;
            },
        }
    }
</script>

<style lang="scss">
    .article-list {
        tr {
            td:nth-child(3), td:nth-child(4){
                width: 15%!important;
            }
            td:nth-child(5), td:nth-child(6){
                width: 5%!important;
            }
        }
    }
</style>