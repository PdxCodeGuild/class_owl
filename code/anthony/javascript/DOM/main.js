
let div1 = document.querySelector('#div1');
div1.innerText = "TGIF";

let div2 = document.querySelector('#div2');
div2.innerHTML = "<h1>Partay!</h1>";


const button = document.querySelector('#btn')


function newButton(){
    
    for (let i=0; i < (Math.floor(Math.random() * 5)) + 1; i++){
        let btn = document.createElement('button')
        btn.innerText = "Click Me"
        btn.addEventListener('click', newButton)
        
        let container = document.querySelector('#container')
        container.appendChild(btn)
    }
}

button.addEventListener('click', newButton)
