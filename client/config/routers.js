import Test from 'views/test/test.vue'
import Mapsh from 'views/test/map-shanghai.vue'
import Mapht from 'views/test/mapht-shanghai.vue'
import Map2d from 'views/test/mapsh2d.vue'
import Map2dWorld from 'views/test/map2d-world.vue'
import ImageClick from 'views/test/image-click.vue'

export default [
  {
    path: '/test',
    component: Test,
    name: 'test',
  },
  {
    path: '/mapsh',
    component: Mapsh,
    name: 'mapsh',
  },
  {
    path: '/mapht',
    component: Mapht,
    name: 'mapht',
  },
  {
    path: '/map2d',
    component: Map2d,
    name: 'map2d',
  },
  {
    path: '/Map2dWorld',
    component: Map2dWorld,
    name: 'Map2dWorld',
  },
  {
    path: '/imgclick',
    component: ImageClick,
    name: 'imgclick',
  }
]