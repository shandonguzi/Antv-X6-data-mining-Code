<template>
  <a-layout>
    <a-layout-header class="header" style="padding: 0 0">
      <a-row>
        <a-col :span="4">
          <div class="logo">
            <laptop-outlined style="fontSize: 25px; color: white"/>
            <el-text style="color: white; font-size: 25px; margin-left: 10px">Data Mining</el-text>
          </div>
        </a-col>
        <a-col :span="20">
          <a-menu
              v-model:selectedKeys="selectedKeys1"
              theme="dark"
              mode="horizontal"
              :style="{ lineHeight: '64px'}"
          >
            <a-menu-item key="1">
              <router-link to="/Introduction"></router-link>
              组件介绍
            </a-menu-item>
            <a-menu-item key="2">
              <router-link to="/homeView"></router-link>
              数据实验楼
            </a-menu-item>
            <a-sub-menu :title="showUserName" :style="{marginLeft: 'auto'}">
              <template #icon>
                <user-outlined/>
              </template>
              <a-menu-item @click="exit">退出登录</a-menu-item>
            </a-sub-menu>

            <!--        <a-menu-item key="3">-->
            <!--          <router-link to="/testModal"></router-link>-->
            <!--          用户管理-->
            <!--        </a-menu-item>-->
          </a-menu>
        </a-col>
      </a-row>
    </a-layout-header>
  </a-layout>
</template>
<script lang="ts">
import {UserOutlined, LaptopOutlined, NotificationOutlined} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';
import {useRouter} from 'vue-router'
import Cookies from "js-cookie";
import {message} from "ant-design-vue";

export default defineComponent({
  name: 'testNavi',
  components: {
    UserOutlined,
    LaptopOutlined,
    NotificationOutlined,
  },
  setup() {
    let router = useRouter()
    return {
      selectedKeys1: ref<string[]>([router.currentRoute.value.fullPath === '/Introduction' ? '1' : '2']),
      collapsed: ref<boolean>(false),
    };
  },
  computed: {
    showUserName() {
      return Cookies.get('username')
    }
  },
  methods: {
    exit() {
      message.success(
          '成功退出',
          1,
          (() => {
            this.$router.push({
              path: "/"
            })
          })
      );
    }
  }
});
</script>
<style scoped>
.logo {
  /*float: left;*/
  /*width: 245px;*/
  margin: 0 auto;
  height: 64px;
}

.site-layout-background {
  background: #fff;
}
</style>