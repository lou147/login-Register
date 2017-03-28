<template>
	<div class="main-body">
		<div class="header">
			<a href="/#/">Home</a>
		</div>
		
		<form class="pure-form">
			<div class="head">
				<a id="nav" href="/#/register_phone">注册</a>
				<b>·</b>
				<a id="nav" class="active">登录</a>
			</div>

			<fieldset class="pure-group">
				<div @click="clickName" class="input-field" style="border-bottom: none;">
					<label id="form-label">{{name_msg}}</label>
					<input v-model="username" type="text" class="pure-input-1" placeholder="手机号或邮箱">
				</div>

				<div @click="clickPassword" class="input-field">
					<label id="form-label">{{password_msg}}</label>
					<input v-model="password" type="password" class="pure-input-1" placeholder="输入密码">
				</div>
		    </fieldset>

		    <span @click="checkInfo" id="btn" type="submit" class="pure-button pure-input-1 pure-button-primary">登录</span>
		</form>
	</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      username: '',
      password: '',
      name_msg: '',
      password_msg: '',
      md_password: ''
    }
  },
  mounted(){
    document.title = 'Login',
    this.ifLogin()
  },
  methods:{
    ifLogin:function() {
      var self = this;
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/login_or_not/',
        headers: Cookies.get('token')?{'Authorization': 'Token ' + Cookies.get('token')}:{},
      }).then(function(response) {
        window.location.href = '/#/'
      }).catch(function() {

      })
    },
  	clickName:function() {
  		var self = this;
  		self.name_msg = ''
  	},
  	clickPassword:function() {
  		var self = this;
  		self.password_msg = ''
  	},
  	logIn:function() {
  		var self = this;
  		axios.post('http://127.0.0.1:8000/api/login/', {
  			username: self.username,
  			password: md5(self.password)
  		}).then(function(response) {
  			Cookies.set('token', response.data.token,{ expires: 10});
  			window.location.href = "/#/"
  		}).catch(function(error) {
  			self.name_msg = '用户名或密码错误'
  		})
  	},
  	checkInfo:function() {
  		var self = this;
  		var check = true;
  		if (self.username == ''){
  			self.name_msg = '请输入手机号或邮箱';
  			check = false
  		}
  		if (self.password.length < 6){
  			self.password_msg = '请输入6位以上密码';
  			check = false
  		}
  		if (check == true){
  			this.logIn()
  		}
  	}
  }
}
</script>
