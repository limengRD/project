<template>
    <div id="shoppingcart">
        <div class="comWidth">
            <div class="title">
                <h3>购物车</h3> 
                <hr>
            </div>
            <div class="filter_Bar">
                <div class="good_Allcheck float_left total">
                    <input type="checkbox" v-bind:class="{'checked':checkAllFlag}" v-on:click="checkAll()">
                    全选
                </div>
                <div class="good_information float_left total">商品信息</div>
                <div class="unit_price float_left total">单价</div>
                <div class="good_count float_left total">数量</div>
                <div class="total_price float_left total">总价值</div>
                <div class="operation float_left total">操作</div>
            </div>
            <ul class="ul_goods_list">
                <li v-for="item in items">
                    <div class="goods_list">
                        <div class="float_left good_Allcheck total">
                            <input type="checkbox" v-bind:checked="{'true':item.checked}" v-on:click="selectProduct(item)">
                        </div>
                        <div class="float_left good_information total">
                            <div class="">{{item.productName}}</div>
                        </div>
                        <div class="float_left unit_price total">
                            <div class="">￥{{item.productPrice}}</div>
                        </div>
                        <div class="float_left good_count total">
                            <div class="good_count_all">
                                <a v-on:click="doSubtraction(item)">-</a>
                                <input class="good_count_input" type="type" value="0" v-model="item.productQuentity">
                                <a v-on:click="doAdd(item)">+</a>
                            </div>
                        </div>
                        <div class="float_left total_price total">
                            <div class="">{{item.productPrice*item.productQuentity}}</div>
                        </div>
                        <div class="float_left operation total">
                            <div>
                                <a>删除</a>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
import jquery from 'jquery'
import Vue from "vue"
import VueResource from "vue-resource"
Vue.use(VueResource)
    export default{ 
         name:'shoppingcart',
         data () {
             return {
                 key:"aaa" ,
                 goods:{},
                 totalMoney:0,
                 items:[],
                 checkAllFlag:false   
             }
         },
         mounted:function(){
                this.cartView();
            },
         methods:{
            cartView:function(){
                var _this = this
                this.$http.get("/static/cartData.json").then(function(res){
                              console.log(res)
                             _this.totalMoney = res.body.result.totalMoney;
                             _this.items = res.body.result.list;
                        });
            },
            doSubtraction:function(item){
                if(item.productQuentity>1) 
                {
                    item.productQuentity = item.productQuentity-1;
                }
            },
            doAdd:function(item){
                item.productQuentity=item.productQuentity+1;
            },
            selectProduct:function(item){
                if(typeof item.checked == "undefined"){
                    Vue.set(item,"checked",true);
                }else{
                    item.checked = !item.checked;
                }
            },
            checkAll:function(){
                this.checkAllFlag = !this.checkAllFlag;
                var _this = this;
                    this.items.forEach(function(item,index){
                        if(typeof item.checked == 'undefined'){
                            _this.$set(item,"checked",_this.checkAllFlag);
                        }else{
                            item.checked = _this.checkAllFlag;
                        }
                    }); 
            }
        },
        watch:{
            item:function(a,b){
             
            }
        }
  }
 
</script>
<style>
    #shoppingcart{height:100%;}
    .comwidth{width:1200px;margin:0 auto;}
    .title h3{text-align:center;color:red;}
    .title hr{height:3px;border:none;border-top:3px double red;}
    .float_left{float:left;}
    .total{height:50px;line-height:50px;font-size:14px;margin-left:20px;}
    .filter_Bar{height:50px;background-color:#cdcdcd;}
    .good_Allcheck{width:10%;}
    .good_information{width:35%;}
    .unit_price{width:10%;}
    .good_count{width:15%;}
    .total_price{width:15%;}
    .operation{widht:15%;}
    .goods_list ul li{height:20px;width:}
    .ul_goods_list li{height:80px;border:1px solid #cdcdcd;margin-top:30px;}
    .good_count_input{float:left;width:30px;text-align:center;height:20px;}
    .good_count a{user-select:none;padding:0px;float:left;height:20px;line-height:20px;width:20px;background-color:#cdcdcd;text-align:center;box-sizing:border-box;}
    .good_count a:hover{cursor:pointer;border:1px solid red;color:red;}
    .good_count_all{height:20px;margin-top:15px;}
</style>
