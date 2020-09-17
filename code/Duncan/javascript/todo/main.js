let intro = document.querySelector("#intro")
let firstI = document.querySelector("#firstI")
let create = document.querySelector("#create")
let usrInp = document.querySelector("#usrInp")
let todo = document.querySelector(".todo")


function Ilist() {
    let newItem = document.createElement("input");
    newItem.className = "todo";
    document.getElementById("usrInp").appendChild(newItem)
}
create.addEventListener("click", Ilist)


function del() {
    let delItem = usrInp.removeChild()
}






