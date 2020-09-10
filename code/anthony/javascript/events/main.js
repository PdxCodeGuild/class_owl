let inputHeader = document.getElementById('inputHeader')
let input = document.querySelector('#input')
let btn = document.querySelector('#updateHeader')
let growingDiv = document.querySelector('#growingDiv')
let position = document.querySelector('#position')


btn.addEventListener('click', function (){
    inputHeader.innerText = input.value
})

function grow(event){
    growingDiv.style.height = '400px'
    growingDiv.style.width = '400px'
    // console.log(event)
}

growingDiv.addEventListener('mouseenter', grow)

growingDiv.addEventListener('mouseleave', function (){
    growingDiv.style.height = '200px'
    growingDiv.style.width = '200px'
})

window.addEventListener('mousemove', function (event){
    let xpos = event.x
    let ypos = event.y
    position.innerText = `Position: ${xpos}x ${ypos}y`
})