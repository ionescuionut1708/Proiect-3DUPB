<template>
    <div class="form">
        <span class="form_title">Login</span>
        <form>
            <!-- <div class="form__input">
                <i class="ri-user-line"></i>
                <input type="text" placeholder="Full Name">
                <span class="bar"></span>
            </div> -->
            <div class="form_input">
                <i class="ri-mail-line"></i>
                <input id="username" type="username" name="Username" placeholder="Username">
                <span class="bar"></span>
            </div>
            <div class="form_input">
                <i class="ri-lock-line"></i>
                <input id="password" type="password" name="Password" placeholder="Password">
                <span class="bar"></span>
            </div>
            <!-- <div class="form__input">
                <i class="ri-lock-line"></i>
                <input type="password" placeholder="Confirm password">
                <span class="bar"></span>
            </div> -->
            <p id="error" style="color: red"></p>
            <input type="submit" @click.prevent="mainMenu()" value="Login" class="form_button">
            <!-- <span>Login</span> -->
            <span class="form_switch"> Don't have an account? <a @click="Register()">Sign up</a></span>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "Login",
        data() {
            return {
                loggedIn: false,
                username: ''
            }
        },
        methods: {
            async mainMenu() {
                if(document.getElementById("username").value && document.getElementById("password").value){
                    
                    const username = document.getElementById("username").value;        
                    const password = document.getElementById("password").value;
                    
                    try {
                    const response = await axios.post('http://127.0.0.1:5000/login', {
                        username: username,
                        password: password 
                    });

                    if (response.status === 200) {
                        this.loggedIn = true;
                        this.username = username; // Setează numele userului autentificat
                        this.$emit("changeState", 1);
                        this.$emit('username', username);
                    } else {
                        document.getElementById("error").textContent = "Invalid credentials";

                        setTimeout(() => {
                            document.getElementById("error").textContent = "";
                        }, 1000);
                    }
                    } catch (error) {
                    console.error("Error during login:", error);
                    document.getElementById("error").textContent = "An error occurred";

                    setTimeout(() => {
                        document.getElementById("error").textContent = "";
                    }, 1000);
                    
                    }

                }
                else {
                    document.getElementById("error").textContent = "Please fill in all fields!"

                    setTimeout(() => {
                        document.getElementById("error").textContent = ""
                    }, 1000)
                }
            },
            Register() {
                if(true)
                    this.$emit("changeState", 2)
            }
        }
    }
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    font-size: 10px;
    font-family: 'Poppins', sans-serif;
}

body {
    font-size: 1.6rem;
    background-image: url('colored_shapes.svg');
    background-attachment: fixed;
    background-size: 100% 100%;
}

img {
    margin: auto;
    display: block;
    border-radius: 100%;
}

.form {
    position: relative;
    max-width: 40rem;
    padding: 10rem 0;
    /* color: #fff; */
    background-color: white;
    border-radius: 1rem;
    box-shadow: 0 1px 1rem rgba(0, 0, 0, .1);
    isolation: isolate;
    filter: blur(0);
}

.form::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 10rem;
    background: linear-gradient(to left,#FFCA08, #00356C);
    border-radius: 1rem 1rem 100% 100%;
    z-index: -1;
}

.form_title {
    position: absolute;
    top: 3.5rem;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2.5rem;
    color: white
}

.form>form {
    padding: 2.5rem;
    background-color: inherit;
}

.form_input {
    position: relative;
    display: flex;
    align-items: baseline;
    margin: 0 auto;
    padding: 0;
    background-color: white;
}

.form_input>i {
    font-size: 2rem;
    margin-right: 1rem;
    color: #007aec;
}

.form_input input {
    position: relative;
    width: 100%;
    font: inherit;
    padding: 1rem 0;
    margin-top: .5rem;
    border: none;
    outline: none;
}

.form_input .bar {
    position: absolute;
    left: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, .1);
    width: 100%;
    height: 1px;
}

.form_input .bar::before {
    content: "";
    position: absolute;
    background-color: #FFCA08;
    width: 100%;
    height: 2px;
    transform: scaleX(0);
    transform-origin: left;
    transition: transform .5s;
}

.form_input>input:focus+.bar::before {
    transform: scaleX(1);
}

.form_button {
    display: block;
    margin: 2.5rem auto 3rem;
    padding: 1rem 5rem;
    background: linear-gradient(to left, #FFCA08, #00356C);
    color: #fff;
    font: inherit;
    border: 0.5px solid black;
    outline: none;
    cursor: pointer;
    border-radius: 3rem;
}

.form_button:hover {
    background: linear-gradient(to right, #FFCA08, #00356C);
}

.form_switch {
    display: block;
    text-align: center;
    font-size: 1.5rem;
    color: black;
}

.form_switch a {
    text-decoration: none;
    color: #007aec;
}

.form_switch a:hover {
    text-decoration: underline;
}

@media screen and (min-width: 43.75em) {
    .form::before {
        height: 30rem;
    }

    .form__title {
        left: 10rem;
        transform: none;
    }

    .form>form {
        transform: translateX(10rem);
        border-radius: inherit;
        box-shadow: inherit;
    }
}
</style>