<template>
	<transition name="fade" @after-leave="afterLeave" @after-enter="afterEnter">
		<div class="notification-notify" :style="style" v-show="visible" @mouseenter="clearTimer" @mouseleave="createTimer">
			<span class="content-notify">{{content}}</span>
			<a class="btn-notify" @click="handleClose" href="javascript:viod(0)">{{btn}}</a>
		</div>
	</transition>
</template>

<script>
export default {
	name: 'Notification',
	props: {
		content: {
			type: String,
			required: true
		},
		btn: {
			type: String,
			default: '关闭'
		}
	},
	data() {
		return {
			visible: true
		}
	},
	computed: {
		style() {
			return {}
		}
	},
	methods: {
		handleClose(e) {
			e.preventDefault()
			this.$emit('close')
		},
		afterLeave() {
			this.$emit('closed')
		},
		afterEnter() {},
		clearTimer() {},
		createTimer() {}
	}
}
</script>

<style>
.notification-notify {
	display: inline-flex;
	background-color: #303030;
	color: rgba(255, 255, 255, 1);
	align-items: center;
	padding: 20px;
	min-width: 280px;
	box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2), 0px 6px 10px 0px rgba(0, 0, 0, 0.14), 0px 1px 18px 0px rgba(0, 0, 0, 0.12);
	flex-wrap: wrap;
	transition: all .3s;
}

.content-notify {
	padding: 0;
}

.btn-notify {
	color: #ff4081;
	padding-left: 24px;
	margin-left: auto;
	cursor: pointer;
}
.btn-notify:hover {
	color: #ff4081;
}
</style>
