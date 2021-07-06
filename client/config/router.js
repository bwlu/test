import Router from 'vue-router'

import routes from './routers'

export default () => {
	return new Router({
		routes,
		mode: 'history',
		linkActiveClass: 'active-link',
		linkExactActiveClass: 'exact-active-link',
		scollBehavior(to, form, savePosition){
			// 路由跳转时，是否滚动，返回要滚动的位置
			if(savePosition){
				return {x: 0, y: 0}
			} else{
				return {x: 0, y: 0}
			}
		},
		fallback: true,
		// 将url?后的参数转换成json对象
		parseQuery(query){
			
		},
		// 参数对象转换成字符串
		stringifQuery(obj){
			
		}
	})
}