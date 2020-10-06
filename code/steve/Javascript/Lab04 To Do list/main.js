let itemTodo = document.getElementById('itemTodo')
let add = document.getElementById('add')
let todos = document.getElementById('tudos')
let card = document.getElementById('card')



add.addEventListener("click", addItem)


function addItem(){
    let card = document.createElement('div')
    let complete = document.createElement('button')
    let remove = document.createElement('button')
    let p = document.createElement('p')
    newItem = document.createElement('h3')
   
    
    card.id = 'card'
    newItem.innerText = 'To Do Item'
    p.innerText = itemTodo.value
    complete.innerText = 'Complete'
    complete.addEventListener("click", complete1)
    remove.innerText = 'Remove'
    remove.addEventListener("click", remove1)
    card.appendChild(newItem)
    card.appendChild(p)
    card.appendChild(complete)
    card.appendChild(remove)
    
    todos.appendChild(card)

    

}

function remove1(){
    let card = this.parentNode
    this.parentNode.parentNode.removeChild(card)

}

function complete1(){
    let card = this.parentNode
    card.childNodes[1].style.textDecoration = 'line-through'
    console.log(card.childNodes)

}