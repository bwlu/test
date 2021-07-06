<template>
  <div class="mcontains">
    <el-row>
      <el-col :span="12">
        <el-form :model="ruleForm" ref="ruleForm" :rules="rules">
          <el-form-item label="日期范围" v-show="showDate">
            <el-date-picker style="width: 70%;"
              v-model="ruleForm.dateRange"
              :type="rangeType"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :value-format="valueFormat"
              :picker-options="pickerOptions">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="日期范围" v-show="!showDate">
            <el-date-picker style="width: 33%;"
              v-model="ruleForm.startYear"
              type="year"
              placeholder="开始年份"
              value-format="yyyy"
              :picker-options="pickerOptionsStartYear"
              @change="startYearchange">
            </el-date-picker>
            至
            <el-date-picker style="width: 33%;"
              v-model="ruleForm.endYear"
              type="year"
              placeholder="结束年份"
              value-format="yyyy"
              :picker-options="pickerOptionsEndYear"
              @change="endYearchange">
            </el-date-picker>
          </el-form-item>
          <el-form-item label="统计周期">
            <el-select v-model="ruleForm.section" clearable placeholder="请选择" style="width: 70%;"
              @change="sectionChange">
              <el-option
                v-for="item in sections"
                :key="item.value"
                :label="item.name"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="任务列表">
            <el-card shadow="never">
              <div v-for="item in 20"
                :key="item"
                :label="item"
                :value="item">{{item}}</div>
            </el-card>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :span="12">
        <h1 style="margin-bottom: 10px">其他条件</h1>
        <el-form>
          <el-form-item v-for="item in conditions"
            :key="item.storename"
            :label="item.showname">
            <el-select 
              v-if="item.type==='combobox'" 
              v-model="condition[item.storename]" 
              clearable 
              placeholder="请选择"
              style="width: 70%;">
              <el-option
                v-for="item in sections"
                :key="item.value"
                :label="item.name"
                :value="item.value">
              </el-option>
            </el-select>
            <el-input 
              v-else-if="item.type==='textbox'" 
              v-model="condition[item.storename]"
              style="width: 70%;"></el-input>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import Vue from 'vue';

export default {
  data() {
    return {
      ruleForm: {
        section: '', // 当前切片
        dateRange: [],
        startYear: '',
        endYear: ''
      },
      rules: {
        section: [
          { required: true, message: '请选择', trigger: 'blur' },
        ],
        timeRange: [
          { required: true, message: '请选择', trigger: 'blur' },
        ]
      },
      showDate: true,
      rangeType: 'daterange',
      valueFormat: 'yyyy-MM-dd',
      pickerOptions: {
        'firstDayOfWeek': 1
      },
      pickerOptionsStartYear: {
        disabledDate(time){
          return false
        }
      },
      pickerOptionsEndYear: {
        disabledDate(time){
          return false
        }
      },
      sections: [
        {name: '日', value: 0},
        {name: '周', value: 1},
        {name: '月', value: 2},
        {name: '年', value: 3},
      ], // 切片大小
      tasks: [
        {name: '1', value: 0},
        {name: '2', value: 1},
        {name: '3', value: 2},
        {name: '4', value: 3},
      ], // 任务列表
      task: '', // 当前任务
      condition: {}, // 条件
      conditions: [{
        showname: "线路",
        storename: "line",
        type: "combobox",
        isMult: true,
        url: "http://......"
      }, {
        showname: "明细",
        storename: "details",
        type: "textbox"
      }]
    };
  },
  mounted() {
    let style = $('<style></style>')
    $('html > head').append(style);
  },
  methods: {
    /**
     * @desc 周期变化，修改时间参数
     * @param value 周期值
     * @return 
     * @author qixiaoying
     * @date 2021-07-05
     */
    sectionChange(value){
      this.showDate = value==3 ? false:true
      if(value!=3 && value != this.section){
        let rangeType = ['daterange', 'daterange', 'monthrange']
        let valueFormat = ['yyyy-MM-dd', 'yyyy-MM-dd', 'yyyy-MM']
        this.rangeType = rangeType[value]
        this.valueFormat = valueFormat[value]
        this.pickerOptions.disabledDate = (time)=>{
          if(value == 1){
            return time.getDay() !== 1
          } else{
            return false
          }
        }
        this.ruleForm.dateRange = []
      } 
    },
    /**
     * @desc 开始年份变化，设置终止年份变化区间
     * @param year 开始年份
     * @return 禁用的年份
     * @author qixiaoying
     * @date 2021-07-05
     */
    startYearchange(year){
      this.pickerOptionsEndYear.disabledDate = (time)=>{
        return time.getFullYear() < (year*1+1)
      }
    },
    /**
     * @desc 结束年份变化，设置开始年份变化区间
     * @param year 结束年份
     * @return 禁用的年份
     * @author qixiaoying
     * @date 2021-07-05
     */
    endYearchange(year){
      this.pickerOptionsStartYear.disabledDate = (time)=>{
        return time.getFullYear() > (year-1)
      }
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
.el-row{
  width: 80%;
}
.el-card{
  height: 200px;
  overflow: auto;
  line-height: 30px;
  padding: 10px 0;
  width: 70%;
}
.el-card div{
  padding: 0 20px;
} 

</style>
