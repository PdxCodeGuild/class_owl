let header = document.querySelector("#header")
let grade = document.querySelector("#gradeInput")
let result = document.querySelector("#result")
let btn = document.querySelector("#evaluate")


grade.focus()

window.addEventListener('keyup', function(event){
    if (event.key == "Enter"){
        
        
        btn.click()
        
    
    
    }
   
})

btn.addEventListener("click", function(){
    
    let gradeNum = grade.value
    let gradeAlpha 
    if (gradeNum !== '' && gradeNum <= 100 && gradeNum >=0) {
        if (gradeNum >89) {
            gradeAlpha = 'A'
        }
        else if(gradeNum >79){
            gradeAlpha = 'B'
        }
        else if(gradeNum >69){
            gradeAlpha = 'C'
        }
        else if (gradeNum >59) {
            gradeAlpha = 'D'
            
        }
        else{
            gradeAlpha = 'E'
        }  
    }
    
    else{
        alert("Enter a Valid Grade!")
        grade.value = ""
    }

    if (gradeAlpha) {
        
        result.innerText = `Your grade: ${gradeAlpha}`
        result.style.color = "white"
    
        setTimeout( ()=>{ grade.value = ""}, 500)
        setTimeout( ()=>{ result.innerText = ""}, 2000)
        grade.focus()
    }


})

