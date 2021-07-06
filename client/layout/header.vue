<template>
	<header class="main-header">
		<h2 class="mel-h2">element-ui Example</h2>
		<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
		  <el-menu-item index="1">导航1</el-menu-item>
		  <el-submenu index="2">
		    <template slot="title">多级导航</template>
		    <el-menu-item index="2-1">子导航1</el-menu-item>
		    <el-menu-item index="2-2">子导航2</el-menu-item>
		    <el-menu-item index="2-3">子导航3</el-menu-item>
		    <el-submenu index="2-4">
		      <template slot="title">子导航4</template>
		      <el-menu-item index="2-4-1">子导航41</el-menu-item>
		      <el-menu-item index="2-4-2">子导航42</el-menu-item>
		      <el-menu-item index="2-4-3">子导航43</el-menu-item>
		    </el-submenu>
		  </el-submenu>
		  <el-menu-item index="3" disabled>导航2</el-menu-item>
		  <el-menu-item index="4"><router-link to="/login/">导航3</router-link></el-menu-item>
		</el-menu>
		<div class="line"></div>
		<el-menu
		  :default-active="activeIndex2"
		  class="el-menu-demo"
		  mode="horizontal"
		  @select="handleSelect"
		  background-color="#545c64"
		  text-color="#fff"
		  active-text-color="#ffd04b">
		  <el-menu-item index="1">导航1</el-menu-item>
		  <el-submenu index="2">
		    <template slot="title">多级导航</template>
		    <el-menu-item index="2-1">子导航1</el-menu-item>
		    <el-menu-item index="2-2">子导航2</el-menu-item>
		    <el-menu-item index="2-3">子导航3</el-menu-item>
		    <el-submenu index="2-4">
		      <template slot="title">子导航4</template>
		      <el-menu-item index="2-4-1">子导航41</el-menu-item>
		      <el-menu-item index="2-4-2">子导航42</el-menu-item>
		      <el-menu-item index="2-4-3">子导航43</el-menu-item>
		    </el-submenu>
		  </el-submenu>
		  <el-menu-item index="3" disabled>导航2</el-menu-item>
		  <el-menu-item index="4"><router-link to="/login/">导航3</router-link></el-menu-item>
		</el-menu>
	</header>
</template>

<script>
import {
	mapState,
	mapGetters,
	mapMutations
} from 'vuex'

export default {
	components: {
		
	},
	data(){
		return {
			activeIndex: '1',
			activeIndex2: '1'
		}
	},
	mounted(){
		
	},
	computed: {
		
	},
	methods: {
		handleSelect(key, keyPath) {
			console.log(key, keyPath);
		}
	}
}
</script>

<style>
.main-header{
	padding-top: 10px;
}
.mel-h2{
	color: white;
}
</style>
