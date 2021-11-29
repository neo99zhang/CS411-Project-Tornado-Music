<template>
<el-menu  class="el-menu-vertical-demo"  :collapse="isCollapse"
background-color="#545c64"
text-color="#fff"
active-text-color="ffd04b"

>


  <h3>Tornado Link</h3>

    <el-menu-item :index="item.label" v-for="item in nochildren" :key="item.path"
    @click="clickMenu(item)"
    >
    <i :class="item.icon"></i>
    <span slot="title">{{item.label}}</span>
  </el-menu-item>


  <el-submenu index="1" v-for="item in haschildren" :key="item.path" @click="clickMenu(item)">
    <template slot="title">
    <i :class="item.icon"></i>
      <span slot="title">{{item.label}}</span>
    </template>
    <el-menu-item-group>
      
      <el-menu-item :index="subItem.path" v-for="(subItem,subIndex) in item.children" :key='subIndex'
      @click="clickMenu(subItem)">
      <i :class="subItem.icon"></i>
      <span slot="title">{{subItem.label}}</span>
      </el-menu-item>

    </el-menu-item-group>

    </el-submenu>
  </el-submenu>


</el-menu>
</template>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 250x;
    min-height: 200px;
  }
</style>

<script>
  export default {
    data() {
      return {
        isCollapse: false,
        menu:[
        {
          path : '/',
          name : 'home',
          label : 'home',
          icon : 's-home',
          url: '/home',
          icon: 'el-icon-s-home',

        },
        {
          path : '/custom_search',
          name :'custom search',
          label : 'custom search',
          icon : 'el-icon-search',
          url: '/about',
        },

        {
        label: 'user',
        icon: 'el-icon-user-solid',
        children:[

        {
          path : '/user/library',
          name :'user library',
          label : 'Library',
          icon : 'el-icon-collection-tag',
          url: '/about',
        },

        {
          path : '/user/friends',
          name :'user friends',
          label : 'Friends',
          icon : 'el-icon-chat-line-round',
          url: '/about',
        },
        {
          path : '/user/recommendation',
          name :'user rec',
          label : 'Recommendation',
          icon : 'el-icon-bangzhu',
          url: '/about',
        },
        ],
        },
        ],



      };
    },
    methods: {
      // handleOpen(key, keyPath) {
      //   console.log(key, keyPath);
      // },
      // handleClose(key, keyPath) {
      //   console.log(key, keyPath);
      // },
      clickMenu(item){
        this.$router.push({name:item.name})
      }
    },
    computed: {
      nochildren(){
        return this.menu.filter((item)=>!item.children);
      },
      haschildren(){
        return this.menu.filter((item)=>item.children);
      }

    }
  }
</script>


