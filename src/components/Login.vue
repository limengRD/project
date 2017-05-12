<template>
<div>
    <div class="login">
        <div class="login_box">
            <div class="login_box_title">
                <p>用户登录</p>
            </div>
            <div class="input-group login_margin">
                <span class="input-group-addon" id="basic-addon2">@</span>
                <input type="text" class="form-control" placeholder="Username" aria-describedby="sizing-addon2">
            </div>
            <div class="input-group login_margin">
                <span class="input-group-addon" id="basic-addon2">@</span>
                <input type="password" class="form-control" placeholder="Password" aria-describedby="sizing-addon2">
            </div>
            <div class="login_margin">
                <button type="button" class="btn btn-primary width_button">登录</button>
            </div>
        </div>
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
    .login_box_title{height:50px;}
    .login_box_title p{height:50px;line-height:50px;}
    .login{position:relative;background-color:red;height:600px;}
    .login_box{padding:30px;position:absolute;left:65%;top:50%;margin-top:-175px;float:right;border:15px;width:350px;height:350px;background-color:#fff;}
    .login_margin{margin-top:20px;}
    .width_button{width:290px;}
</style>