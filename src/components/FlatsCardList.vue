<script setup>
import CardFlat from './CardFlat.vue';
</script>

<template>
  <div class="flat_list">
    <CardFlat />
    <CardFlat />
    <CardFlat />
  </div>
</template>

<style scoped>
.data_block {
    background-color:#FE5F55;
    grid-area: filter;
    padding: 0;
    display: grid;
    grid-gap: 1rem;
}
.test {
    text-align: center;
    color: white;
}

</style>
