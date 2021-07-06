import Vue from "vue"
// 因为我这里要使用vue中公共的方法$getUserAgent，所以引入vue并实例化 不需要的可不必引入
let $vue = new Vue

// 公共过滤器 某某币 ——> 人民币
const vFilter = {
  dateFilter: function (value) {
    if (!value) return ''
    if(value.indexOf('/')!==-1){
      value = value.split('/')
    } else if(value.indexOf('-')!==-1){
      value = value.split('-')
    }
    if(typeof value === 'string') return value
    if(value[0]<2020) value[0] = '2020'
    return value.join('-')
  }
}

export default vFilter
