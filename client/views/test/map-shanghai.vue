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
// import 'echarts-gl'; //3D地图插件
export default {
  data() {
    return {};
  },
  mounted() {
    this.mapgeo3dtest('myechart', '#2183DC', './static/a.png', 2);
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
    mapgeo3dtest(id, bgcolor, img, num=1) {
      // let img = 'image://'+require('@/client/views/test/xz3.png')
      let geooption = {
        title: {
          show: false,
          text: '测试scatter3D、geo3D',
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
        geo3D: {
          map: '上海',
          roam: true,
          boxDepth: 100,
          regionHeight: 2.5,
          itemStyle: {
            color: 'transparent',
            borderWidth: 0,
          },
          viewControl: {
            distance: 130, //地图视角 控制初始大小
            rotateSensitivity: 0, //禁止旋转
            zoomSensitivity: 0 //禁止缩放
          },
          // shading: `color`,
          // colorMaterial: {
          //   detailTexture: './static/f.png', // 纹理贴图 格式支持（string, HTMLImageElement, HTMLCanvasElement）
          //   textureTiling: 6 ,// 纹理平铺，1是拉伸，数字表示纹理平铺次数
          // },
          emphasis: {
            //当鼠标放上去  地区区域是否显示名称
            label: {
              show: false,
            },
            itemStyle: {
              color: '#113fe4' ,//地图高亮颜色
              opacity: 0.8,
              borderWidth: 1,
              borderColor: '#09C6EE'
            }
          },
        },
        series: [
          {
            type: 'map3D',
            silent: true,
            name: '上海',
            selectedMode: 'single', //地图高亮单选
            boxDepth: 100, //地图倾斜度
            regionHeight: 2, //地图高度
            map: '上海',
            viewControl: {
              distance: 130, //地图视角 控制初始大小
              rotateSensitivity: 0, //禁止旋转
              zoomSensitivity: 0 //禁止缩放
            },
            itemStyle: {
              color: bgcolor,
              opacity: 1,
              borderWidth: 1,
              borderColor: '#09C6EE'
            },
            // shading: `color`,
            // colorMaterial: {
            //   detailTexture: img, // 纹理贴图 格式支持（string, HTMLImageElement, HTMLCanvasElement）
            //   textureTiling: num ,// 纹理平铺，1是拉伸，数字表示纹理平铺次数
            // },
            data: [
              {
                name: '崇明区',
                itemStyle: {
                  borderWidth: 0
                },
              },
            ]
          },
          {
            name: 'scatter3D',
            type: 'scatter3D',
            coordinateSystem: 'geo3D',
            zlevel: 2,
            symbol: 'pin',
            symbolSize: 30,
            silent: true,
            label: {
              show: true,
              position: 'top',
              distance: 0,
              formatter: '{b}',
              textStyle: {
                color: '#66e3ff',
                fontSize: 20,
                backgroundColor: 'transparent'
              }
            },
            itemStyle: {
              color: '#66e3ff',
              borderWidth: 0,
              borderColor: '#66e3ff'
            },
            data: [
              {name: '站点1', value: [121.59, 31.22, 3000]},
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
      // mychart.on('mouseover', function(param){
      //   console.log(param)
      // })
      // mychart.on('mouseout', function(param){
      //   console.log(mychart.getOption())
      //   if(param.data && param.data.fl){
      //     let option = mychart.getOption()
      //     console.log(option)
      //     option.geo3D[0].regions = []
      //     mychart.setOption(option)
      //   }
      // })
      mychart.getZr().on('click', function (clickparams) {
          console.log(clickparams);
          console.log(clickparams.offsetX, clickparams.offsetY);
      });
      mychart.getZr().on('legendselectchanged', function (obj) {
        console.log(obj)
      })
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
