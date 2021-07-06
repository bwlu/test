export default {
	BASEURL: 'http://localhost:8000',
  FSTOKEN: 'fs-user-token',
  FSUSER: 'fs-user-info',
  FSMTOKEN: 'fsm-user-token',
  FSMUSER: 'fsm-user-info',
  COLORS: [''],
	successTodo(msg, todo){
		layer.msg(msg, {
			anim: 0,
      icon: 6,
			time: 1200,
		}, todo);
	},
	successTips(msg){
    if(!msg) msg = '操作成功'
    else if(typeof msg === 'object') msg = '操作成功'
		layer.msg(msg, {
			anim: 0,
			icon: 6
		});
	},
	warnTips(msg){
		layer.msg(msg, {
			anim: 0,
      icon: 7
		});
	},
	errorTodo(msg, todo){
		layer.msg(msg, {
			anim: 0,
      icon: 5,
			time: 1200,
		}, todo);
	},
	errorTips(msg){
		layer.msg(msg, {
			anim: 0,
      icon: 5
		});
	},
  tips(content, target, location=2, bgColor='#000'){
    layer.tips(content, target, {
      tips: [location, bgColor] //还可配置颜色
    });
  },
	confirmTips({msg, btnSuccess='确认', btnCancel='取消', success=()=>{}, cancel=()=>{}}, area='auto', skin=''){
		layer.confirm(msg, {
			time: 0, //不自动关闭
			area: area,
			skin: skin,
			btn: [btnSuccess, btnCancel],
			yes: success,
			btn2: cancel,
		});
	},
	// formType=1 密码输入
	promptTips(title, success, type = 0){
		layer.prompt({
		  formType: type,
		  title: title,
		}, (value, index) => {
		  success(value)
		  layer.close(index);
		});
	},
	getUrlParam(name){
		//username=admin&password=123456
		let queryString = window.location.search.substring(1) || '',
			reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"),
			result = queryString.match(reg);
		//result:['param=123', '', 'admin', &']
		return result ? decodeURIComponent(result[2]) : null;
	},
	setLocalStorage(name, data){
		let dataType = typeof data;
		if(dataType ===  'object'){
			window.localStorage.setItem(name, JSON.stringify(data));
		} else if(['number', 'string', 'boolean'].indexOf(dataType)>=0){
			layer.msg('该类型不能用于本地存储');
		}
	},
	getLocalStorage(name){
		let data = window.localStorage.getItem(name);
		if(data){
			return JSON.parse(data);
		} else{
			return '';
		}
	},
	removeLocalStorage(name){
		window.localStorage.removeItem(name);
	},
	saveToken(token) {
		localStorage.setItem(this.FSTOKEN, token);
	},
	readToken() {
		return localStorage.getItem(this.FSTOKEN);
	},
	removeToken() {
		return localStorage.removeItem(this.FSTOKEN);
	},
  saveUserInfo(userInfo) {
  	localStorage.setItem(this.FSUSER, JSON.stringify(userInfo));
  },
  readUserInfo() {
  	return JSON.parse(localStorage.getItem(this.FSUSER));
  },
  removeUserInfo() {
  	return localStorage.removeItem(this.FSUSER);
  },
  saveMToken(token) {
  	localStorage.setItem(this.FSMTOKEN, token);
  },
  readMToken() {
  	return localStorage.getItem(this.FSMTOKEN);
  },
  removeMToken() {
  	return localStorage.removeItem(this.FSMTOKEN);
  },
  saveMUserInfo(userInfo) {
  	localStorage.setItem(this.FSMUSER, JSON.stringify(userInfo));
  },
  readMUserInfo() {
  	return JSON.parse(localStorage.getItem(this.FSMUSER));
  },
  removeMUserInfo() {
  	return localStorage.removeItem(this.FSMUSER);
  },
	toLogin(){
		window.location.href = '/login/';
	}
}