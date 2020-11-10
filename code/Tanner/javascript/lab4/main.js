let createTodo = document.getElementById('createTodo');
let inputTodo = document.getElementById('inputTodo');
let todoList = document.getElementById('todoList');
let todoCompleted = document.getElementById('todoCompleted');

createTodo.addEventListener('click', function(){
    let paragraph = document.createElement('div')
    paragraph.className = "col-sm bg-light text-center";
    let button = document.createElement('button');
    button.className = "btn btn-danger pull-right";
    button.innerText = 'X';
    paragraph.innerText = inputTodo.value;
    todoList.append(paragraph, button);
    inputTodo.value = "";
    button.addEventListener('click', function(){
        todoCompleted.appendChild(paragraph);
        todoCompleted.appendChild(button);
        paragraph.style.textDecoration = 'line-through';
    button.addEventListener('click', function(){
        todoCompleted.removeChild(paragraph);
        todoCompleted.removeChild(button);
    })
    })
});
