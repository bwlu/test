<template>
  <div class="container">
    <h1>上海地图</h1>
    <div class="h-3" style="position: relative;">
      <!--弹窗-->
      <!-- <div class="layer" ref="layer" :style="styles" v-if="layerList.length>0">
            <div class="content">
                <p>LPL夏季赛({{name}})</p>
                <Row style="text-align: center;line-height: 22px;height: 24px;">
                    <Button style="margin-left:4px" :type="item.selected?'warning':'info'" size="small" @click="tabsChange(item)" v-for="(item,index) in btn" :key="index">{{item.name}}</Button>
                </Row>
                <Row style="text-align: center;padding-bottom: 20px;">
                    <Col span="8" v-for="(item,index) in layerList" :key="index" class="col-item">
                        <div class="num">{{item.circle}}</div>
                        <div class="text">{{item.text}}</div>
                    </Col>
                </Row>
                <Spin fix style="background: rgba(0,0,0,0.5);font-size: 20px;" v-if="loading">
                    <Icon type="ios-loading" size=18 class="demo-spin-icon-load"></Icon>
                    <div>Loading</div>
                </Spin>
            </div>
        </div> -->
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
    this.mapgeo3dtest();
  },
  methods: {
    convertData(data) {
      var res = [];
      for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
          res.push({
            name: data[i].name,
            value: geoCoord.concat(data[i].value)
          });
        }
      }
      console.log(res);
      return res;
    },
    mapgeo3dtest() {
      let geooption = {
        title: {
          text: '测试bar3D、scatter3D、geo3D',
          x: 'left',
          top: '10',
          textStyle: {
            color: '#000',
            fontSize: 14
          }
        },
        tooltip: {
          show: true
          // formatter:(params)=>{
          //   let data = "测试1:"+params.name + "<br/>"+"值:"+ params.value[2]+"<br/>"+"地理坐标:[" + params.value[0]+","+params.value[1] +"]";
          //   return data;
          // },
        },
        visualMap: [
          {
            type: 'continuous',
            seriesIndex: 0,
            text: ['bar3D'],
            calculable: true,
            max: 300,
            inRange: {
              color: ['#87aa66', '#eba438', '#d94d4c']
            }
          },
          {
            type: 'continuous',
            seriesIndex: 1,
            text: ['scatter3D'],
            left: 'right',
            max: 100,
            calculable: true,
            inRange: {
              color: ['#000', 'blue', 'purple']
            }
          }
        ],
        geo3D: {
          map: 'china',
          roam: true,
          regionHeight: 3,
          itemStyle: {
            color: '#1d5e98',
            opacity: 1,
            borderWidth: 0.4,
            borderColor: '#000'
          },
          viewControl: {
            distance: 150, //地图视角 控制初始大小
            rotateSensitivity: 0, //禁止旋转
            zoomSensitivity: 0 //禁止缩放
          },
          label: {
            // show: true,
            textStyle: {
              color: '#f00', //地图初始化区域字体颜色
              fontSize: 8,
              opacity: 1,
              backgroundColor: 'rgba(0,23,11,0)'
            }
          },
          regions: [
            {name: '广东', regionHeight: 10}
          ],
          emphasis: {
            //当鼠标放上去  地区区域是否显示名称
            label: {
              show: true,
              textStyle: {
                color: '#fff',
                fontSize: 3,
                backgroundColor: 'rgba(0,23,11,0)'
              }
            },
            regionHeight: 10
          },
          //shading: 'lambert',
          light: {
            //光照阴影
            main: {
              color: '#fff', //光照颜色
              intensity: 1.2, //光照强度
              //shadowQuality: 'high', //阴影亮度
              shadow: false, //是否显示阴影
              alpha: 55,
              beta: 10
            },
            ambient: {
              intensity: 0.3
            }
          }
        },
        series: [
          {
            name: 'bar3D',
            type: 'bar3D',
            coordinateSystem: 'geo3D',
            barSize: 0.5, //柱子粗细
            shading: 'lambert',
            opacity: 1,
            bevelSize: 0.3,
            label: {
              show: false,
              formatter: '{b}'
            },
            data: [
              {name: '齐齐哈尔', value: [123.97, 47.33, 2000]}
            ]
          },
          {
            name: 'scatter3D',
            type: 'scatter3D',
            coordinateSystem: 'geo3D',
            symbol: 'pin',
            symbolSize: 30,
            opacity: 1,
            label: {
              show: false,
              formatter: '{b}'
            },
            itemStyle: {
              borderWidth: 0.5,
              borderColor: '#fff'
            },
            data: []
          }
        ]
      }
      let mychart = echarts.init(document.getElementById('myechart'));
      mychart.setOption(geooption);
    },
    map3dtest() {
      let myoption = {
        series: [
          {
            type: 'map3D',
            name: '上海',
            selectedMode: 'single', //地图高亮单选
            boxDepth: 90, //地图倾斜度
            regionHeight: 3, //地图高度
            map: '上海',
            viewControl: {
              distance: 150, //地图视角 控制初始大小
              rotateSensitivity: 0, //禁止旋转
              zoomSensitivity: 0 //禁止缩放
            },
            label: {
              // show: true, //是否显示市
              textStyle: {
                color: '#0a1640', //文字颜色
                fontSize: 12, //文字大小
                backgroundColor: 'rgba(0,0,0,0)' //透明度0清空文字背景
              }
            },
            itemStyle: {
              color: '#1917c3', //地图颜色
              borderWidth: 0.5, //分界线wdith
              borderColor: '#459bca' //分界线颜色
            },
            emphasis: {
              regionHeight: 13,
              label: {
                show: false, //是否显示高亮
                textStyle: {
                  color: '#fff' //高亮文字颜色
                }
              },
              itemStyle: {
                color: '#0397ec' //地图高亮颜色
              }
            },
            //高亮市区  echarts  bug 不生效
            data: [
              {
                name: '金山区',
                regionHeight: 28,
                itemStyle: {
                  // 单个区域的样式设置
                  color: '#0489d6',
                  opacity: 1,
                  borderWidth: 1,
                  borderColor: '#04a3ff'
                },
                label: {
                  show: true, //是否显示高亮
                  textStyle: {
                    color: '#fff' //高亮文字颜色
                  }
                }
              }
            ]
          }
        ]
      };
      let mychart = echarts.init(document.getElementById('myechart'));
      mychart.setOption(myoption);
    }
  }
};
</script>

<style>
.container {
  width: 100%;
  height: 800px;
}
.container > div {
  width: 100%;
  height: 100%;
}
</style>
