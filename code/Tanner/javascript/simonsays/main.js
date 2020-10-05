let round_sb = document.getElementById('round')
let highScore_sb = document.getElementById('high-score')
let playerScore_sb = document.getElementById('player-score')
let newGame = document.getElementById('new-game')
let startGame = document.getElementById('start-game')
let green = document.getElementById('green')
let red = document.getElementById('red')
let yellow = document.getElementById('yellow')
let blue = document.getElementById('blue')




function generateColor(){
    const colors = ["green", "red", "yellow", "blue"]
    const index = Math.floor(Math.random() * colors.length)
    return colors[index]
}

function simonSays(colors){
    for (let i in colors) {
        setTimeout(function () {
            if (colors[i] === 'green'){
                green.classList.add('current')
                setTimeout(() => green.classList.remove('current'), 500)
            } else if (colors[i] === 'red') {
                red.classList.add('current')
                setTimeout(() => red.classList.remove('current'), 500)
            } else if (colors[i] === 'yellow') {
                yellow.classList.add('current')
                setTimeout(() => yellow.classList.remove('current'), 500)
            } else if (colors[i] === 'blue') {
                blue.classList.add('current')
                setTimeout(() => blue.classList.remove('current'), 500)
            }
            console.log(colors[i])
        }, i+1*500)
    }

}


function game(){
    let simon = []
    let player = []
    let round = 0
    let highScore = 0
    let currentScore = 0

    simonSays(["red", "yellow", "green", "blue"])
    
    
}

newGame.addEventListener('click', game)