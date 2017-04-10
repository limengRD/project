<template>
    <div class="top">
        <div class="topBar">
            <div class="comWidth">
                <div class="leftArea">
                    <a v-text="key"></a>
                    <a href="">免费注册</a>
                </div>
            <div class="rightArea">
                    <a href="">我的淘宝</a>
                    <a href="">我的订单</a>
                    <a href="">收藏夹</a>
                    <a href="">商品分类</a>
                    <a href="">网站导航</a>
                </div>
            </div>
        </div>
        <div class="logoBar">
            <div class="comWidth">
                <div class="logo">
                    <a href="#"><img src="" alt=""></a>
                </div>
                <div class="search_box">
                    <input type="text" class="search_text">
                    <input type="button" value="搜索" class="search_button">
                </div> 
            </div>
        </div>
    </div>
</template>
<script>
   export default{
        name:"header",
        data () {
            return {
                key:"limeng"
            }
        }
    }
</script>
<style>
.top{height:130px;}
.topBar{height:31px;background-color:#f7f7f7;line-height:31px;box-shadow:0 0 1px 0 #8e8e8e}
.comWidth{width:1200px;margin-left:auto;margin-right:auto}
.leftArea a,.rightArea a{font-size:12px;color:#6c6c6c;margin-right:10px;}
.rightArea a:hover{color:red;}
.leftArea a:hover{color:red;}
.leftArea{float:left;}
.rightArea{float:right;}
.rightArea a{border-right:1px solid #6c6c6c;padding-right:6px}
.leftArea a:nth-of-type(1){color:red;font-weight:bold}
.logoBar{height:160px;padding-top:40px;}
.logo{float:left;}
.search_box{float:right;}
.search_text{width:300px;height:35px;padding-left:5px;padding-right:5px;float:left;border:#ff0000 solid 1px;}
.search_button{width:70px;height:37px;font-size:14px;font-family:"MicrosoftYaHei","微软雅黑";background-color:#ff0000;border:none;color:#fff;float:right;}
</style>
