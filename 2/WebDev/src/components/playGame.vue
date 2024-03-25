<template>
  <div>
    <v-toolbar style="position: absolute; top: 0px; left: 0px; height: 7%; background: linear-gradient(to right, #FFCA08, #00356C);">
        <v-app-bar-title>{{ gameName }}</v-app-bar-title>
    </v-toolbar>
    <v-btn @click="viewHighScores()" style="position: absolute; right: 20px; top: 2%; background: linear-gradient(to right, #FFCA08, #ff6a00);"> View High Scores </v-btn>
    <v-btn @click="back_to_menu()" style="position: absolute; left: 20px; top: 2%; background: #6ab2ff;">
        <i class="mdi mdi-chevron-double-left">Menu</i>
    </v-btn>
  </div>
</template>

<script>
import * as THREE from 'three'
import { CSS2DRenderer, CSS2DObject } from 'three/examples/jsm/renderers/CSS2DRenderer'

export default {
  name: "Endless Runner",
  props: ['gameName', 'user'],
  mounted(){
    this.init()

    window.addEventListener('beforeunload', this.handleUnload);
  },
  data(){
    return {
        keyboard: {},
        playerSpeed: 0.1,
        spawnPoint: new THREE.Vector3(5, -1.25, 1),
        time: 0,
        sprites: [],
        playerState: 0,
        playerCounter: 0,
        jumpDuration: 1, // durata săriturii
        isJumping: false, // dacă player-ul sare sau nu
        jumpCounter: 0, // contor pentru săritură
        highScore: 0, // pentru a păstra scorul
        obstacles: ['public/rock.png', 'public/tree.png'],
        respawnDistance: 0.1,
        isPlaying: true // flag pentru a verifica dacă jocul este în desfășurare 
    }
  },
  methods: {
    init() {

    //event listeners
    window.addEventListener('keydown', this.keyDown.bind(this));
    window.addEventListener('keyup', this.keyUp.bind(this));


      /* Create scene */
    this.scene = new THREE.Scene() 
   
    //get clock
    this.clock = new THREE.Clock()

    //create camera
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000)
    this.camera.position.y = 1.5
    this.camera.position.z = 5
    this.camera.lookAt(new THREE.Vector3(0, 1, 0))
    
    //background
    var textureLoader = new THREE.TextureLoader()
    var backgroundTexture = textureLoader.load("public/background2d.jpg")
    backgroundTexture.wrapS = THREE.RepeatWarapping

    this.backgroundMesh = new THREE.Mesh(
        new THREE.PlaneGeometry(20, 10, 100, 100),
        new THREE.MeshBasicMaterial({
            map: backgroundTexture
        })
    )
 
    this.backgroundMesh.position.y = 1
    this.scene.add(this.backgroundMesh)

    /* Player */ 
    this.sprites.push(textureLoader.load('public/1.png'))
    this.sprites.push(textureLoader.load('public/2.png'))
    this.sprites.push(textureLoader.load('public/3.png'))
    this.sprites.push(textureLoader.load('public/4.png'))

    this.playerMesh = new THREE.Mesh(
        new THREE.PlaneGeometry(1, 1, 50, 50), 
        new THREE.MeshBasicMaterial({ 
            map: this.sprites[this.playerState], 
            transparent: true
        })
    )

    this.playerMesh.position.x = -3.5
    this.playerMesh.position.y = -1 
    this.playerMesh.position.z = 1

    this.scene.add(this.playerMesh)

    //obstacle
    const randomObstacleIndex = Math.floor(Math.random() * this.obstacles.length);
    this.rock = new THREE.Mesh (
    new THREE.PlaneGeometry(1, 1, 50, 50), 
    new THREE.MeshBasicMaterial({ 
        map: textureLoader.load(this.obstacles[randomObstacleIndex]), 
        transparent: true
    })
    )

    this.rock.position.x = this.spawnPoint.x
    this.rock.position.y = this.spawnPoint.y
    this.rock.position.z =this.spawnPoint.z

    this.scene.add(this.rock)
    
    //test renderer
    this.timerDiv = document.createElement('div')
    this.timerDiv.id = 'timerDiv'
    this.timerDiv.textContent = 'Time: 0'
    this.timerDiv.style.backgroundColor = 'transparent'
    this.timerDiv.style.fontSize = '30px'

    const timerLabel = new CSS2DObject(this.timerDiv)
    timerLabel.position.set(0, 0, 0)
    this.scene.add(timerLabel)
    timerLabel.layers.set(0)
    
    this.labelRenderer = new CSS2DRenderer()
    this.labelRenderer.setSize(window.innerWidth * 15 / 100, window.innerHeight * 5 / 100)

    this.labelRenderer.domElement.id = "timerLabel"
    this.labelRenderer.domElement.style.color = 'black'
    this.labelRenderer.domElement.style.position = "absolute"
    this.labelRenderer.domElement.style.left = "5%" 
    this.labelRenderer.domElement.style.top = "10%"
    document.body.appendChild(this.labelRenderer.domElement)

    /* Renderer Setup */
    this.renderer = new THREE.WebGLRenderer()
    this.renderer.setSize(window.innerWidth * 90 / 100, window.innerHeight * 90 / 100)
    document.body.appendChild(this.renderer.domElement)

    this.renderer.domElement.id = "canvas"
    this.renderer.domElement.style.position = "absolute"
    this.renderer.domElement.style.left = "5%" 
    this.renderer.domElement.style.right= "5%"
    this.renderer.domElement.style.top = "10%"

    this.animate()
    },

    animate() {

        if (!this.isPlaying) {
            return; // dacă jocul nu este în desfășurare, oprește animația
        }

        requestAnimationFrame(this.animate)

        this.delta = this.clock.getDelta()
        this.backgroundMesh.material.map.offset.x += this.playerSpeed * this.delta
        this.time += this.delta
        this.playerCounter += this.delta
        this.timerDiv.textContent = 'Time: ' + this.time.toFixed(1).toString()

        //rock obstacle movment
        this.rock.position.x -= this.playerSpeed * this.delta * 10

        //delete obstacle
        if(this.rock.position.x < -5)
        {
            //drop material
            this.rock.material.dispose()
            //drop geometry
            this.rock.geometry.dispose()
            //remove
            this.rock.removeFromParent()

            //respawn
            this.spawnObstacle();
        }

        //player - obstacole collision
        var playerBoundingBox = new THREE.Box3().setFromObject(this.playerMesh)
        var rockBoundingBox = new THREE.Box3().setFromObject(this.rock)
        var collision = playerBoundingBox.intersectsBox(rockBoundingBox)

        if (collision == true) 
        {
            console.log("game over")
        }

        //player update
        if(this.playerCounter >= 1){
            this.playerCounter = 0
            this.playerState += 1
            this.playerState %= 4
            this.playerMesh.material.map = this.sprites[this.playerState]
        }

        if(this.keyboard[39]){
            if(this.playerSpeed < 0.5)
                this.playerSpeed += 2 * this.delta 
        } else {
            if(this.playerSpeed > 0.1)
                this.playerSpeed -= 2 * this.delta
        }

        // Verificare pentru jump
        if (this.isJumping) {
                this.jumpCounter += this.delta;
                if (this.jumpCounter < this.jumpDuration / 2) {
                    this.playerMesh.position.y += 0.05; // reglați această valoare pentru înălțimea săriturii
                } else {
                    this.playerMesh.position.y -= 0.05;
                }
                if (this.jumpCounter >= this.jumpDuration) {
                    this.isJumping = false;
                    this.jumpCounter = 0;
                    this.playerMesh.position.y = -1; // poziția originală
                }
            }

        // verificare coliziune / game over
        if (collision == true) {
                this.gameOver();
            }

        this.renderer.render(this.scene, this.camera)
        this.labelRenderer.render(this.scene, this.camera)
    },

    keyDown(event){
        this.keyboard[event.keyCode] = true;

        if (event.keyCode == 38 && !this.isJumping) { // ArrowUp
            this.jump();
        }
    },

    keyUp(event){
        this.keyboard[event.keyCode] = false;
    },

    spawnObstacle() {
    const textureLoader = new THREE.TextureLoader()
    const randomObstacleIndex = Math.floor(Math.random() * this.obstacles.length);
    this.rock = new THREE.Mesh(
        new THREE.PlaneGeometry(1, 1, 50, 50), 
        new THREE.MeshBasicMaterial({ 
            map: textureLoader.load(this.obstacles[randomObstacleIndex]), 
            transparent: true
        })
    )

    this.rock.position.x = this.spawnPoint.x
    this.rock.position.y = this.spawnPoint.y
    this.rock.position.z = this.spawnPoint.z

    this.scene.add(this.rock)
    },

    jump() {
        this.isJumping = true;
        this.jumpCounter = 0;
    },

    gameOver() {
        this.isPlaying = false; // oprește jocul
        console.log("game over");
        this.highScore = this.time;
        this.time = 0;
        alert("Game Over. High Score: " + this.highScore.toFixed(1));
    },

    handleUnload() {
        this.isPlaying = false; // oprește jocul atunci când se părăsește pagina
    },
    
    beforeDestroy() {
        window.removeEventListener('beforeunload', this.handleUnload);
    },

    viewHighScores() {
        this.$emit("changeState", 3);
        document.getElementById('canvas').remove()
        document.getElementById('timerLabel').remove()
        document.getElementById('timerDiv').remove()
    },

    back_to_menu() {
        this.$emit("changeState", 1);
        document.getElementById('canvas').remove()
        document.getElementById('timerLabel').remove()
        document.getElementById('timerDiv').remove()
    }
  }
}
</script>

<style scoped>

</style>