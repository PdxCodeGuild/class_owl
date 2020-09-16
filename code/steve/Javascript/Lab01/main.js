let input = document.getElementById('gradeNumber')
let gradeNumber = Number
let finalGrade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
let result    


function grades(){
    gradeNumber = input.value
    if (gradeNumber < 0){
        result = `<h1>Invalid Grade you PUTZ</h1>`   
    } else if (gradeNumber < 60){
        result = `<h1>${finalGrade[12]}</h1>`
    } else if (gradeNumber < 65) {
        result = `<h1>${finalGrade[11]}</h1>`
    } else if (gradeNumber == 65) {
        result = `<h1>${finalGrade[10]}</h1>`
    } else if (gradeNumber < 70) {
        result = `<h1>${finalGrade[9]}</h1>`
    } else if (gradeNumber < 75) {
        result = `<h1>${finalGrade[8]}</h1>`
    } else if (gradeNumber == 75) {
        result = `<h1>${finalGrade[7]}</h1>`
    } else if (gradeNumber < 80) {
        result = `<h1>${finalGrade[6]}</h1>`
    } else if (gradeNumber < 85) {
        result = `<h1>${finalGrade[5]}</h1>`
    } else if (gradeNumber == 85) {
        result = `<h1>${finalGrade[4]}</h1>`
    } else if (gradeNumber < 90) {
        result = `<h1>${finalGrade[3]}</h1>`
    } else if (gradeNumber < 95) {
        result = `<h1>${finalGrade[2]}</h1>`      
    } else if (gradeNumber == 95) {
        result = `<h1>${finalGrade[1]}</h1>`
    } else if (gradeNumber <= 100) {
        result = `<h1>${finalGrade[0]}</h1>`
        
    } else {result = `<h1>Invalid Grade you PUTZ</h1>`
    }

    let print = document.getElementById('final')
    print.innerHTML = result
}


let button = document.getElementById('eightBallAnswer')


function eightBallAnswer(){

    let answers = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
        ]
    
        let index = Math.floor(Math.random() * answers.length)
            result = `<h3>${answers[index]}</h3>`

        let print = document.getElementById('eightAnswer')
        print.innerHTML = result
}




function emoticon(){


    let eyes = [';', ':', '>', '%', '!', 'O']
    let nose = ['>', '-', '+', '=', '@', '<', '~']
    let mouth = ['>', 'X', 'S', ')', '(', 'D', 'Z']
    
    let index1 = Math.floor(Math.random() * eyes.length)
    let index2 = Math.floor(Math.random() * nose.length)
    let index3 = Math.floor(Math.random() * mouth.length)


    result = `<h1>${eyes[index1]} ${nose[index2]} ${mouth[index3]}</h1>`
    let print = document.getElementById('emoticon')
        print.innerHTML = result

}