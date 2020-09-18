let inputItem = document.querySelector("#inputItem")
let addBtn = document.querySelector("#addBtn")
let addedItems = document.querySelector("#addedItems")
let completedItems = document.querySelector("#completedItems")
let clearList = document.querySelector("#clearList")
let removeAll = document.querySelector("#removeAll")



const addItems = function(event){
    if (inputItem.value.trim() == ""){
        console.log(inputItem.value)
        return
    }
    console.log(inputItem.value)
    let listNode = document.createElement("li")
    let toAdd = document.createElement("button")
    listNode.classList.add("doList")

    toAdd.innerHTML = "<span>&#10003;</span>"
    toAdd.classList.add('doneBtn')

    toAdd.addEventListener('click', function(){

        this.innerText = ''
        let complete = this.parentNode.innerText
        let liComp = document.createElement('li')
        liComp.innerHTML = `<strike> ${complete} </strike>`
        completedItems.appendChild(liComp)
        this.parentElement.remove()


    })

    listNode.innerText= `${inputItem.value}`
    
    listNode.addEventListener('dblclick', function(){ 
        console.log(this)
        this.remove()
    })
    
    listNode.appendChild(toAdd)
    
    addedItems.appendChild(listNode)
    

    inputItem.value = ""
    inputItem.focus()


}


const removeItems = function(event){

}

addBtn.addEventListener("click",addItems)
inputItem.addEventListener("keyup", function(event){
    if (event.key === 'Enter'){
        addItems()
    } 
})
clearList.addEventListener('click', function (){
    for (x of [...completedItems.children]){
        x.remove()
    }
})


removeAll.addEventListener('click', function(){
    for (x of [...addedItems.children]){
        x.remove()
    }
})
