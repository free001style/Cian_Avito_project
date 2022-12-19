<script setup>
import Filters from "./Filters.vue"
import FlatsCardList from "./FlatsCardList.vue"
</script>

<template>
  <div class="data_block">
    <Filters />
    <FlatsCardList />
  </div>
</template>

<style scoped>
.data_block {
    background-color:#F7F7FF;
    grid-area: data;
    padding: 0;
    display: grid;
    grid-template-areas: 
    "filters"
    "list";
    grid-template-rows: 12rem 1fr;
    grid-template-columns: 100%;  
}
.test {
    text-align: center;
    color: white;
}

</style>
