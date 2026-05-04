import axios from "axios";


const request = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  timeout: 5000,
})

// 请求拦截器
request.interceptors.request.use((config) => {
  // 每次发请求自动执行
  // 可以在这里统一带 token、请求头
  return config
})

// 响应拦截器
request.interceptors.response.use(
  (res) => {
    // 统一只返回后端真正的数据，不用每次写 res.data
    return res.data
  },
  (err) => {
    // 统一处理报错：弹窗提示、401跳登录页等
    return Promise.reject(err)
  },
)

export default request;
