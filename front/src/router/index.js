import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/home.vue"
import about from "../views/about.vue"


Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        name:'home',
        component: home,
    },
    {
        path:'/custom_search',
        name:'custom search',
        component: about
    },
    {
        path: '/user/library',
        name:'user library',
        component: about
    },

    {
        path: '/user/friends',
        name:'user friends',
        component: about
    },

    {
        path: '/user/recommendation',
        name:'user rec',
        component: about
    },

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes

})

export default router
