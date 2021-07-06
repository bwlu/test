<template>
	<div id="app">
		<div id="cover"></div>
		<transition name="fade" mode="out-in">
			<router-view />
		</transition>
	</div>
</template>

<script>
import {
	mapState,
	mapGetters,
	// mapActions,
	// mapMutations
} from 'vuex'

export default {
	components: {
		
	},
	mounted(){
		
	},
	computed: {
		...mapState(['count']),
		...mapGetters({
			'fullName': 'fullName'
		})
	},
	methods: {
		
	}
}
</script>

<style>

</style>
