import Vue from 'vue'
import Router from 'vue-router'

import Index from '@/components/Index'
import Login from '@/views/Login'
import Logout from '@/views/Logout'
import ListBooks from '@/components/Books/List'
import EditBook from'@/components/Books/Edit'
import Experiments from '@/components/Experiments'
import ListCases from '@/components/Cases/List'
import CreateCases from '@/components/Cases/Create'
import EditCases from '@/components/Cases/Edit'
import ListMachines from '@/components/Machines/List'
import ListProblems from '@/components/Problems/List'





Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/books',
      name: 'ListBooks',
      component: ListBooks
    },
    {
      path: '/books/edit/:id',
      name: 'EditBook',
      component: EditBook
    },
    {
      path: '/experiments',
      name: 'Experiments',
      component: Experiments
    },
    {
      path: '/listcases',
      name: 'ListCases',
      component: ListCases
    },
    //{
      //path: '/cases/edit/:id',
      //name: 'EditCases',
      //component: EditCases
    // },
    {
      path: '/editcases',
      name: 'EditCases',
      component: EditCases
    },
    {
      path: '/machines',
      name: 'ListMachines',
      component: ListMachines
    },
    {
      path: '/problem',
      name: 'ListProblems',
      component: ListProblems
    }
  ]
})
