<template>
<div>
    <div class="login">
        <div class="login_box"></div>
    </div>
</div>
</template>
<script>

    import jquery from 'jquery' 
    import Vue from 'vue'
    import VueResource from 'vue-resource' 
    Vue.use(VueResource)
    export default{
        name:"login",
        data () {
            return{

            } 
        },
        
    }
</script>
<style>
    .login{position:relative;background-color:red;height:600px;}
    .login_box{position:absolute;left:65%;top:50%;margin-top:-175px;float:right;border:15px;width:350px;height:350px;background-color:#fff;}
</style>