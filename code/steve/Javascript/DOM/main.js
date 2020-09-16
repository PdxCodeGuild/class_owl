

let div1 = document.querySelector('#div1');
div1.innerText = "TGIF";

let dive2 = document.querySelector('#div2');
dive2.innerHTML = "<h1>Partay!</h1>";


const panda = document.querySelector('#btn')


function newButton(){

    for (let i=0; i < (math.floor(math.random() * 5)); i++){
    button.addEventListener('click', function (){
        let btn = document.createElement('button')
        btn.innerText = "Click Me"
        btn.addEventListener('click', newButton)
        
        let container = document.querySelector('#container')
        container.appendChild(btn)
    }
}

