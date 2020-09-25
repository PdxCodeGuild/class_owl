let output = document.getElementById("clockOutput")
let header = document.querySelector("#head")
let dateOutput = document.querySelector("#date")
let stopwatch = document.querySelector("#watch")
let stopBtn = document.querySelector("#stopBtn")
let playBtn = document.querySelector("#startBtn")
let lapBtn = document.querySelector("#lapBtn")
let laps = document.querySelector("#laps")






console.log(output)
console.log(header)
setInterval(function(){

    let clock = new Date
    let a = clock.getHours()
    let b = clock.getMinutes()
    let c = clock.getSeconds()
    let d = clock.getUTCDate()

    dateOutput.innerText = `${clock.getUTCMonth()+1}/${d}/${clock.getFullYear()}`

    clockOutput.innerText = `${a}:${b}:${c}`
    
}, 1000)


let hate = new Date
hate.setHours(0,0,0,0)
stopwatch.innerText = `${hate.getHours()}:${hate.getMinutes()}:${hate.getSeconds()}`
let c = 0

function test() {
    if (c>=60){
        c = 0
    }
    c +=1
    console.log(c)
    hate.setSeconds(c)
    stopwatch.innerText = `${hate.getHours()}:${hate.getMinutes()}:${hate.getSeconds()}`
}

let timr

function stopWatch(){
    timr = setInterval(function(){
        if (c>=60){
            c = 0
        }
        c +=1
        console.log(c)
        hate.setSeconds(c)
        stopwatch.innerText = `${hate.getHours()}:${hate.getMinutes()}:${hate.getSeconds()}`
    }
    ,1000)
    console.log(timr)
    return timr
}

stopBtn.addEventListener('click', function(){
    if(playBtn.disabled === false){
        c = 0
        hate.setHours(0,0,0,0)
        stopwatch.innerText = `${hate.getHours()}:${hate.getMinutes()}:${hate.getSeconds()}`
        for (i of [...laps.children]){
            i.remove()
        }
    }
    
    
    clearInterval(timr)
    playBtn.disabled =false
})


playBtn.addEventListener("click", function(){
    playBtn.disabled = true
    stopWatch()

})

lapBtn.addEventListener('click',function(){
    let tester = stopwatch.innerText
    if (laps.children.length <5){
        let liEl = document.createElement('li')
        liEl.innerText = tester
        
        laps.appendChild(liEl)
    }
    else{
        let liEl = document.createElement('li')
        liEl.innerText = tester
        for (i of [...laps.children]){
            i.remove()
        }
        laps.appendChild(liEl)
        
    }





})



