<template>
  <v-toolbar style="position: absolute; top: 0px; left: 100px; height: 7%; background: linear-gradient(to right, #FFCA08, #00356C);">
      <v-app-bar-title>{{ user }}</v-app-bar-title>
  </v-toolbar>
  <v-btn @click="mainMenu()" style="position: absolute; top: 0px; left: 0px; height: 7%; background: linear-gradient(to right, #FFCA08, #00356C);">
      <i class="mdi mdi-keyboard-backspace" style="color: aliceblue;">Back</i>
  </v-btn>
  <v-table id="scores">
      <tr>
        <th>Username</th>
        <th>Score</th>
      </tr>
      <tr v-for="i in scores.length" :key="i">
        <td>{{ scores[i - 1].user }}</td>
        <td>{{ scores[i - 1].score }}</td>
      </tr>
  </v-table>
  <!-- <v-btn @click="updateScores()">Add Score</v-btn> -->
</template>

<script>
import axios from 'axios';

export default {
  name: "highScores",
  props: ['name', 'user'],
  data() {
  return {
    scores: [],
    score: ''
  }
},
  mounted() {
    this.init()
  },
  methods: {
    async init() {
      try {
        const api = this.createAxiosInstance();
        const response = await api.get('/getScoresByGameName/' + this.name);
        this.scores = response.data.result;
      } catch (error) {
        console.error("Error during initialization:", error);
      }
    },
    mainMenu() {
      this.$emit("changeState", 1);
    },
    async updateScores() {
  this.score = Math.floor(Math.random() * (100 - 50 + 1) + 50);

  const data = {
    game: this.name,
    user: this.user,
    score: this.score,
    _id: this._id 
  };

  let position = this.scores.findIndex(score => score.user === this.user);
  const method = position === -1 ? 'post' : 'put';

  try {
    const response = await axios[method]('http://127.0.0.1:5000/addScore', data);

  } catch (error) {
    console.error(`Error during ${method.toUpperCase()} request:`, error);
  }
},

createAxiosInstance() {
  return axios.create({
    baseURL: 'http://127.0.0.1:5000',
    timeout: 1000
  });
},

async getScore(id, index) {
  if (!id) {
    console.error('ID is undefined. Cannot fetch score.');
    return;
  }

  try {
    const api = this.createAxiosInstance();
    const response = await api.get('/getScoreById/' + id);

    if (this.scores[index]) { 
      this.scores[index]['score'] = response.data.result;
    } else {
      console.error("Cannot update score. Invalid index:", index);
    }
  } catch (error) {
    console.error("Error fetching the score by ID:", error);
  }
 }
  }
}
</script>

<style scoped>

#scores {
  position: absolute;
  right: 0px;
  left: 0px;
  top: 10%;
  width: 100%;
  border-collapse: collapse;
}

#scores td, #scores th {
  border: 1px solid #3E9ACD;
  padding: 10px;
  text-align: center;
}

#scores th {
  background-color: #F7D358;
  color: #3E9ACD;
  font-weight: bold;
}

#scores tr:nth-child(even) {
  background-color: #E0FFFF;
}

#scores tr:hover {
  background-color: #A9D0F5;
}

</style>