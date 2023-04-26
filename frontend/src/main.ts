import {createApp} from 'vue'
import App from './App.vue'
import router from './router'

import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import Menus from 'vue3-menus'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as Icons from '@ant-design/icons-vue'
import ECharts from 'vue-echarts'
import "echarts"


const app = createApp(App)
app.use(ElementPlus).use(Menus, {'name': 'menus'}).use(router).use(Antd).component('ECharts', ECharts)

const icons: any = Icons
for (const i in icons) {
    app.component(i, icons[i])
}

app.mount('#app')