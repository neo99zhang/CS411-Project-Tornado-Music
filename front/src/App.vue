

<template>
  <div id="app">
    <router-link to='/'>Go Home</router-link>
    <router-link to='/about'>About</router-link>
    <router-view />
  </div>
</template>

<script>
var axios = require('axios');
export default {
  name: 'app',
  data () {
    return {
      msg: ''
    }
  },
  mounted() {
      axios.get('/api/hello')
  .then(response => this.msg = response.data.data)  }
}
</script>

<style>
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>