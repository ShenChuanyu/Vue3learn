import { createRouter,createrWebHistory } from 'vue-router'
import MovieList from '@/views/MovieList.vue'

const router = createRouter({
    history:createrWebHistory(),
    router:[
        {
        path:'/movies',
        name:'MovieList',
        component:MovieList
    }
    ]
})