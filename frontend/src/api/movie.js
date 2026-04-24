import request from "./request";

export function getMovieList(){
    return request({
        url:'/movies/',
        method:'get'
    })
}