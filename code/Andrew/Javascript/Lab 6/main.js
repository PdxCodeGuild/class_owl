let output = document.getElementById("clockOutput")
let header = document.querySelector("#head")
let dateOutput = document.querySelector("#date")
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
    // console.log(new Date())
}, 1000)

