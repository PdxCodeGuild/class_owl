let passLen = document.querySelector("#passLen")
let btn = document.querySelector("#passBtn")
let result = document.querySelector("#resultPassword")
let reIn1 = document.querySelector("#reInput1")
let reIn2 = document.querySelector("#reInput2")
let hider = document.getElementsByClassName("hide")

 

btn.addEventListener("click", function() {
    let password = ''
    if (passLen.value >0 && passLen.value <=16){
        
        for (let i =0; i<passLen.value; i++){
            let x = Math.floor(Math.random() * (127 - 33) + 33)
            password += String.fromCharCode(x)

        }
        

    }
    else{
        alert("Invalid Input!")
    }


    result.innerText = password
    result.style.color = "red"
    result.style["font-size"] = "1.5rem"

    hider.classList.remove("hiders")

})




