let round_sb = document.getElementById('round')
let highScore_sb = document.getElementById('highscore')
let playerscore_sb = document.getElementById('playerscore')
let newgame = document.getElementById('new-game')
let startGame = document.getElementById('start-game')
let green = document.getElementById('green')
let red = document.getElementById('red')
let yellow = document.getElementById('yellow')
let blue = document.getElementById('blue')

let simon = []
let player = []
let round = 0
let highScore = 0
let currentScore = 0

function generateColor(){
    const colors = ["green", "red", "blue", "yellow"]
    const index = Math.floor(Math.random() * colors.length)
    return colors[index]
}

function game(){
    let simon = []
    let player = []
    let round = 0
    let highScore = 0
    let currentScore = 0

    while (true) {
        simon.push(generateColor())  
    }
    
}

newgame.addEventListener('click', game)