<template>
	<div id="footer">
	  <span>Written by {{this.author}}</span>
	</div>
</template>

<script>
export default {
	data(){
		return {
			author: 'bwlu'
		}
	}
}
</script>

<style>
#footer{
	width: 100%;
	position: absolute;
	bottom: 0;
	text-align: center;
}
</style>
