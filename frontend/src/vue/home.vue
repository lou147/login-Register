<template>
	<div class="main">
		<a class="header">HOME</a>
		<div class="login" v-show="loginOrNot">
			<h1>你已经登录</h1>
			<div>你的用户名：<span>{{username}}</span> </div>
			<div>你的昵称：<span>{{name}}</span> </div>
			<div>点击<a @click="logOut">这里</a>登出</div>
		</div>

		<div class="not-login" v-show="!loginOrNot">
			<div>你还未登录，去<a href="/#/login">登录</a></div>
		</div>
	</div>
</template>
	

<script>
import axios from 'axios'
export default {
  data () {
    return {
    	loginOrNot:'',
    	username: '',
    	name: ''
    }
  },
  mounted(){
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
  			self.username = response.data.username;
  			self.name = response.data.name;
  			self.loginOrNot = true
  		}).catch(function() {
  			self.loginOrNot = false
  		})
  	},
  	logOut:function() {
  		Cookies.remove('token')
  		location.reload()
  	}

  }
}
</script>