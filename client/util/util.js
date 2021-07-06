import axios from 'axios'
import Qs from 'qs';
import _tool from 'util/tools'

const requestPromise = (param) => {
  let baseUrl = 'http://localhost:8000';
  if (param.url) param.url = `${baseUrl}${param.url}`;
  if (param.data) {
    param.data.token = _tool.readToken();
    if(param.manage) param.data.manage = true
  } else{
    param.data = {token: _tool.readToken()}
    if(param.manage) param.data.manage = true
  } 
  return new Promise((resolve, reject) => {
    let loading = layer.load(0)
    $.ajax({
      type: param.type || 'get',
      url: param.url || '',
      headers: {
        // 'x-user-token': _tool.readToken()
      },
      dataType: param.dataType || 'json',
      data: param.data || null,
      success: res => {
        layer.close(loading)
        // console.log(res)
        if (0 === res.code) {
          typeof resolve === 'function' && resolve(res.data);
        } else if (-1 === res.code) {
          reject('请先登录');
          _tool.toLogin();
        } else if (-9 === res.code) {
          
        } else {
          if (!res.msg) {
            if (-5 === res.code) {
              res.msg = '没有权限访问';
            } else if (-6 === res.code) {
              res.msg = '当前访问对象不存在';
            } else if (-4 === res.code) {
              res.msg = '用户已被禁用';
            } else if (-8 === res.code) {
              res.msg = '无效值';
            }
            console.log(param.url);
          }
          typeof reject === 'function' && reject(res.msg || `错误 code:${res.code}`);
        }
      },
      error: err => {
        layer.close(loading)
        console.log('err:', err)
        console.log('err:', err.statusText)
        let msg = '服务器错误，请检查您的链接'
        if(err.status === 404){
          msg = '找不到链接'
        } else if(err.status === 401){
          msg = '未认证'
        } else if(err.status === 405){
          msg = '不允许的方法'
        } else if(err.status === 500){
          msg = '服务器错误'
        } 
        typeof reject === 'function' && reject(msg);
      },
    });
  });
}
const requestTimeout = (ms) => {
  let timeoutMsg = '响应超时';
  return new Promise((resolve, reject) => {
    setTimeout(function() {
      reject(timeoutMsg)
    }, ms)
  })
}

export const handleRequest = (param) => {
  return Promise.race([
    requestPromise(param),
    requestTimeout(30000) // 10秒超时
  ])
}
