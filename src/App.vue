<template>
  <div id="app">
      <top></top> 
      <shopping-cart></shopping-cart>
      <foot></foot>
  </div>
</template>

<script>
import Top from './components/Top' 
import ShoppingCart from './components/ShoppingCart'
import Foot from './components/Foot'
export default {
    name: 'app',
    components: {
        Top,
        ShoppingCart,
        Foot
    }
}
</script>

<style>
body,ol,ul,h1,h2,h3,h4,h5,h6,p,th,td,dl,dd.form.fieldset,legend,input,textarea,select{margin:0;padding:0;}
a{text-decoration:none;}
li{list-style:none;}
</style>
