import axios from "axios"

//创建一个axios实例，用于配置全局请求的默认设置
const request = axios.create({
    baseURL:'http://localhost:8000/api',
    timeout:5000
})

//请求拦截器，在请求发送前对请求数据进行处理
request.interceptors.request.use(
    config => {
        //如果请求方法是GET，并且存在参数
        if(config.method === 'get' && config.params){
            //遍历GET请求的参数对象
            Object.keys(config.params).forEach(key => {
                //如果某个参数的值是undefined,则删除该参数
                if (config.params[key] === undefined){
                    delete config.params[key]
                }
            })
        }
        //返回修改后的请求配置
        return config
    }
)

//响应拦截器，用于处理服务器响应
request.interceptors.response.use(
    //如果响应成功，直接返回响应的data部分
    response => response.data,
    //如果响应失败，返回一个拒绝的Promise对象，便于调用方处理错误
    error => Promise.reject(error)
)

//导出axios实例，供其他模块使用
export default request