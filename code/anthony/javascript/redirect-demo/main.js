let timer = document.querySelector('#countdown-timer')
let iframe = document.querySelector('#iframe > iframe')
let playPause = document.querySelector('#pause-play')

let timeRemaining = 5
let urls = ["wikipedia.com", "dictionary.com", "thesaurus.com", "wikipedia.com/wiki/javascript", "wikipedia.com/wiki/python", "wikipedia.com/wiki/ruby"]

function random(){
    let i = Math.floor(Math.random() * urls.length)
    return "https://" + urls[i]
}

function startTimer(){

    let interval = setInterval(function () {
        timeRemaining--
        if (timeRemaining < 0){
            iframe.src = random()
            timeRemaining = 5
        } else {
            timer.innerText = `${timeRemaining}s until wormhole`
        }
    }, 1000)
    return interval
}

playPause.onclick = function() {
    if(playPause.innerText === 'Play'){
        interval = startTimer()
        playPause.innerText = 'Pause'
    } else {
        playPause.innerText = 'Play'
        clearInterval(interval)
    }
}

let interval = startTimer()