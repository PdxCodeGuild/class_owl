let getRecipeButton = document.querySelector('#get-recipe')
let recipeBox = document.querySelector('#recipe')

// getRecipeButton.addEventListener('click', function(){
//     fetch('https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist')
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(data){
//         if (data.type === "twopart"){
//             recipeBox.innerText = data.setup + "---" + data.delivery
//         } else        
//         recipeBox.innerText = data.joke
//     })
    
// })

getRecipeButton.addEventListener('click', async function(){
    let response = await fetch('https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist')
    let data = await response.json()
    if (data.type === "twopart"){
        recipeBox.innerText = data.setup + "---" + data.delivery
        } else {
            recipeBox.innerText = data.joke
        }
})