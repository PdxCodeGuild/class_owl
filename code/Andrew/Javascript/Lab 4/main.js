let inputItem = document.querySelector("#inputItem")
let addBtn = document.querySelector("#addBtn")
let addedItems = document.querySelector("#addedItems")
let completedItems = document.querySelector("#completedItems")


const addItems = function(event){
    console.log(inputItem.value)
    let toAdd = document.createElement("input type=checkbox")

    let toAddItem = document.createTextNode(inputItem.value)
    toAdd.appendChild(toAddItem)
    addedItems.appendChild(toAdd)
    




}


const removeItems = function(event){

}

addBtn.addEventListener("click",addItems)