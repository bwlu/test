<template>
  <div class="container">
    <div id="imgDiv"></div>
    <canvas id="myCanvas" width="200" height="200"></canvas>
    <canvas width="500" height="500" id="canvas"></canvas>
  </div>
</template>
<script>
export default{
  data() {
    return {
      
    };
  },
  mounted() {
    // this.test1()
    var canvas = new Canvas(document.getElementById('canvas'))
    	canvas.createBlock({					// 红色
    		x: 100,
    		y: 100,
    		w: 100,
    		h: 100,
    		color: '#f00'
    	})
    	canvas.createBlock({					// 蓝色
    		x: 100,
    		y: 100,
    		w: 300,
    		h: 100,
    		color: '#00f'
    	})
  },
  methods: {
    test(e){
      var img = document.getElementById('img');
      // 创建 Image对象
      var imgObj = new Image();
      // 为 src 属性赋值
      imgObj.src = "./static/map.png";
      // 将 Image对象插入到 img元素中
      img.appendChild(imgObj);
      // 当 imgObj 加载完毕后触发事件
      imgObj.onload = function () {
          // 控制台打印 Image对象的 宽 和 高
          console.log(imgObj.width + "----" + imgObj.height);
      };
      imgObj.onclick = function (e, a) {
          console.log(e);
          console.log(a);
      };
    },
    test1(){
      var c=document.getElementById("myCanvas");
      var ctx=c.getContext("2d");
      var imgObj = new Image();
      imgObj.src = "./static/map.png";
      imgObj.onload = function () {
          ctx.drawImage(imgObj,10,10);
          c.addEventListener("mousedown",function(){
            console.log(123)
          },false);
      };
    }
  }
}
class Canvas {
  blockList = []
  ctx = null
  canvas = null
  nowBlock = null
  createBlock (option) {
    option.hierarchy = this.blockList.length
    option.Canvas = this
    this.blockList.push(new Block(option))
    this.painting()
  }
  rendering (block) {
    this.ctx.fillStyle = block.color
    this.ctx.fillRect(block.x, block.y, block.w, block.h)
  }
  painting () {
    // 清空画布
    this.ctx.fillStyle = '#fff'
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
    this.blockList.forEach(ele => {
      this.rendering(ele)
    })
  }
  mousedownEvent (e) {					// 点击事件
    const x = e.offsetX
    const y = e.offsetY
    // 获取点中里层级最高的色块
    this.nowBlock = (this.blockList.filter(ele => ele.checkBoundary(x, y))).pop()
    // 如果没有捕获的色块直接退出
		if (!this.nowBlock) return
    // 将点击到的色块层级提高到最高
    this.nowBlock.hierarchy = this.blockList.length
    // 重新排序(从小到大)
    this.blockList.sort((a, b) => a.hierarchy - b.hierarchy)
    // 在重新从0开始分配层级
    this.blockList.forEach((ele, idx) => ele.hierarchy = idx)
    // 重新倒序排序后再重新渲染。
    this.painting()
    this.nowBlock.mousedownEvent(e)
    // this.blockList.forEach(ele => {
    //   if (ele.checkBoundary(x, y)) ele.clickEvent(e)
    // })
  }
  constructor (ele) {
    this.canvas = ele
    this.ctx = this.canvas.getContext('2d')
    this.blockList = []
    // 事件绑定
    this.canvas.addEventListener('mousedown', this.mousedownEvent.bind(this))
  }
}
class Block {
  w = 0
  h = 0
  x = 0
  y = 0
  color = ''
  Canvas = null
  hierarchy = 0
  constructor ({ w, h, x, y, color, Canvas, hierarchy }) {
    this.w = w
    this.h = h
    this.x = x
    this.y = y
    this.color = color
    this.Canvas = Canvas
    this.hierarchy = hierarchy
  }
  checkBoundary (x, y) {
    return x > this.x && x < (this.x + this.w) && y > this.y && y < (this.y + this.h)
  }
  mousedownEvent (e) {
    const disX = e.offsetX - this.x
    const disY = e.offsetY - this.y
    document.onmousemove = (mouseEvent) => {
      this.x = mouseEvent.offsetX - disX
      this.y = mouseEvent.offsetY - disY
      this.Canvas.painting()
    }
    document.onmouseup = () => {
      document.onmousemove = document.onmousedown = null
    }
  }
}
class Canvas1 {
  blockList = []
  ctx = null
  canvas = null
  nowBlock = null
  createBlock (option) {
    option.hierarchy = this.blockList.length
    option.Canvas = this
    this.blockList.push(new Block(option))
    this.painting()
  }
  rendering (block) {
    this.ctx.fillStyle = block.color
    this.ctx.fillRect(block.x, block.y, block.w, block.h)
  }
  painting () {
    // 清空画布
    this.ctx.fillStyle = '#fff'
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height)
    this.blockList.forEach(ele => {
      this.rendering(ele)
    })
  }
  mousedownEvent (e) {					// 点击事件
    const x = e.offsetX
    const y = e.offsetY
    // 获取点中里层级最高的色块
    this.nowBlock = (this.blockList.filter(ele => ele.checkBoundary(x, y))).pop()
    // 如果没有捕获的色块直接退出
		if (!this.nowBlock) return
    // 将点击到的色块层级提高到最高
    this.nowBlock.hierarchy = this.blockList.length
    // 重新排序(从小到大)
    this.blockList.sort((a, b) => a.hierarchy - b.hierarchy)
    // 在重新从0开始分配层级
    this.blockList.forEach((ele, idx) => ele.hierarchy = idx)
    // 重新倒序排序后再重新渲染。
    this.painting()
    this.nowBlock.mousedownEvent(e)
    // this.blockList.forEach(ele => {
    //   if (ele.checkBoundary(x, y)) ele.clickEvent(e)
    // })
  }
  constructor (ele) {
    this.canvas = ele
    this.ctx = this.canvas.getContext('2d')
    this.blockList = []
    // 事件绑定
    this.canvas.addEventListener('mousedown', this.mousedownEvent.bind(this))
  }
}
class Block1 {
  w = 0
  h = 0
  x = 0
  y = 0
  color = ''
  Canvas = null
  hierarchy = 0
  constructor ({ w, h, x, y, color, Canvas, hierarchy }) {
    this.w = w
    this.h = h
    this.x = x
    this.y = y
    this.color = color
    this.Canvas = Canvas
    this.hierarchy = hierarchy
  }
  checkBoundary (x, y) {
    return x > this.x && x < (this.x + this.w) && y > this.y && y < (this.y + this.h)
  }
  mousedownEvent (e) {
    const disX = e.offsetX - this.x
    const disY = e.offsetY - this.y
    document.onmousemove = (mouseEvent) => {
      this.x = mouseEvent.offsetX - disX
      this.y = mouseEvent.offsetY - disY
      this.Canvas.painting()
    }
    document.onmouseup = () => {
      document.onmousemove = document.onmousedown = null
    }
  }
}
</script>
<style>
.container{
  width: 500px;
  height: 500px;
}
.container img{
  width: 100%;
  height: auto;
}
#myCanvas{
  border: 1px solid red;
}
</style>