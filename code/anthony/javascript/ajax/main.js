let button = document.querySelector('#get-quote')
let quote = document.querySelector('#quote')



// button.addEventListener('click', function(){
//     fetch('https://favqs.com/api/qotd')
//     .then(function(response){
//         return response.json()
//     })
//     .then(function(data){
//         quote.innerText = data.quote.body
//     })

//     console.log('hello')
// })

button.addEventListener('click', async function(){
    let response = await fetch('https://favqs.com/api/qotd')
    data = await response.json()

    quote.innerText = data.quote.body

    console.log('hello')
})