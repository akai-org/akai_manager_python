<template>
    <tr role="row" >
        <td role="cell" >{{article.title}}</td>
        <td role="cell" class="d-none d-lg-table-cell">{{article.description}}</td>
        <td role="cell">{{
            article.author.first_name.length&&article.author.last_name.length?
            `${article.author.first_name} ${article.author.last_name}`:
            article.author.email
            }}
        </td>
        <td role="cell">
            {{article.updated_at.split('.')[0].replace('T', '\n')}}
        </td>
        <td role="cell">
            <b-link :href="`/cms/articles/${article.id}/edit`" class="btn btn-primary">Edit</b-link>
        </td>
        <td role="cell">
            <b-btn @click="$emit('remove', article.id)" class="btn btn-danger">Delete</b-btn>
        </td>
    </tr>
</template>

<script>
    export default {
        name: "ArticleListItem",
        props: {
            article: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped lang="scss">
    td{
        vertical-align: middle!important;
    }
</style>