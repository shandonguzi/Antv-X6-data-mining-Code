<template>
  <div class="login-container">
    <h2 class="login-title">金融数据挖掘与风险管理网站</h2>
        <div class="login-form" v-show="ifLogin">
          <a-form ref="form" :model="form">
            <h2 class="title" style="margin-bottom: 20px; color: #000000">用户登陆</h2>
          <a-form-item>
            <a-input class="inputBox" v-model:value="form.username" placeholder="请输入用户名">
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input-password class="inputBox" v-model:value="form.password" placeholder="请输入密码">
            </a-input-password>
          </a-form-item>
          <a-form-item>
              <a-button type="primary" @click="onSubmit" block>登录</a-button>
              <a-button type="default" @click="changeLog" block style="margin-top: 10px">注册</a-button>
          </a-form-item>
        </a-form>
        </div>
        <div class="log-form" v-show="!ifLogin">
          <a-form ref="formLog" :model="formLog">
            <h2 class="title" style="margin-bottom: 20px; color: #000000">用户注册</h2>
          <a-form-item label="用户名">
            <a-input v-model:value="formLog.username" placeholder="请输入用户名" style="width: 485px; float: right">
            </a-input>
          </a-form-item>
          <a-form-item label="密码">
            <a-input-password v-model:value="formLog.password" placeholder="请输入密码" style="width: 485px; float: right">
            </a-input-password>
          </a-form-item>
          <a-form-item label="确认密码">
            <a-input-password v-model:value="formLog.passwordConfirm" placeholder="确认密码" style="width: 485px; float: right">
            </a-input-password>
          </a-form-item>
          <a-form-item>
              <a-button type="primary" @click="onLog" block>确认注册</a-button>
          </a-form-item>
        </a-form>
        </div>
  </div>
</template>

<script lang="ts">
import {ref} from 'vue'
import {useRouter} from "vue-router";
import axios from "axios";
import { message } from 'ant-design-vue'
import Cookies from 'js-cookie'

export default {
  name: 'login',
  setup() {
    let form = ref({
      username: null,
      password: null
    })

    let formLog = ref({
      username: null,
      password: null,
      passwordConfirm: null
    })

    let ifLogin = ref(true)

    const router = useRouter()

    function onSubmit() {
      axios.post('http://127.0.0.1:8000/api/test_login_info', form.value).then(res => {
        console.log(res)
        if (res.data.result == 1) {
          message.success(
            '登陆成功，2s后跳转至组件介绍页面',
            2,
              (()=>{
                Cookies.set('username', form.value.username)
                router.push({
                  path: "/Introduction"
                })
              })
          );
        } else {
          message.error(
            '用户名或密码错误，请重新输入',
            2,
          );
        }
      })
    }

    function changeLog(){
      ifLogin.value = false
    }

    function onLog(){
      console.log(formLog.value)
      axios.post('http://127.0.0.1:8000/api/log', formLog.value).then(res => {
        console.log(res)
        if (res.data.result == 1) {
          message.success(
            '注册成功，2s后跳转至登陆页面',
            2,
              (()=>{
                ifLogin.value = true
              })
          );
        } else {
          message.error(
            '用户名已存在，请重新输入',
            2,
          );
        }
      })

    }

    return {
      form,
      formLog,
      ifLogin,
      onSubmit,
      changeLog,
      onLog,
    }
  }
}
</script>
<style>
.login-form {
  background: #ffffff;
  padding: 20px;
  width: 600px;
  height: 320px;
  margin: 0 auto
}

.log-form {
  background: #ffffff;
  padding: 20px;
  width: 600px;
  height: 320px;
  margin: 0 auto
}

/* 背景 */
.login-container {
  position: absolute;
  width: 100%;
  height: 100%;
  background: url("~@/assets/login_background.png");
}

/* Log */
.login-title {
  margin-top: 100px;
  margin-bottom: 50px;
  color: #fff;
  text-align: center;
  font-size: 48px;
  font-family: Microsoft Yahei;
}

/* 用户登陆标题 */
.title {
  margin-bottom: 20px;
  color: #fff;
  font-weight: 700;
  font-size: 24px;
  font-family: Microsoft Yahei;
}

/* 输入框 */
.inputBox {
  height: 45px;
}

.logBox {
  width: 200px;
  float: right;
}

/* 输入框内左边距50px */
.ant-input-affix-wrapper .ant-input:not(:first-child) {
  padding-left: 50px;
}

</style>

