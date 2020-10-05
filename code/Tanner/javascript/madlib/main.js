let name = document.getElementById('name')
let adjective = document.getElementById('adjective')
let animal = document.getElementById('animal')
let color = document.getElementById('color')
let noun = document.getElementById('noun')
let btn = document.getElementById('createMadlib')
let ouput = document.getElementById('output')


btn.addEventListener('click', function () {

    let madlib = `
    ${name.value} had a ${adjective.value} ${animal.value}
    It's fleece was ${color.value} as ${noun.value}, yeah
    Everywhere the child went
    The ${animal.value}, the ${animal.value} was sure to go, yeah
    He followed her to school one day
    And broke the teacher's rule
    And what a time did they have
    That day at school
    `
    
    output.innerText = madlib
    output.style.color = color.value
})


