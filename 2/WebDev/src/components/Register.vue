<template>
    <div class="form">
        <span class="form_title">Sign up</span>
        <form>
            <div class="form_input">
                <i class="ri-user-line"></i>
                <input type="text" name="Username" placeholder="Username" id="username">
                <span class="bar"></span>
            </div>
            <div class="form_input">
                <i class="ri-mail-line"></i>
                <input type="email" name="Email" placeholder="Email" id="email">
                <span class="bar"></span>
            </div>
            <div class="form_input">
                <i class="ri-lock-line"></i>
                <input type="password" name="Password" placeholder="Password" id="password">
                <span class="bar"></span>
            </div>
            <div class="form_input">
                <i class="ri-lock-line"></i>
                <input type="password" name="ConfirmPassword" placeholder="Confirm Password" id="confirmpassword">
                <span class="bar"></span>
            </div>
            <button type="submit" class="form_button" @click.prevent="mainMenu()">Sign up</button>
            <p id="error" style="color: red"></p>
            <span class="form_switch"> Already have an account? <a @click="Login()">Login</a></span>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Register",
    data() {
        return {
            apiUrl: 'http://localhost:5000'  
        }
    },
    methods: {
        async mainMenu() {

            let username = document.getElementById("username").value;
            let email = document.getElementById("email").value;
            let password = document.getElementById("password").value;
            let confirmpassword = document.getElementById("confirmpassword").value;

            if(username && email && password){
                if(password == confirmpassword) {
                    try {

                        let response = await axios.post(`${this.apiUrl}/register`, {
                            username: username,
                            email: email, 
                            password: password
                        });


                        if(response.data.message === 'User registered successfully') {
                            this.$emit("changeState", 1);
                        }
                    } catch (error) {
                        document.getElementById("error").textContent = error.response.data.message || "Error registering user!";
                        setTimeout(() => {
                            document.getElementById("error").textContent = ""
                        }, 1500);
                    }
                } else {
                    document.getElementById("error").textContent = "Passwords aren't the same!"
                    setTimeout(() => {
                        document.getElementById("error").textContent = ""
                    }, 1500);
                }
            } else {
                document.getElementById("error").textContent = "Please fill in all fields!"
                setTimeout(() => {
                    document.getElementById("error").textContent = ""
                }, 1000);
            }
        },
        Login() {
            if(true) 
                this.$emit("changeState", 0)
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
    color: #fff;
    background-color: #fff;
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
    border: .5rem solid #fff;
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
    color: #a1a1a1;
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