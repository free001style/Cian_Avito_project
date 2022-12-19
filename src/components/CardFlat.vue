<script setup>
</script>

<template>
  <div class="card_flat">
    <h1 class="test">Flat card text</h1>
  </div>
</template>

<style scoped>
.card_flat {
    background-color:teal;
    grid-area: filter;
    height: 10rem;
    margin: 1rem;
    display: flex;
    justify-content: center;
    align-content: center;
    flex-direction: column;
}
.test {
    text-align: center;
    color: white;
}

</style>
