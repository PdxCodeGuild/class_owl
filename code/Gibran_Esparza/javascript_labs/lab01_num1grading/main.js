let score = document.getElementById('grade')
let btn = document.getElementById('generate')
let letter = document.getElementById('letter')

btn.addEventListener('click', function () {
    
   
    let letterGrade 
    
    if (score.value <= 100 && score.value >= 90){
        letterGrade = '<h1>You got an A</h1>';
    }else if ( score.value <= 89 && score.value >= 80 ){
        letterGrade = '<h1>You got a B</h1>';
    }else if ( score.value <= 79 &&  score.value >= 70 ){
        letterGrade = '<h1>You got a C</h1>';
    }else if ( score.value <= 69 && score.value >= 60 ){
        letterGrade = '<h1>You got a D</h1>';}
    else if (score < 60){
        letterGrade = "<h1>You Failed</h1<"
    }else
        letterGrade = "<h1> Please enter a Valid Number</h1>"
    
    letter.innerHTML= letterGrade

})

