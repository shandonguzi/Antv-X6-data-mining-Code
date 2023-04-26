<template>
  <div id="login" class="loginContainer">
    <div class="loginMainWrapper">
      <div class="loginWrapper">
        <div class="loginTipsWrapper" style="color: #ffffff">
          <span class="siteSummaryTitle">田少蛟博客管理系统</span>
          <div class="siteSummary">
            <ul>
              <li>
                <a-icon type="check-square" style="margin-right: 10px"/>
                <span>统一方便的资源管理</span></li>
              <li>
                <a-icon type="check-square" style="margin-right: 10px"/>
                <span>友好的界面展示，基于AntDesign组件库</span></li>
              <li>
                <a-icon type="check-square" style="margin-right: 10px"/>
                <span>基于角色权限划分，更利于资源隔离</span></li>
              <li>
                <a-icon type="check-square" style="margin-right: 10px"/>
                <span>前后端分离，便于维护</span></li>
              <li>
                <a-icon type="check-square" style="margin-right: 10px"/>
                <span>前后端均支持多实例部署</span></li>
            </ul>
          </div>
        </div>
        <div class="loginBoxWrapper">
          <a-form-model :model="formInline" @submit="handleSubmit" @submit.native.prevent style="width: 100%">
            <a-form-model-item style="text-align: center">
              <h1>欢迎登录</h1>
            </a-form-model-item>
            <a-form-model-item>
              <a-input v-model="formInline.user" placeholder="账号">
                <a-icon slot="prefix" type="user" style="color:rgba(0,0,0,.25)"/>
              </a-input>
            </a-form-model-item>
            <a-form-model-item>
              <a-input v-model="formInline.password" type="password" placeholder="密码">
                <a-icon slot="prefix" type="lock" style="color:rgba(0,0,0,.25)"/>
              </a-input>
            </a-form-model-item>
            <a-form-model-item>
              <div class="rememberMeWrapper">
                <a-checkbox-group v-model="formInline.resource">
                  <a-checkbox value="true" name="type">记住密码</a-checkbox>
                </a-checkbox-group>
                <a href="">忘记密码</a>
              </div>
            </a-form-model-item>
            <a-form-model-item>
              <router-link to="/admin" style="width: 100%" class="ant-btn ant-btn-primary">立即登录</router-link>
              还没有账号?
              <a href="" class="ant-btn ant-btn-link">立即注册</a>
            </a-form-model-item>
            <a-divider>其他登录方式</a-divider>
            <a-form-model-item style="text-align: center">
              <a-space size="large">
                <a-icon type="weibo" style="font-size: 2em;cursor: pointer;color:#f50"/>
                <a-icon type="qq" style="font-size: 2em;cursor: pointer;color:#2b92e4;"/>
                <a-icon type="github" style="font-size: 2em;cursor: pointer;color:#333;"/>
              </a-space>
            </a-form-model-item>
          </a-form-model>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      formInline: {
        user: '',
        password: '',
        resource: '',
      },
    };
  },
  methods: {
    handleSubmit(e) {
      console.log(this.formInline);
    },
  },
}
</script>

<style scoped>
.loginContainer {
  width: 100%;
  height: 100%;
  position: absolute;
  background: url("~@/assets/login_background.png");
  background-attachment: fixed;
  background-repeat: no-repeat !important;
  background-size: cover;
  background-position: center;
  padding-top: 105px;
  min-height: 100%;
}

.loginHeader {
  width: 100%;
  height: 64px;
  background-color: #ffffff;
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 15px rgba(0, 0, 0, .2);
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: row;
  padding: 10px;
}

.loginHeader span {
  font-size: 25px;
  font-weight: 700;
}

.loginMainWrapper {
  width: 100%;
  display: flex;
  justify-content: space-between;
  flex-direction: column;
  align-items: center;
}

.loginWrapper {
  width: 90%;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-direction: row;
  height: 100%;
}

.loginFooter {
  width: 100%;
  min-height: 64px;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-direction: row;
  text-align: center;
  color: #ffffff;
  margin-top: 40px;
}

.siteSummary ul {
  list-style: none;
  padding: 0;
}

.siteSummary ul li {
  margin-top: 10px;
  list-style: none;
}

@media screen and (min-width: 1200px) {
  .loginTipsWrapper {
    padding: 20px 30px;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-direction: column;
    min-height: 100%;
  }

  .loginBoxWrapper {
    background-color: #ffffff;
    padding: 20px;
    width: 400px;
    height: 100%;
    border-radius: 5px;
  }
}

@media screen and (min-width: 769px) and (max-width: 1200px) {
  .loginTipsWrapper {
    padding: 20px 30px;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    flex-direction: column;
    height: 100%;
  }

  .loginBoxWrapper {
    background-color: #ffffff;
    padding: 20px;
    width: 400px;
    height: 100%;
    border-radius: 5px;
  }
}

@media screen and (max-width: 768px) {
  .loginTipsWrapper {
    display: none;
  }

  .loginBoxWrapper {
    background-color: #ffffff;
    padding: 20px;
    width: 100%;
    border-radius: 5px;
  }
}

.rememberMeWrapper {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
}

.siteSummaryTitle {
  color: #ffffff;
  font-size: 1.5rem;
  font-weight: 700;
}

.siteSummary {
  margin-top: 25px;
  color: #ffffff;
  font-size: 1.2rem;
  font-weight: 300;
}
</style>