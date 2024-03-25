<script setup>
import Login from './components/Login.vue'
import Meniu from './components/Meniu.vue'
import Register from './components/Register.vue'
import highScores from './components/highScores.vue'
import playGame from './components/playGame.vue'
</script>

<template>
  <div v-if="state == 0">
    <Login @changeState="state = $event" @username="user = $event"></Login>
  </div>
  <div v-else-if="state == 1">
    <Meniu @changeState="state = $event" @selectGame="game = $event"></Meniu>
  </div>
  <div v-else-if="state == 2">
    <Register @changeState="state = $event"></Register>
  </div>
  <div v-else-if="state == 3">
    <highScores @changeState="state = $event" :name="game" :user="user"></highScores>
  </div>
  <div v-else-if="state == 6"> <!-- ar fi starea = 6 -->
    <playGame @changeState="state = $event"></playGame>
  </div>
</template>

<script>
  export default {
    components: {
      Login,
      Meniu,
      Register,
      highScores
    },
    data () {
      return {
        state: 0,
        game: '',
        user: ''
      }
    }
  }
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
