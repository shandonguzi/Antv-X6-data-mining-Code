<template>
  <!--  <img alt="Vue logo" src="./assets/logo.png">-->
  <!--  <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>-->
  <!--  <homeView/>-->

  <div v-if="$route.meta.keepAlive">
    <test-navi></test-navi>
    <router-view v-slot="{ Component }">
      <transition>
        <keep-alive>
          <component :is="Component"></component>
        </keep-alive>
      </transition>
    </router-view>

  </div>
  <div v-if="!$route.meta.keepAlive">
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import HelloWorld from './components/HelloWorld.vue';
import homeView from "@/components/homeView.vue";
import testNavi from "@/components/testNavi.vue";

export default defineComponent({
  name: 'App',
  components: {
    // HelloWorld
    // homeView,
    testNavi
  }
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
}
</style>
