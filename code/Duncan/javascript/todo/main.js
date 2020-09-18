let form = document.getElementsByClassName("form")
let newItem = document.getElementById("newItem")
let add = document.getElementById("add")
let ilist = document.getElementsByClassName("ilist")
let delist = document.getElementsByClassName("delist")
delist = delist[0]
ilist = ilist[0]
form = form[0]


add.addEventListener("click", additem)

function additem(){
    console.log("hi")
    let newitem = newItem.value 
    
    
    let list = document.createElement("div")
    let listitem = document.createElement("h3")
    let done = document.createElement("button")
    let del = document.createElement("button") 
    
    list.className = "list"
    del.className = "delete"
    done.className = "finished"
    
    listitem.innerText = `${newitem}`
    list.appendChild(listitem)
    
    
    list.appendChild(done)
    list.appendChild(del)
    ilist.appendChild(list)
    done.innerText = "Finished"
    
    del.innerText = "DELETE"

    done.addEventListener("click", finishedI)

    function finishedI(){
        console.log("donesers")
        let dlist = document.createElement("div")
        let dlistI = document.createElement("h3")
        let del = document.createElement("button")

        delist.appendChild("dlist")
        dlist.appendChild("dlistI")
        dlist.appendChild("del")
    
        dlistI.innerText = `${listitem}`
    
    
    }
}











