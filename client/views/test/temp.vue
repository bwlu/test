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
      const h = this.$createElement;
      let vueIns = new Vue({
        data: () => {
          return {
            startTime: '',
            endTime: '',
            sections: [
              {name: '日', value: 0},
              {name: '月', value: 1},
              {name: '周', value: 2}
            ], // 切片大小
            section: '', // 当前切片
            tasks: [1,2,3,4,5], // 任务列表
            task: '', // 当前任务
            condition: {}, // 条件
          };
        },
        methods: {
          // 生成切片下拉列表
          generateSection(){
            let that = this
            let sectionDiv = new Vue({
              render: function(h){
                return h('el-select', {
                  props: {
                    placeholder: '请选择',
                    value: that.section,
                  },
                  style: { width: '70%' },
                  on: {
                    change: function(value){
                      if(that.section !== value){
                        that.section = value
                        // 加载时间控件
                        that.generateTime()
                      }
                    },
                  }
                }, 
                that.sections.map(function (item) {
                  return h('el-option', {
                    props: {
                      label: item.name,
                      value: item.value
                    }
                  })
                })
                )
              }
            })
            $('#sectionDiv').html(sectionDiv.$mount().$el)
          },
          // 生成时间控件
          generateTime(){
            let that = this
            let rangeType = ['daterange', 'monthrange', 'daterange']
            let timeScope = new Vue({
              render: function(h){
                return h('el-date-picker', {
                  style: { width: '70%' },
                  props: {
                    'type': rangeType[that.section || 0],
                    'range-separator': "至",
                    'start-placeholder': "开始日期",
                    'end-placeholder': "结束日期",
                    'value-format': that.section == 1?'yyyy-MM':'yyyy-MM-dd',
                    'value': [that.startTime, that.endTime],
                    'picker-options': {
                        disabledDate(time) {
                          if(that.section == 2){
                            return time.getDay() !== 1
                          } else{
                            return false
                          }
                        },
                        'firstDayOfWeek': 1
                    }
                  },
                  on: {
                    input: function(value){
                      if(value){
                        let [start, end] = value
                        that.startTime = start
                        that.endTime = end
                      } else{
                        that.startTime = ''
                        that.endTime = ''
                      }
                    },
                  }
                })
              },
            })
            $('#timeDiv').html(timeScope.$mount().$el)
          },
          // 生成任务列表
          generateTask(){
            let that = this
            // 没有数据时显示空
            let taskContent = [h('el-empty', {props: {'image-size': "50", 'description': '没有数据'}})]
            if(this.tasks.length){
              taskContent = this.tasks.map(function (item) {
                return h('div', {
                  attrs: {
                    'data-key': item
                  },
                  style: {'padding': '0 20px'},
                  on: {
                    click: function(event){
                      let brothers = $(event.target).siblings()
                      brothers.map(function(item){
                        $(brothers[item]).css('background-color', '#fff')
                      })
                      $(event.target).css('background-color', '#eee')
                      console.log(event.currentTarget.dataset.key)
                      let clist = [{
                        showname: "线路",
                        storename: "line",
                        type: "combobox",
                        isMult: true,
                        url: "http://......"
                      }, {
                        showname: "明细",
                        storename: "details",
                        type: "textbox"
                      	},
                      ]
                      clist.map(function(cond){
                        that.$set(that.condition, cond.storename, '')
                      })
                      that.generateCondition(clist)
                    }
                  }
                }, item)
              })
            }
            return h('el-card',{
              props: {
                'shadow': 'never',
                'body-style': {
                  'height': '200px',
                  'overflow': 'auto',
                  'line-height': '30px',
                  'padding': '10px 0'
                }
              },
              style: { width: '70%' },
            },
              taskContent
            )
          },
          // 动态条件
          generateCondition(condList){
            let that = this
            let condition = new Vue({
              render: function(h){
                return h('el-form', {}, 
                  condList.map(function(cond){
                    if(cond.type === 'combobox'){
                      return h('el-form-item', {
                        props: { label: cond.showname },
                      }, [
                        h('el-select', {
                          props: {
                            placeholder: '请选择',
                            value: that.condition[cond.storename],
                            multiple: cond.isMult
                          },
                          style: { width: '70%' },
                          on: {
                            change: function(value){
                              that.$set(that.condition, cond.storename, value)
                            }
                          }
                        }, [
                          h('el-option', {
                            props: {
                              label: '1701',
                              value: 0
                            }
                          }),
                          h('el-option', {
                            props: {
                              label: '1702',
                              value: 2
                            }
                          })
                        ])
                      ])
                    } else if(cond.type === 'textbox'){
                      return h('el-form-item', {
                        props: { label: cond.showname },
                      }, [
                        h('el-input', {
                          props: {
                            placeholder: '请输入',
                            value: that.condition[cond.storename],
                          },
                          style: { width: '70%' },
                          on: {
                            input: function(value){
                              that.$set(that.condition, cond.storename, value)
                            }
                          }
                        })
                      ])
                    }
                  })
                )
              },
            }).$mount()
            $('#conditionDiv').html(condition.$el)
          },
          vaildFormItem(e, v, msg='请输入'){
            let vaild = (typeof v === 'string' && v) || v.length !== 0
            if(vaild){
              if($(e).next() && $(e).next().attr('class')==='el-form-item__error'){
                $(e).next().remove()
              }
            } else{
              if($(e).next() && $(e).next().attr('class')==='el-form-item__error'){
                
              } else{
                $(e).after('<div class="el-form-item__error">'+msg+'</div>')
              }
            }
          }
        }
      });
      let options = {
        title: '创建任务',
        customClass: 'task-msgbox',
        message: h('el-row', {}, [
          h('el-col', {
            props: {
              span: 12
            }
          }, [
            h('el-form', {}, [
              h('el-form-item', {
                props: { label: '时间范围' },
              }, [
                h('div', {
                  attrs: { id: 'timeDiv' },
                }),
              ]),
              h('el-form-item', {
                props: {
                  label: '切片大小'
                }
              }, [h('div', {
                  attrs: { id: 'sectionDiv' },
                })]),
              h('el-form-item', {
                props: {
                  label: '选择任务'
                },
              }, [vueIns.generateTask()]),
            ])
          ]),
          h('el-col', {
            props: { span: 12 }
          }, [
            h('h1', {style: {'margin-bottom': '10px'}}, '其他条件'),
            h('div', {
              attrs: {
                id: 'conditionDiv'
              }
            }, '请选择左侧任务')
          ]),
        ]),
        showCancelButton: true,
        confirmButtonText: '创建',
        cancelButtonText: '取消',
        beforeClose: (action, instance, done) => {
          if (action === 'confirm') {
            instance.confirmButtonLoading = true;
            instance.confirmButtonText = '执行中...';
            setTimeout(() => {
              done();
              instance.confirmButtonLoading = false;
              this.$message({
                type: 'success',
                message: '成功'
              });
            }, 1000);
          } else {
            $('#conditionDiv').html('')
            $('.task-div').css('background-color', '#fff')
            console.log(vueIns.$data)
            done();
          }
        }
      };
      this.$msgbox(options)
      .then(action => {})
      .catch(action => {});
      this.$nextTick(function(){
        vueIns.generateSection()
        vueIns.generateTime()
      })
      
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
