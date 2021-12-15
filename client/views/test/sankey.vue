<template>
  <div class="container">
    <div class="h-3" style="position: relative;">
      <div id="myechart" style="width: 100%;height:100%;"></div>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts/lib/echarts'; //echarts
export default {
  data() {
    return {
      mychart: null
    };
  },
  mounted() {
    this.mychart = echarts.init(document.getElementById('myechart'));
    this.genEchart()
  },
  methods: {
    onSearch(){
      this.genEchart()
    },
    genEchart() {
      let nodes = [{"name":"上游"},{"name":"中游"},{"name":"原材料"},{"name":"元器件"},{"name":"零部件"},{"name":"核心关键系统制造和检修"},{"name":"整车制造和检修"},{"name":"其他轨道交通装备"},{"name":"钢材"},{"name":"光管"},{"name":"铝型材"},{"name":"轮轴毛坯"},{"name":"芯片"},{"name":"电容"},{"name":"电阻"},{"name":"轴承"},{"name":"弹簧"},{"name":"线缆"},{"name":"车体"},{"name":"转向架"},{"name":"牵引"},{"name":"制动"},{"name":"高铁动车组"},{"name":"铁路机车车辆"},{"name":"城市轨道交通"},{"name":"通信信号系统"},{"name":"牵引供电系统"},{"name":"优势"},{"name":"劣势"},{"name":"鞍钢"},{"name":"马钢"},{"name":"诺维科轻量化装备"},{"name":"南山铝业"},{"name":"法维莱"},{"name":"TI"},{"name":"NDI"},{"name":"YAGEO"},{"name":"NSK/NTN"},{"name":"大连弹簧"},{"name":"克诺尔"},{"name":"西屋制动"},{"name":"中国中车集团"},{"name":"阿尔斯通"},{"name":"西门子"},{"name":"日立"},{"name":"西屋"},{"name":"通号集团"},{"name":"交控科技"},{"name":"铁科院"}]
      let links = [
        {"source": "上游", "target": "原材料", "value": 1},
        {"source": "上游", "target": "原材料", "value": 1},
      {"source": "原材料", "target": "钢材", "value": 1},
      {"source": "钢材", "target": "优势", "value": 1},
      {"source": "优势", "target": "鞍钢", "value": 1},
      {"source": "优势", "target": "马钢", "value": 1},
      {"source": "原材料", "target": "光管", "value": 1},
      {"source": "光管", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "诺维科轻量化装备", "value": 1},
      {"source": "原材料", "target": "铝型材", "value": 1},
      {"source": "铝型材", "target": "优势", "value": 1},
      {"source": "优势", "target": "南山铝业", "value": 1},
      {"source": "原材料", "target": "轮轴毛坯", "value": 1},
      {"source": "轮轴毛坯", "target": "优势", "value": 1},
      {"source": "上游", "target": "元器件", "value": 1},
      {"source": "元器件", "target": "芯片", "value": 1},
      {"source": "芯片", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "法维莱", "value": 1},
      {"source": "劣势", "target": "TI", "value": 1},
      {"source": "元器件", "target": "电容", "value": 1},
      {"source": "电容", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "NDI", "value": 1},
      {"source": "元器件", "target": "电阻", "value": 1},
      {"source": "电阻", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "YAGEO", "value": 1},
      {"source": "上游", "target": "零部件", "value": 1},
      {"source": "零部件", "target": "轴承", "value": 1},
      {"source": "轴承", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "NSK/NTN", "value": 1},
      {"source": "零部件", "target": "弹簧", "value": 1},
      {"source": "弹簧", "target": "优势", "value": 1},
      {"source": "优势", "target": "大连弹簧", "value": 1},
      {"source": "零部件", "target": "线缆", "value": 1},
      {"source": "线缆", "target": "劣势", "value": 1},
      {"source": "中游", "target": "核心关键系统制造和检修", "value": 1},
      {"source": "核心关键系统制造和检修", "target": "车体", "value": 1},
      {"source": "车体", "target": "优势", "value": 1},
      {"source": "优势", "target": "克诺尔", "value": 1},
      {"source": "核心关键系统制造和检修", "target": "转向架", "value": 1},
      {"source": "转向架", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "克诺尔", "value": 1},
      {"source": "核心关键系统制造和检修", "target": "牵引", "value": 1},
      {"source": "牵引", "target": "劣势", "value": 1},
      {"source": "核心关键系统制造和检修", "target": "制动", "value": 1},
      {"source": "制动", "target": "劣势", "value": 1},
      {"source": "劣势", "target": "西屋制动", "value": 1},
      {"source": "中游", "target": "整车制造和检修", "value": 1},
      {"source": "整车制造和检修", "target": "高铁动车组", "value": 1},
      {"source": "高铁动车组", "target": "优势", "value": 1},
      {"source": "优势", "target": "中国中车集团", "value": 1},
      {"source": "整车制造和检修", "target": "铁路机车车辆", "value": 1},
      {"source": "铁路机车车辆", "target": "优势", "value": 1},
      {"source": "优势", "target": "阿尔斯通", "value": 1},
      {"source": "优势", "target": "西门子", "value": 1},
      {"source": "整车制造和检修", "target": "城市轨道交通", "value": 1},
      {"source": "优势", "target": "日立", "value": 1},
      {"source": "优势", "target": "西屋", "value": 1},
      {"source": "中游", "target": "其他轨道交通装备", "value": 1},
      {"source": "其他轨道交通装备", "target": "通信信号系统", "value": 1},
      {"source": "通信信号系统", "target": "优势", "value": 1},
      {"source": "优势", "target": "通号集团", "value": 1},
      {"source": "其他轨道交通装备", "target": "牵引供电系统", "value": 1},
      {"source": "牵引供电系统", "target": "优势", "value": 1},
      {"source": "优势", "target": "交控科技", "value": 1},
      {"source": "车体", "target": "交控科技", "value": 1},
      {"source": "优势", "target": "铁科院", "value": 1}]
      let option = {
        title: {
          text: 'Node Align Left'
        },
        tooltip: {
          trigger: 'item',
          triggerOn: 'mousemove'
        },
        animation: false,
        series: [
          {
            type: 'sankey',
            emphasis: {
              focus: 'adjacency'
            },
            nodeAlign: 'right',
            data: nodes,
            links: links,
            lineStyle: {
              color: 'source',
              curveness: 0.5
            }
          }
        ]
      }
      this.mychart.setOption(option, true);
    },
  }
};
</script>

<style>
.container {
  width: 100%;
  height: 1000px;
  text-align: center;
}
.container > div {
  width: 100%;
  height: 100%;
  margin: 0 auto;
}
.content{
  display: none;
  width: 200px;
  height: 300px;
  background-color: blue;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 999;
}
</style>
