<template>
	<div class="content-row" v-if="totalCount > pageSize">
		<div class="col-md-12">
			<nav aria-label="Page navigation">
				<ul class="pagination justify-content-center">
					<li :class="{'page-item': true, 'disabled': pageNumber == 1}" @click="toHead">
						<a class="page-link" href="javascript:void(0);" aria-label="Previous">
							<span aria-hidden="true">首页</span>
						</a>
					</li>
					<li :class="{'page-item': true, 'disabled': pageNumber == 1}" @click="previous">
						<a class="page-link" href="javascript:void(0);" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						</a>
					</li>
					<li :class="{'page-item': true, 'active': pageNumber == page}" v-for="page in pageList" @click="changeNumber(page)">
						<a class="page-link" href="javascript:void(0);">{{page}}</a>
					</li>
					<li :class="{'page-item': true, 'disabled': pageNumber == pageMax || pageMax === 0}" @click="next">
						<a class="page-link" href="javascript:void(0);" aria-label="Previous">
							<span aria-hidden="true">&raquo;</span>
						</a>
					</li>
					<li :class="{'page-item': true, 'disabled': pageNumber == pageMax || pageMax === 0}" @click="toTail">
						<a class="page-link" href="javascript:void(0);" aria-label="Previous">
							<span aria-hidden="true">尾页</span>
						</a>
					</li>
					<li class="page-item disabled">
						<a class="page-link" href="javascript:void(0);" aria-label="Previous">
							共{{pageMax}}页
						</a>
					</li>
					<li class="page-item">
						<div class="input-group input-group-default mb-3 jump-page">
						  <input type="text" class="" v-model="pageJump" @focus="selectAll">
						  <a class="page-link" href="javascript:void(0);" aria-label="Previous" @click="jump">
						  	跳转
						  </a>
						</div>
					</li>
				</ul>
			</nav>
		</div>
	</div>
</template>

<script>
export default {
	components: {
		
	},
	props: {
		totalCount: {
			type: Number,
			required: true
		},
		pageNumber: {
			type: Number,
			required: true
		},
		pageSize: {
			type: Number,
			required: false,
			default: 10
		},
	},
	watch: {
		pageNumber(newValue, oldValue) {
			this.changeNumber(newValue);
			return newValue;
		},
		totalCount(newValue, oldValue) {
			this.init();
			return newValue;
		},
	},
	data(){
		return {
			pageList: [],
			pageMax: 0,
			pageJump: ''
		}
	},
	update(){
		
	},
	beforeMount(){
		
	},
	mounted() {
		this.init();
	},
	computed: {
		
	},
	methods: {
		// 获取焦点时全选
		selectAll(event){event.currentTarget.select()},
		init(){
			let pagefinal = this.totalCount/this.pageSize;
			pagefinal = pagefinal % 1 === 0 ? pagefinal : parseInt(pagefinal) + 1;
			this.pageMax = pagefinal;
			this.changeNumber(this.pageNumber);
		},
		changeNumber(pageNumber){
			let pagefinal = this.pageMax;
			let pageStart = pageNumber - 4, pageEnd = pageNumber + 4;
			pageStart = pageStart < 1 ? 1 : pageStart;
			pageEnd = pageEnd > pagefinal ? pagefinal : pageEnd;
			let pages = [];
			for(let i=pageStart;i<=pageEnd;i++) {
				pages.push(i);
			}
			this.pageList = pages;
			if(pageNumber === this.pageNumber) return;
			this.$emit('pageChange', pageNumber);
		},
		previous(){
			let pageNumber = this.pageNumber;
			if(pageNumber <= 1) return;
			pageNumber--;
			pageNumber = pageNumber < 1 ? 1 : pageNumber;
			this.$emit('pageChange', pageNumber);
		},
		next(){
			let pageNumber = this.pageNumber;
			if(this.pageMax !== 0 && pageNumber < this.pageMax){
				pageNumber++;
				pageNumber = pageNumber > this.pageMax ? this.pageMax : pageNumber;
				this.$emit('pageChange', pageNumber);
			}
		},
		toHead(){
			let pageNumber = this.pageNumber;
			if(pageNumber <= 1) return;
			this.$emit('pageChange', 1);
		},
		toTail(){
			let pageNumber = this.pageNumber;
			if(this.pageMax !== 0 && pageNumber < this.pageMax){
				this.$emit('pageChange', this.pageMax);
			}
		},
		jump(){
			if(this.pageJump === '' || isNaN(this.pageJump) || this.pageJump < 1 || this.pageJump > this.pageMax || this.pageNumber === parseInt(this.pageJump)) return
			this.$emit('pageChange', parseInt(this.pageJump));
		}
	}
}
</script>

<style>
.jump-page input{
	width: 60px;
	padding: .375rem .5rem;
	border: 1px solid #ced4da;
	border-radius: .25rem;
	margin-left: .75rem;
	margin-right: .1rem;
}
</style>
