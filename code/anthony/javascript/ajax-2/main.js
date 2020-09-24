let getRecipeButton = document.querySelector('#get-recipe')
let recipeBox = document.querySelector('#recipe')

let url = 'https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist'

// getRecipeButton.addEventListener('click', function(){
//     fetch('https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist')
//     .then(function(response){
//         // console.log(response.json())
//         return response.json()
//     })
//     .then(function(data){
//         // console.log(data)
//         if (data.type === "twopart"){
//             recipeBox.innerText = data.setup + " --- " + data.delivery
//         } else {
//             recipeBox.innerText = data.joke
//         }
//     })
//     console.log('Hey, did we get a response?')
// })

// getRecipeButton.addEventListener('click', async function(){
//     let response = await fetch('https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist')
//     let data = await response.json()
//     // console.log(data)

//     if (data.type === "twopart"){
//         recipeBox.innerText = data.setup + " --- " + data.delivery
//     } else {
//         recipeBox.innerText = data.joke
//     }

//     console.log("Hello")
// })

// getRecipeButton.addEventListener('click', function(){
//     axios.get(url)
//     .then(function(response){
//         if (response.data.type === "twopart"){
//             recipeBox.innerText = response.data.setup + " --- " + response.data.delivery
//         } else {
//             recipeBox.innerText = response.data.joke
//         }
//     })
// })

getRecipeButton.addEventListener('click', async function(){
    let response = await axios.get(url)
    
    if (response.data.type === "twopart"){
        recipeBox.innerText = response.data.setup + " --- " + response.data.delivery
    } else {
        recipeBox.innerText = response.data.joke
    }    
})