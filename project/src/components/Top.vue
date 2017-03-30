<template>
    <div class="topBar">
        <div class="comWidth">
            <div class="leftArea">
                <a href="">亲，请登录</a>
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
</template>
<script>
   export default{
        name:"header",
        data () {
            return {
                key:""
            }
        }
    }
</script>
<style>
.topBar{height:31px;background-color:#f7f7f7;line-height:31px;box-shadow:0 0 1px 0 #8e8e8e}
.comWidth{width:1200px;height:125px;margin-left:auto;margin-right:auto}
.leftArea a,.rightArea a{font-size:12px;color:#6c6c6c;margin-right:10px;}
.rightArea a:hover{color:red;}
.leftArea a:hover{color:red;}
.leftArea{float:left;}
.rightArea{float:right;}
.rightArea a{border-right:1px solid #6c6c6c;padding-right:6px}
.leftArea a:nth-of-type(1){color:red;font-weight:bold}
</style>
