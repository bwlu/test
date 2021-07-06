<template>
	<div>
		<canvas width="120" height="48" id="c1" @click="draw" />
		<p>点击刷新验证码</p>
	</div>
</template>
<script>
export default {
	name: 'Verifycode',
	props: {},
	data() {
		return{
			verify: ''
		}
	},
	computed: {
		
	},
	mounted(){
		this.draw();
	},
	methods: {
		//1.新建一个函数产生随机数
		rn(min,max) {
			return parseInt(Math.random()*(max-min)+min);
		},
		//2.新建一个函数产生随机颜色
		rc(min,max) {
			let r=this.rn(min,max);
			let g=this.rn(min,max);
			let b=this.rn(min,max);
			return `rgb(${r},${g},${b})`;
		},
		draw() {
			//3.填充背景颜色,颜色要浅一点
			let w=120;
			let h=48;
			let ctx=c1.getContext("2d");
			ctx.fillStyle=this.rc(180,230);
			ctx.fillRect(0,0,w,h);
			
			//4.随机产生字符串
			let verify = ''
			let pool="ABCDEFGHIJKLIMNOPQRSTUVWSYZ1234567890";
			for(let i=0;i<4;i++){
				let c=pool[this.rn(0,pool.length)];//随机的字
				verify += c;
				let fs=this.rn(18,40);//字体的大小
				let deg=this.rn(-30,30);//字体的旋转角度
				ctx.font=fs+'px Simhei';
				ctx.textBaseline="top";
				ctx.fillStyle=this.rc(80,150);
				ctx.save();
				ctx.translate(30*i+15,15);
				ctx.rotate(deg*Math.PI/180);
				ctx.fillText(c,-15+5,-15);
				ctx.restore();
			}
			this.verify = verify;
			this.$emit('onVerify', this.verify);
			//5.随机产生5条干扰线,干扰线的颜色要浅一点
			for(let i=0;i<5;i++){
				ctx.beginPath();
				ctx.moveTo(this.rn(0,w),this.rn(0,h));
				ctx.lineTo(this.rn(0,w),this.rn(0,h));
				ctx.strokeStyle=this.rc(180,230);
				ctx.closePath();
				ctx.stroke();
			}
			//6.随机产生40个干扰的小点
			for(let i=0;i<40;i++){
				ctx.beginPath();
				ctx.arc(this.rn(0,w),this.rn(0,h),1,0,2*Math.PI);
				ctx.closePath();
				ctx.fillStyle=this.rc(150,200);
				ctx.fill();
			}
		}
	}
}
</script>
<style>

</style>

