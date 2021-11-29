<template>
<a>
<el-row>
  <el-col :span="8">
  <div class="tornado">
  <el-image style="width: 350px; height: 80px" :src="url"></el-image>
  </div></el-col>
  </div>
</el-row>
<el-row>
  <el-col :span="24"><el-input v-model="input" placeholder="Type the music"></el-input></div></el-col>
</el-row>
</a>
</template>


<script>
    
    export default {
       data() {
         return {
            
            url: 'https://media.istockphoto.com/vectors/tornado-storm-warning-handmade-lettering-vector-id1067276308?k=20&m=1067276308&s=170667a&w=0&h=5YMhX0-qX10w4JklVRekn2IWklumDZAOGhI_bAE9ZaU=',
            input: ''      
            }
       }
    }
</script>


