import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.min';

import ArticleList from "./components/Articles/ArticleList";
import ArticleEditor from "./components/Articles/ArticleEditor";
Vue.use(BootstrapVue);
window.Vue = Vue;

new Vue({
    el: '#App',
    delimiters: ['${','}'],
    components: {
        ArticleList,
        ArticleEditor
    }
});
