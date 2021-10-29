<template>
  <div class="container">
    <h1>上海地图</h1>
    <div class="h-3" style="position: relative;">
      <!--弹窗-->
      <div>
        <div class="content">
          <p>test</p>
          <p>test</p>
          <p>test</p>
          <p>test</p>
          <p>test</p>
          <p>test</p>
          <p>test</p>
        </div>
      </div>
      <div id="myechart" style="width: 100%;height:100%;"></div>
      <div id="myechart1" style="width: 100%;height:100%;"></div>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts/lib/echarts'; //echarts
import '../../map/js/province/shanghai.js'; //对应的省份
import '../../map/js/china.js'; //对应的省份
import 'echarts-gl'; //3D地图插件
export default {
  data() {
    return {};
  },
  mounted() {
    this.mapgeotest('myechart');
  },
  methods: {
    mapgeotest(id) {
      let geooption = {
        title: {
          show: false,
          text: '测试scatter、geo',
          x: 'left',
          top: '10',
          textStyle: {
            color: '#000',
            fontSize: 14
          }
        },
        tooltip: {
          show: false
        },
        geo: {
          map: '上海',
          roam: true,
          regionHeight: 2.5,
          itemStyle: {
            color: '#1d5adc',
            borderWidth: 0.5,
            borderColor: '#09C6EE'
          },
          emphasis: {
            //当鼠标放上去  地区区域是否显示名称
            label: {
              show: false,
            },
            itemStyle: {
              // color: '#0eb7ff',
              shadowColor: 'rgba(0, 0, 0, 0.5)',
              shadowBlur: 60
            }
          },
        },
        series: [
          {
            name: 'scatter',
            type: 'scatter',
            coordinateSystem: 'geo',
            zlevel: 2,
            symbol: 'image://./static/mp.png',
            symbolSize: 60,
            label: {
              show: true,
              position: 'top',
              distance: -20,
              formatter: '{b}',
              textStyle: {
                color: '#66e3ff',
                fontSize: 14,
                backgroundColor: 'transparent'
              }
            },
            itemStyle: {
              color: '#66e3ff',
              borderWidth: 0,
              borderColor: '#66e3ff'
            },
            emphasis: {
              itemStyle: {
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 60
              }
            },
            data: [
              {name: '站点1', value: [121.59, 31.22, 3000], symbol: 'image://./static/mp1.png', symbolSize: 60},
              {name: '站点2', value: [121.49, 31.22, 3000]},
              {name: '站点3', value: [121.59, 31.12, 3000]},
              {name: '站点4', value: [121.59, 31.02, 3000]},
              {name: '站点5', value: [121.39, 30.84, 3000]},
            ]
          },
        ]
      }
      let mychart = echarts.init(document.getElementById(id));
      mychart.setOption(geooption);
      mychart.on('click', function(param){
        console.log(param)
      })
      // mychart.on('mouseout', function(param){
      //   console.log(mychart.getOption())
      //   if(param.data && param.data.fl){
      //     let option = mychart.getOption()
      //     console.log(option)
      //     option.geo3D[0].regions = []
      //     mychart.setOption(option)
      //   }
      // })
    },
  }
};
$(document).on('click', function(){
  $('.content').hide();
})
$('.content').click(function(e){
  console.log('content')
  if ( e && e.stopPropagation ){
    e.stopPropagation();
  }
})
</script>

<style>
.container {
  width: 100%;
  height: 1000px;
  text-align: center;
}
.container > div {
  width: 1000px;
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
