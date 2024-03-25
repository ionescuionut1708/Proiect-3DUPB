<template>
    <v-toolbar style="position: absolute; top: 0px; left: 0px; height: 7%; background: linear-gradient(to right, #FFCA08, #00356C);">
        <v-toolbar-title class="placeholder-text">Search your games</v-toolbar-title>
        <v-btn @click="Search()">
            <i class="mdi mdi-magnify">Search</i>
        </v-btn>
        <v-text-field single-line hide-details id="search" @input="Search()"></v-text-field>
        <v-btn @click="logout()" style="color:#FFCA08; ">
            <i class="mdi mdi-logout">Logout</i>
        </v-btn>
    </v-toolbar>
    <v-container style="position: absolute; left: 5%; right: 5%; background-color: azure; top: 7%">
        <v-row>
            <v-col v-for="i in count" :key="i" cols="3" :id="'element' + i">
                <v-card @click="scores(i)" max-width="400" height="400px">
                    <v-img :src="'http://127.0.0.1:5000/getImageById/' + games[i - 1].image" height="200px" cover></v-img>
                    <v-card-title class="my-card-title">{{ games[i - 1].title }}</v-card-title>
                    <v-card-text class="my-card-description">{{ games[i - 1].description }}</v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "Menu",
        data () {
            return {
                games: [],
                count: 0 
            }
        },
        mounted (){
            this.init()
        },
        methods: {
            async init () {
                const api = axios.create({
                baseURL: 'http://127.0.0.1:5000',
                headers: {
                    'ContentType': 'multipart/form-data'
                },
                timeout: 1000
                })
                
                const response = await api.get('/getGames') 
                this.games = response.data.result
                this.count = this.games.length;
            },
            Search () {
                for (var i = 0; i < this.count; i ++) {
                    if(this.games[i].title.toLowerCase().includes(document.getElementById("search").value.toLowerCase())){
                        document.getElementById('element' + (i + 1)).style.display = "block";
                    } else {
                        document.getElementById('element' + (i + 1)).style.display = "none";
                    }
                }
            },
            logout () {
                this.$emit("changeState", 0);
            },
            scores (pos) {   //selectGame ()
                if(this.games[pos - 1].title == "Balloons Madness") this.$emit("changeState", 6); //4
                else if(this.games[pos - 1].title == "Endless Runner") this.$emit("changeState", 6); //5
                
                this.$emit("selectGame", this.games[pos - 1].title);
            }
        }
    }
</script>

<style scoped>

.my-card-title {
  font-size: 18px; 
  margin-top: 10px;
}

.my-card-description {
  font-size: 14px; 
}
</style>