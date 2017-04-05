<template>
    <div id="shoppingcart">
        <div class="comWidth">
            <div class="title">
                <h3>购物车</h3> 
                <hr>
            </div>
            <div class="filter_Bar">
                <div class="good_Allcheck float_left total">
                    <input class="check" type="checkbox">
                    全选
                </div>
                <div class="good_information float_left total">商品信息</div>
                <div class="unit_price float_left total">单价</div>
                <div class="good_count float_left total">数量</div>
                <div class="total_price float_left total">金额</div>
                <div class="operation float_left total">操作</div>
            </div>
            <div class="goods_list">
                <ul>
                    <li v-for=""></li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
import Vue from "vue"
    export default{ 
        name:"shoppingcart",
         data () {
             return {
                 key:"aaa" ,
                 goods:{}    
             }
         }
  }
 
</script>
<style>
    .comwidth{width:1200px;margin:0 auto;}
    .title h3{text-align:center;color:red;}
    .title hr{height:3px;border:none;border-top:3px double red;}
    .float_left{float:left;}
    .total{height:50px;line-height:50px;font-size:14px;margin-left:20px;}
    .filter_Bar{height:50px;}
    .good_Allcheck{width:10%;}
    .good_information{width:35%;}
    .unit_price{width:10%;}
    .good_count{width:15%;}
    .total_price{width:15%;}
    .operation{widht:15%;}
</style>
