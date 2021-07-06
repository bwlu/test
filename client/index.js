import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import App from './app.vue'

// import 'assets/styles/bootstrap.min.css'
// import 'assets/styles/global.css'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import createRouter from 'config/router'
import createStore from './store/store'
import Notification from './components/notification'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(Vuex)
Vue.use(Notification)

const router = createRouter()
const store = createStore()

/** 路由守卫 路由钩子 **/
// 路由跳转前  // 例子:登录拦截
router.beforeEach((to, from, next) => {
  $("html,body").animate({
    scrollTop: 0
  }, 500);
	// console.log('before each invoked');
  // document.body.scrollTop = document.documentElement.scrollTop = 0
	next()
	// if(to.fullPath === '/app'){
	// 	next('/login')
	// 	// next({path: '/', replace: ''}) // 和route一样
	// } else{
	// 	next()
	// }
})

// router.beforeResolve((to, from, next) => {
// 	console.log('before resolve invoked');
// 	next()
// })
// 导航跳转后
// router.afterEach((to, from) => {
// 	console.log('after each invoked');
// })

// 引入公共过滤器
import vueFilter from 'util/filters'
for (let key in vueFilter){ 
    Vue.filter(key,vueFilter[key]) 
}

new Vue({
	router,
	store,
	render: (h) => h(App)
}).$mount('#root')