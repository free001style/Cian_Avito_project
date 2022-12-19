<template>
      <div class="calc">
        <h3 class="calc_text">Калькулятор ипотеки</h3>
        <form>
          <div>
            <label class="calc_text">Первоначальный взнос: </label>
            <input class="input" type="number" id="first payment" min="1">
          </div>
          <div>
            <label class="calc_text">Сколько лет: </label>
            <input class="input" type="number" id="year" min="1" max="30">
          </div>

          <!--Кнопочки для банков -->
          <div>
            <p class="calc_text">ВТБ банк:</p>
            <div>
              <input type="radio" class="radio" id="Choice1"
              name="1" value="1">
              <label for="Choice1" class="calc_text"> Для семей с детьми </label>

              <input type="radio" class="radio" id="Choice2"
              name="2" value="2">
              <label for="Choice2" class="calc_text"> С госсподержкой </label>

              <input type="radio" class="radio" id="Choice3"
              name="3" value="3">
              <label for="Choice3" class="calc_text"> Для IT-специалистов </label>

              <input type="radio" class="radio" id="Choice4"
              name="4" value="4">
              <label for="Choice4" class="calc_text"> Обычная ставка </label><br>
            </div>
            <p class="calc_text">Альфа банк:</p>
            <div>
              <input type="radio"  class="radio" id="Choice1_"
              name="1" value="1">
              <label for="Choice1" class="calc_text"> Для семей с детьми </label>

              <input type="radio" class="radio" id="Choice2_"
              name="2" value="2">
              <label for="Choice2" class="calc_text"> 'Под залог' </label>

              <input type="radio" class="radio" id="Choice3_"
              name="3" value="3">
              <label for="Choice3" class="calc_text"> Обычная ставка </label>
            </div>

      <!-- кнопка всплывающего окошка-->
<!--            <button id="myBtn">Open Modal</button>-->

<!--              <div id="myModal" class="modal">-->
<!--                <div class="modal-content">-->
<!--                  <span class="close">&times;</span>-->
<!--                  <p>Some text in the Modal..</p>-->
<!--                </div>-->
<!--              </div>-->
          </div>>
        </form>
      </div>
ть
</template>

<script>
export default {
  el: 'calculator',
  methods: {
    Answer: function (message, picked) {
      if (picked == "Choice1") {
        var p = 5.7;
      }
      if (picked == "Choice2") {
        var p = 6.7;
      }
      if (picked == "Choice3") {
        var p = 4.7;
      }
      if (picked == "Choice4") {
        var p = 11.5;
      }
      if (picked == "Choice1_") {
        var p = 5.8;
      }
      if (picked == "Choice2_") {
        var p = 10.7;
      }
      if (picked == "Choice3_") {
        var p = 11.8;
      }
      var r  = 10000; /* цена квартиры */
      var s = message[0]; /* первоначальный взнос */
      var m = message[1]; /* количесво лет */
      var x = ((r - s) / 12*m) + p*0.01*(r - s)
      return x
    },
  },
}
</script>

<style scoped>
</style>
