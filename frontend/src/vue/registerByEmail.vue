<template>
	<div class="main-body">
		<div class="header">
			<a href="/#/">Home</a>
		</div>

		<form class="pure-form">
			<div class="head">
				<a id="nav" class="active">注册</a>
				<b>·</b>
				<a id="nav" href="/#/login">登录</a>
			</div>
			
			<fieldset class="pure-group">
				<div @click="clickNameInput" class="input-field">
					<label id="form-label">{{name_msg}}</label>
					<input v-model="name" type="text" class="pure-input-1" placeholder="你的昵称">
				</div>

				<div @click="clickPhoneInput" style="border-top: none;border-bottom: none" class="input-field">
					<label id="form-label">{{email_msg}}</label>
					<input v-model="email" type="text" class="pure-input-1" placeholder="邮箱">
				</div>

				<div @click="clickPasswdInput" class="input-field">
					<label id="form-label">{{passwd_msg}}</label>
					<input v-model="password" type="password" class="pure-input-1" placeholder="设置密码">
				</div>
		    </fieldset>

		    <a class="foot-menu" href="/#/register_phone">用手机号注册</a>
		    <span @click="checkInfo" id="btn" class="pure-button pure-input-1 pure-button-primary">注册</span>
		</form>
	</div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      name: '',
      email: '',
      password: '',
      name_msg: '',
      email_msg: '',
      passwd_msg: ''
    }
  },
  mounted(){
    document.title = 'Register',
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
    checkInfo:function() {
      var self = this;
      var check = true;
      // 验证
      if (self.name == ''){
        self.name_msg="请输入昵称";
        check = false;
      }
      // 邮箱正则
      var strreg=/^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	  if(self.email.search(strreg)==-1) { 
		self.email_msg = "请输入正确格式的邮箱";
		check = false;
	  } 

      if (self.password.length < 6){
        self.passwd_msg = "请输入大于6位的密码";
        check = false;
      }
      // 验证通过后注册
      if (check == true){
      	self.Register()
      }
    },
  	Register:function() {
  		var self = this;
  		axios.post('http://127.0.0.1:8000/api/register/', {
  			name: self.name,
  			email: self.email,
  			password: md5(self.password)
  		}).then(function(response) {
  			window.location.href = '/#/login'
  		}).catch(function() {
  			self.email_msg = "邮箱已被注册"
  		})
  	},
    clickNameInput:function() {
      var self = this;
      self.name_msg = ''
    },
    clickPhoneInput:function() {
      var self = this;
      self.email_msg = ''
    },
    clickPasswdInput:function() {
      var self = this;
      self.passwd_msg = ''
    },
  }
}
</script>

