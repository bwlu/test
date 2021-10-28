import Test from 'views/test/test.vue'
import Mapsh from 'views/test/map-shanghai.vue'
import Mapht from 'views/test/mapht-shanghai.vue'
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
    path: '/imgclick',
    component: ImageClick,
    name: 'imgclick',
  }
]