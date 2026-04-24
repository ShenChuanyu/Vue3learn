<template>
    <div class="movie-list">
        <h2>电影列表</h2>
        <div v-if="loading">加载中……</div>
        <div v-else>
            <div v-for="movie in movies" :key="movie.id" class="movie-item">
                <img :src="getImageUrl(movie.image_url)" :alt="movie.movie_name">
                <h3>{{ movie.movie_name }}</h3>
                <p>导演：{{ movie.director }}</p>
                <p>评分：{{ movie.rate }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
//从vue中导入ref和onMounted
import {ref,onMounted} from 'vue'
//导入getMovieList()方法，用于从API获取电影列表
import { getMovieList } from '@/api/movie'

//定义响应式变量movies,用于存储电影列表数据
const movies = ref([])

//定义响应式变量loading，用于表示数据加载状态，初始值为true（加载中）
const loading = ref(true)

//定义一个异步函数fetchMovies(),用于获取电影列表数据
const fetchMovies = async () =>{
    try {
        //调用API获取电影列表
        const res = await getMovieList()
        //将获取到的数据存入movies变量
        movies.value = res.data
    }catch(error){
        //如果请求失败，输出错误信息到控制台
        console.error('获取电影列表失败：',error)
    }finally{
        //无论请求成功或失败，都将loading状态设置为false
        loading.value = false
    }
}

// ✅ 关键：处理本地图片路径
const getImageUrl = (url) => {
    if (!url) return ''

    // 处理本地 @/assets/ 路径
    if (url.startsWith('@/assets/')) {
        // 关键：把 @/assets/ 替换成 src/assets/，再用 import.meta.url 解析
        const realPath = url.replace('@/assets/', '../assets/')
        const fullUrl = new URL(realPath, import.meta.url).href
        return fullUrl
    }
    // 网络图片直接返回
    return url
}


//使用onMounted生命周期钩子，在组件挂载时调用fetchMovies()函数
onMounted (() => {
    fetchMovies()
})
</script>