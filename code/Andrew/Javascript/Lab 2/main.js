let passLen = document.querySelector("#passLen")
let btn = document.querySelector("#passBtn")
let result = document.querySelector("#resultPassword")
let reIn1 = document.querySelector("#reInput1")
let reIn2 = document.querySelector("#reInput2")
let hider = document.getElementsByClassName("hide")
let verifyBtn = document.querySelector("#verify")
let body = document.querySelector("#output") 

btn.addEventListener("click", function() {
    var password = ''
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

    for (i of hider){
        console.log(i)
        i.classList.remove("hiders")
    }

    

})




verifyBtn.addEventListener('click',function(){
    console.log(result.innerText)

    console.log(reIn1.value)
    if(reIn1.value === reIn2.value && reIn2.value === result.innerText){
        
        let header = document.createElement("h1")
        let hB = document.createTextNode("Password Verfied to work!")
        header.appendChild(hB)
        
        body.appendChild(header)
        header.style.color = "green"
       

    }
    else{
        let header = document.createElement("h1")
        let hB = document.createTextNode("Passwords do not match!")
        header.appendChild(hB)
        
        body.appendChild(header)
        header.style.color = "red"

        reIn1.value = ""
        reIn2.value = ""
        console.log(result.innerText)
    }
    
})


