import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import Home from './vue/home.vue'
import Register from './vue/register.vue'
import Login from './vue/login.vue'
import RegisterByEmail from './vue/RegisterByEmail.vue'
import './css/pure-min.css'
import './css/set.css'

Vue.use(VueRouter)

const router = new VueRouter({
	routes: [
		{ path: '/', component: Home },
		{ path: '/register_phone', component: Register },
		{ path: '/register_email', component: RegisterByEmail },
		{ path: '/login', component: Login }
	]
})


new Vue({
	el: '#app',
	router: router,
	data:{

	},

})

