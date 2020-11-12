let jump = document.getElementById("jump")
let timer = document.querySelector("#countdown-timer")
let iframe = document.querySelector("#iframe > iframe")
let pausePlay = document.querySelector("#pausePlay")
let container = document.querySelector("#iframe")



let timeremaining = 5
locales = ["https://www.flamesofwar.com/", "https://dnd.wizards.com/", "https://warhammer40000.com/" ]
let url = ["wikipedia.com","dictionary.com", "thesarus.com"]

container.getElementsByClassName.animation = 'animation: transition 2s ease 0s 2 alternate;'


setInterval(function (){
        timeremaining-- 
        if (timeremaining < 0 ){
            iframe.src = worm()
            timeremaining = 5
        } else {
            timer.innerText = `${timeremaining}s until jump through wormhole`
        }
    }, 1000)

    setTimeout(function(){
        iframe.classList.remove("shrink-grow")
    })

function worm(){
    let i = Math.floor(Math.random()*url.length)
         return "https://" + url[i]

}

// jump.addEventListener("click", () => {
//     locales = ["https://www.flamesofwar.com/", "https://dnd.wizards.com/", "https://warhammer40000.com/" ]
//     let jloc = Math.floor(Math.random()*locales.length);
//     window.location = locales[jloc];
// })

