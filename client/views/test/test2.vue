<template>
  <div class="mcontains">
    <p class="mcontent" @click="handleClick">test</p>
  </div>
</template>
<script>
import Vue from 'vue';

export default {
  data() {
    return {};
  },
  mounted() {
    let style = $('<style>.task-msgbox { width: 80%; }</style>')
    $('html > head').append(style);
  },
  methods: {
    handleClick() {
      let data = [
        {date: '2021-09-20', name: 'hahah', label: 'ewrewr'},
        {date: '2021-09-20', name: 'hahah', label: 'ewrewr'},
        {date: '2021-09-20', name: 'hahah', label: 'ewrewr'},
        {date: '2021-09-20', name: 'hahah', label: 'ewrewr'},
        {date: '2021-09-20', name: 'hahah', label: 'ewrewr'},
      ]
      const h = this.$createElement;
      let options = {
        title: '任务日志',
        customClass: 'task-msgbox',
        message: h('el-table', {
          props: {
            data: data,
            stripe: ''
          }
        }, [
          h('el-table-column', {
            props: {
              prop: 'date',
              label: '日期'
            }
          }),
          h('el-table-column', {
            props: {
              prop: 'name',
              label: '姓名'
            }
          }),
          h('el-table-column', {
            props: {
              prop: 'label',
              label: '标签'
            }
          }),
        ]),
        showCancelButton: true,
        showConfirmButton: false,
        cancelButtonText: '关闭',
        beforeClose: (action, instance, done) => {
          done();
        }
      };
      this.$msgbox(options)
      .then(action => {})
      .catch(action => {});
    }
  }
};
</script>
<style>
div.mcontains {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
p.mcontent {
  font-size: 5em;
}

</style>
