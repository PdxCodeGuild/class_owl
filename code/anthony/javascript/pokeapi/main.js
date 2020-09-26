const API = 'https://pokeapi.co/api/v2/pokemon/'

let searchInput = document.querySelector('#search-input')
let searchBtn = document.querySelector('#search-btn')
let image = document.querySelector('#poke-image')
let id = document.querySelector('#id')
let name = document.querySelector('#name')
let height = document.querySelector('#height')
let weight = document.querySelector('#weight')


searchBtn.addEventListener('click', async function(){
    // console.log(searchInput.value)
    let url = `https://pokeapi.co/api/v2/pokemon/${searchInput.value}`
    let response = await axios.get(url, headers)
    let data = response.data

    image.src = data.sprites.front_default
    id.innerText = data.id
    name.innerText = data.name
    height.innerText = data.height
    weight.innerText = data.weight
    
    console.log(data)
})
