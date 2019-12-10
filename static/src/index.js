// Django admin dependencies
import jquery from 'jquery';
import Select2 from 'select2';
import XRegexp from 'xregexp';

// Vue dependencies
import Vue from 'vue/dist/vue.esm';
import BootstrapVue from 'bootstrap-vue';

Vue.use(BootstrapVue);

const app = new Vue({
    el: '#App',
});

module.exports(app);