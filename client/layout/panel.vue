<template>
	<div id="home">
		<Header></Header>
		<div class="row">
			<div class="col-md-12">
				<div>
					<transition name="fade" mode="out-in">
						<router-view />
					</transition>
				</div>
			</div>
		</div>
		<Footer></Footer>
	</div>
</template>

<script>
import {
	mapState,
	mapGetters,
	// mapActions,
	// mapMutations
} from 'vuex'
import Header from 'layout/header.vue'
import Footer from 'layout/footer.vue'

export default {
	components: {
		Header,
		Footer
	},
	updated() {
		
	},
	mounted() {
		
	},
	computed: {
		...mapState(['count']),
	},
	methods: {
		notify() {
			this.$notify({
				content: 'test $notify',
				btn: 'close'
			})
		}
	}
}
</script>

<style>
#home{
	background-image: url(../assets/images/bg.jpg);
	background-repeat: no-repeat;
	background-size: cover;
	background-position:center;
	position: absolute;
	top: 0;
	bottom: 0;
	left: 0;
	right: 0;
}
</style>
