<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <header>
    <div class="wrapper">
      <HelloWorld />
    </div>
  </header>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=BIZ+UDPGothic&display=swap');
body {
  font-family: 'BIZ UDPGothic', sans-serif;
}
.wrapper {
  display: grid;
  grid-template-areas: 
    "map map map";
  grid-template-rows: 100vh;
  margin: 0;
  padding: 3px;
}

@media screen and (max-width:420px) {
    .wrapper {
      grid-template-areas: 
    "header header header"
    "data data data"
    "footer footer footer";
    }
}

</style>