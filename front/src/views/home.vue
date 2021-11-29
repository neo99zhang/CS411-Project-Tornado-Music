<template>
    <el-container style="height: 100%, width:100%">
    <el-aside width="auto"><common-aside></common-aside></el-aside>
    <el-container  >
        <el-header style="text-align: right"><common-header></common-header></el-header>
        <el-main>

        <el-row>
        <el-col :span="8">
        <el-image style="width: 350px; height: 80px" :src="url" :fit="fit"></el-image>
        </el-col>
        </el-row>

        <el-row>
        <el-col :span="24"><el-input v-model="input" placeholder="Type the music"></el-input></div></el-col>
        </el-row>

        
        </el-main>
    </el-container>
    </el-container>
</template>

<script>
import CommonAside from "../components/CommonAside.vue"
import CommonHeader from "../components/CommonHeader.vue"
import CommonMain from "../components/CommonMain.vue"

var axios = require('axios');
export default {
//   name: 'app',
//   data () {
//     return {
//       msg: ''
//     }
//   },
//   mounted() {
//       axios.get('/api/hello')
//   .then(response => this.msg = response.data.data)  }
    name: 'main',
    components: {CommonAside,CommonHeader,CommonMain},
    data() {
         return {
            
            url: 'https://media.istockphoto.com/vectors/tornado-storm-warning-handmade-lettering-vector-id1067276308?k=20&m=1067276308&s=170667a&w=0&h=5YMhX0-qX10w4JklVRekn2IWklumDZAOGhI_bAE9ZaU=',
            input: ''      
            }
       },
};
</script>

<style >


.el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  

  
  body > .el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  } 
</style>