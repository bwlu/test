<template>
  <div class="container">
    <div class="h-3" style="position: relative;">
      <el-container>
        <el-form :inline="true" label-width="80px">
          <el-form-item label="选择区域">
            <el-select v-model="form.region" placeholder="请选择区域">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="选择年份">
            <el-select v-model="form.year" placeholder="请选择年份">
              <el-option label="2021" value="2021"></el-option>
              <el-option label="2020" value="2020"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="选择产品">
            <el-select v-model="form.prod" placeholder="请选择产品">
              <el-option label="全部" value=""></el-option>
              <el-option label="复兴号" value="fxh"></el-option>
              <el-option label="和谐号" value="hxh"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="选择型号">
            <el-select v-model="form.xh" placeholder="请选择型号">
              <el-option label="全部" value=""></el-option>
              <el-option label="型号一" value="1"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSearch">查询</el-button>
          </el-form-item>
        </el-form>
      </el-container>
      <div id="myechart" style="width: 100%;height:100%;"></div>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts/lib/echarts'; //echarts
import '../../map/js/world.js'; //对应的省份
export default {
  data() {
    return {
      form: {
        region: '',
        year: '',
        prod: '',
        xh: ''
      }
    };
  },
  mounted() {
    this.mapgeotest('myechart', 'world');
  },
  methods: {
    onSearch(){
      this.mapgeotest('myechart', 'world');
    },
    mapgeotest(id, type) {
      let that = this
      let scatterData = []
      let effectScatterData = []
      // 经度范围:73°33′E至135°05′E;纬度范围:3°51′N至53°33′N
      let x1 = 73, x2 = 135, y1 = 3.51, y2 = 53
      for(let i=0;i<100;i++){
        let x = Math.round(Math.random()*(x2-x1)+x1);
        let y = Math.round(Math.random()*(y2-y1)+y1);
        let s = Math.round(Math.random()*(20-10)+10);
        scatterData.push({name: 'test', value: [x, y], symbolSize: s})
      }
      for(let i=0;i<10;i++){
        let x = Math.round(Math.random()*(x2-x1)+x1);
        let y = Math.round(Math.random()*(y2-y1)+y1);
        let s = Math.round(Math.random()*(30-20)+20);
        effectScatterData.push({name: 'test'+x+y, value: [x, y], symbolSize: s})
      }
      if(type==='world'){
        x1 = -100
        x2 = 60
        y1 = -20
        y2 = 80
        for(let i=0;i<50;i++){
          let x = Math.round(Math.random()*(x2-x1)+x1);
          let y = Math.round(Math.random()*(y2-y1)+y1);
          let s = Math.round(Math.random()*(20-10)+10);
          scatterData.push({name: 'test', value: [x, y], symbolSize: s})
        }
      }
      const data = [
        
      ];
      const geoCoordMap = {
        
      };
      const convertData = function (data) {
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
        return res;
      };
      let geooption = {
        title: {
          show: false,
        },
        tooltip: {
          show: false
        },
        geo: {
          map: type,
          roam: true,
          aspectScale: 0.75,
          // center: [115.97, 29.71],
          scaleLimit: {
            min: 0.75
          },
          itemStyle: {
            color: '#e1e1e1',
            borderWidth: 2.5,
            borderColor: '#ffffff'
          },
          emphasis: {
            //当鼠标放上去  地区区域是否显示名称
            label: {
              show: false,
            },
            itemStyle: {
              color: '#e1e1e1',
            }
          },
        },
        series: [
          {
            name: 'scatter',
            type: 'scatter',
            coordinateSystem: 'geo',
            zlevel: 2,
            symbol: 'circle',
            symbolSize: 20,
            symbolOffset: [0, '-50%'],
            label: {
              show: false,
              // position: 'top',
              // distance: -20,
              // formatter: '{b}',
              // textStyle: {
              //   color: '#1d5adc',
              //   fontSize: 14,
              //   backgroundColor: 'transparent'
              // }
            },
            itemStyle: {
              color: '#1d5adc',
              borderWidth: 0,
            },
            emphasis: {
              itemStyle: {
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 60
              }
            },
            data: scatterData
          },
          {
            name: 'effectScatter',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            zlevel: 2,
            symbol: 'circle',
            symbolSize: 20,
            // symbolOffset: [0, '-50%'],
            label: {
              show: false,
            },
            itemStyle: {
              color: '#1edc64',
              borderWidth: 0,
            },
            emphasis: {
              itemStyle: {
                shadowColor: 'rgba(0, 0, 0, 0.5)',
                shadowBlur: 60
              }
            },
            data: effectScatterData
          },
        ]
      }
      geooption = {
        title: {
          text: '全国主要城市空气质量 - 百度地图',
          subtext: 'data from PM25.in',
          sublink: 'http://www.pm25.in',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        bmap: {
          center: [104.114129, 37.550339],
          zoom: 5,
          roam: true,
          mapStyle: {
            styleJson: [
              {
                featureType: 'water',
                elementType: 'all',
                stylers: {
                  color: '#d1d1d1'
                }
              },
              {
                featureType: 'land',
                elementType: 'all',
                stylers: {
                  color: '#f3f3f3'
                }
              },
              {
                featureType: 'railway',
                elementType: 'all',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'highway',
                elementType: 'all',
                stylers: {
                  color: '#fdfdfd'
                }
              },
              {
                featureType: 'highway',
                elementType: 'labels',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'arterial',
                elementType: 'geometry',
                stylers: {
                  color: '#fefefe'
                }
              },
              {
                featureType: 'arterial',
                elementType: 'geometry.fill',
                stylers: {
                  color: '#fefefe'
                }
              },
              {
                featureType: 'poi',
                elementType: 'all',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'green',
                elementType: 'all',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'subway',
                elementType: 'all',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'manmade',
                elementType: 'all',
                stylers: {
                  color: '#d1d1d1'
                }
              },
              {
                featureType: 'local',
                elementType: 'all',
                stylers: {
                  color: '#d1d1d1'
                }
              },
              {
                featureType: 'arterial',
                elementType: 'labels',
                stylers: {
                  visibility: 'off'
                }
              },
              {
                featureType: 'boundary',
                elementType: 'all',
                stylers: {
                  color: '#fefefe'
                }
              },
              {
                featureType: 'building',
                elementType: 'all',
                stylers: {
                  color: '#d1d1d1'
                }
              },
              {
                featureType: 'label',
                elementType: 'labels.text.fill',
                stylers: {
                  color: '#999999'
                }
              }
            ]
          }
        },
        series: [
          {
            name: 'pm2.5',
            type: 'scatter',
            coordinateSystem: 'bmap',
            data: convertData(data),
            symbolSize: function (val) {
              return val[2] / 10;
            },
            encode: {
              value: 2
            },
            label: {
              formatter: '{b}',
              position: 'right',
              show: false
            },
            emphasis: {
              label: {
                show: true
              }
            }
          },
          {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'bmap',
            data: convertData(
              data
                .sort(function (a, b) {
                  return b.value - a.value;
                })
                .slice(0, 6)
            ),
            symbolSize: function (val) {
              return val[2] / 10;
            },
            encode: {
              value: 2
            },
            showEffectOn: 'render',
            rippleEffect: {
              brushType: 'stroke'
            },
            label: {
              formatter: '{b}',
              position: 'right',
              show: true
            },
            itemStyle: {
              shadowBlur: 10,
              shadowColor: '#333'
            },
            emphasis: {
              scale: true
            },
            zlevel: 1
          }
        ]
      };
      let mychart = echarts.getInstanceByDom(document.getElementById(id));
      if(!mychart){
        mychart = echarts.init(document.getElementById(id));
        mychart.on('click', function(param){
          console.log(param)
          console.log(param.name)
          if(param.name === 'China'){
            that.mapgeotest('myechart', 'china');
          }
        })
      }
      console.log(geooption)
      mychart.setOption(geooption, true);
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
