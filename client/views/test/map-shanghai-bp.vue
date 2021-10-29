<template>
  <div class="container">
    <h1>上海地图</h1>
    <img src="./map.png"/>
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
    this.mapgeo3dtest('myechart', '#2183DC', './static/a.png', 2);
    this.mapgeo3dtest('myechart1', '#dcdcdc', './static/d.png', 6);
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
          // {
          //   type: 'continuous',
          //   seriesIndex: 0,
          //   text: ['bar3D'],
          //   calculable: true,
          //   max: 300,
          //   inRange: {
          //     color: ['#87aa66', '#eba438', '#d94d4c']
          //   }
          // },
          // {
          //   type: 'continuous',
          //   seriesIndex: 1,
          //   text: ['scatter3D'],
          //   left: 'right',
          //   max: 100,
          //   calculable: true,
          //   inRange: {
          //     color: ['#000', 'blue', 'purple']
          //   }
          // }
        ],
        geo: {
          show: false,
          map: '上海',
          viewControl: {
            distance: 130, //地图视角 控制初始大小
            rotateSensitivity: 0, //禁止旋转
            zoomSensitivity: 0 //禁止缩放
          },
        },
        geo3D: {
          map: '上海',
          roam: true,
          boxDepth: 100,
          regionHeight: 2,
          itemStyle: {
            color: 'transparent',
            opacity: 1,
            borderWidth: 0,
          },
          viewControl: {
            distance: 130, //地图视角 控制初始大小
            rotateSensitivity: 0, //禁止旋转
            zoomSensitivity: 0 //禁止缩放
          },
          label: {
            show: false,
            textStyle: {
              color: 'transparent', //地图初始化区域字体颜色
              fontSize: 8,
              opacity: 1,
              backgroundColor: 'rgba(0,23,11,0)'
            }
          },
          shading: 'lambert',
          // lambertMaterial: {
          //   detailTexture: './map.png',
            
          // },
          // regions: [
          //   {
          //     name: '松江区',
          //     itemStyle: {
          //       color: '#09b4b4' //地图高亮颜色
          //     }
          //   }
          // ],
          // colorMaterial: {
          //   detailTexture: './static/map.png', // 纹理贴图 格式支持（string, HTMLImageElement, HTMLCanvasElement）
          //   textureTiling: 1 ,// 纹理平铺，1是拉伸，数字表示纹理平铺次数
          //   textureOffset: 1
          // },
          emphasis: {
            //当鼠标放上去  地区区域是否显示名称
            label: {
              show: false,
              textStyle: {
                color: '#fff',
                fontSize: 3,
                backgroundColor: '#007436'
              }
            },
            itemStyle: {
              color: '#09C6EE' ,//地图高亮颜色
              // opacity: 0.3,
            }
          },
          regions: [
            {
              name: '金山区', 
              itemStyle: {
                color: '#09C6EE' ,//地图高亮颜色
                opacity: 0.3,
              },
            }
          ],
          zlevel: 1,
          // light: {
          //   //光照阴影
          //   main: {
          //     color: '#fff', //光照颜色
          //     intensity: 1.2, //光照强度
          //     shadowQuality: 'high', //阴影亮度
          //     shadow: true, //是否显示阴影
          //     alpha: 55,
          //     beta: 10
          //   },
          //   ambient: {
          //     intensity: 0.3
          //   }
          // },
        },
        series: [
          {
            type: 'map3D',
            name: '上海',
            silent: true,
            selectedMode: 'single', //地图高亮单选
            boxDepth: 100, //地图倾斜度
            regionHeight: 1, //地图高度
            map: '上海',
            viewControl: {
              distance: 130, //地图视角 控制初始大小
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
              color: bgcolor,
              opacity: 1,
              borderWidth: 1,
              borderColor: '#09C6EE'
            },
            shading: `color`,
            colorMaterial: {
              detailTexture: img, // 纹理贴图 格式支持（string, HTMLImageElement, HTMLCanvasElement）
              textureTiling: num ,// 纹理平铺，1是拉伸，数字表示纹理平铺次数
              textureOffset: 0
            },
            // postEffect: {
            //   enable: true,
            //   SSAO: {
            //     enable: true,
            //     intensity: 1.3,
            //     radius: 5
            //   },
            //   screenSpaceReflection: {
            //     enable: false
            //   },
            //   depthOfField: {
            //     enable: true,
            //     blurRadius: 4,
            //     focalDistance: 30
            //   }
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
            // symbol: 'path://M8 16A8 8 0 1 1 8 0h10a8 8 0 1 1 0 16h-3l-2 4-2-4H8z',
            // symbol: 'image://data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC4AAABACAMAAABSmbUvAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAzFBMVEURHDz///9l/f5m//9ss76B192V+PmV+PmB191kprMjOlYRHDwiOFRnrLh/09pnq7d/1NpY2t9b4uZc5elf6+5h8vRj9vdk+vpl/P1W1Npc5Ohg7vBj+Plh8vRc4+dV0tlMusRBnas0eYwkUGhc5eli8/Ve6+1TzNM7jJwRHDxZ3eJf6+5e6exJsryV+fpc5OhZ3OETIEBsipuq1du/7/Gq/v5m//9j9/g9kqG66ezJ+/wWKEdm/v5m//+Z//9l/f7M//+5///G///////zcFiGAAAAPnRSTlMAAAAACbD19q+3iYCIu6i7qRJGdJm50uX0EF6i3M6tj3RdTD5owb2HVTMUlbVt5YqdNFSTyfl62le18DX9jGs65F8AAAABYktHRAH/Ai3eAAAAB3RJTUUH5QobAjYCI2PMmQAAAjp6VFh0UmF3IHByb2ZpbGUgdHlwZSB4bXAAADiNlVVbttsgDPzXKroErCdejhPMX8/pZ5ffEdwkTuLepvaJjYXQjEaC0O+fv+hHXlELyVV61Ci+uPjFLZSLs5uHr75LY9775XLpzLCvrmmxENMmRVsUFfhWX0lrbIGFJrHpbup4I6AIFjFLl52LXKPKFtWx0FuC+cIlv/3qe0jOUSKAjXpPHrLNibv7YPIIA9slV+h9BRer2qwQJ7kewyTGuwg38CmyCFAF+cK2iIrlGLYrrDzmmTve8+nEbbhtw3GDS3B5ufkrPQYL+Birqr+kxjQmM70airvIhnR6jIv3gBfvg3EAeZE17zsTxrNNADAKCdQnFYmKtICQ888sQAGlQiHY16HUCoXgcZv3hSBYDwibrKawx1qkwO98B9j+KBHGQhg2pFLBpyR5SFtutXoNqQ3d85ew9Bz3PCwCtpPgEmrZukNj+jfp8+DZ3AG94NMzHIUMjRgLbMZPqSd2htcU2BBEs3aWAN2vb01ZwAgO6SRjVLJBTdCGhauN/Zbu6AXh9QEw1No0qy1Zb4dGYKKrjqpNJ6Szju2JoqsgKosoYqP6+Gm+0fVqKoq+wuascMPud7QYw3FBk1V8MTbKK3KmIGG5A7Pj3oDRV3SCHN8hnwPLTvOQeEK30b8OdHxgnFUrh2JvftDmJg19oI1+wpDetDkif6DNDZgOyPb/2vDXCcqdvt/fN7fns+huPRzANI/UOXXyN2DZkCMdnic4/QFsymws4FeZRAAAAQ1JREFUSMft09cSgjAQBdCIiiXYsPcK9l6wLuj/f5QdDUYIT44zuU9hc4ZJ2SDkLj6/CIwJ+H0oGApjxkiRKBKZNcZhEQG7xhg45/y/ucvnEQxJrFqKxS9PO+DmadMD8GXCQw0Avc4555xz/jMu2HPvLQk5mUpnsjmAXDaTTiXlxL1O4/lCsVSuVGv1RhOg2ajXqpVyqVjI03lLUdud7j0Aj0GnrSotCu/1B8OumdHoNR4O+r0PPp5Mn/Oz+WK5XMxnz+/pZGzhK11bm7/bGMbxaBgbs7DW9JUtP51suUcgF7PdkosRBAsnt/qe61at3HKQZr4dJHlNu53jNb03wX7v0ARkdN2hxcgcDnR+BjiSiSXZunu5AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIxLTEwLTI3VDAyOjU0OjAyKzAwOjAw2Gn5nAAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMS0xMC0yN1QwMjo1NDowMiswMDowMKk0QSAAAAAZdEVYdFNvZnR3YXJlAEFkb2JlIEltYWdlUmVhZHlxyWU8AAAAAElFTkSuQmCC',
            symbol: 'rect',
            symbolSize: 20,
            silent: true,
            label: {
              show: true,
              position: 'top',
              distance: 0,
              formatter: '{b}',
              textStyle: {
                color: '#fff',
                fontSize: 20,
                backgroundColor: 'transparent'
              }
            },
            itemStyle: {
              color: 'red',
              borderWidth: 0.5,
              borderColor: 'green'
            },
            data: [
              {name: '金山区1', value: [121.59, 31.22, 3000], fl: '浦东新区'},
              {name: '金山区2', value: [121.49, 31.22, 3000], fl: '浦东新区'},
              {name: '金山区3', value: [121.59, 31.12, 3000], fl: '金山区'},
              {name: '金山区4', value: [121.59, 31.02, 3000], fl: '长宁区'},
              {name: '金山区5', value: [121.39, 30.84, 3000], fl: '宝山区'},
            ]
          },
        ]
      }
      let mychart = echarts.init(document.getElementById(id));
      mychart.setOption(geooption);
      // mychart.on('click', function(param){
      //   console.log(param)
      //   console.log(param.name)
      //   console.log(param.event.offsetX)
      //   console.log(param.event.offsetY)
      //   $('.content').css('top', param.event.offsetY+10+'px')
      //   $('.content').css('left', param.event.offsetX+10+'px')
      //   $('.content').show()
      //   param.event.stop()
      // })
      // mychart.on('mouseover', function(param){
      //   let option = mychart.getOption()
      //   if(param.data && param.data.fl){
      //     option.geo3D[0].regions = [{
      //       name: param.data.fl,
      //       itemStyle: {
      //         color: '#09C6EE',
      //         opacity: 0,
      //       }
      //     }]
      //   } else{
      //     option.geo3D[0].regions = []
      //   }
      //   mychart.setOption(option)
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
  width: 1000px;
  height: 1000px;
}
.container > div {
  width: 100%;
  height: 100%;
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
