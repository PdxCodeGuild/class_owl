const API = "https://favqs.com/api/qotd"



let getQuote = document.querySelector("#get-quote")
let quote = document.querySelector("#quote")
let author = document.querySelector("#Author")
let ID = document.querySelector("#ID")

getQuote.addEventListener("click", async function(){

    let res = await axios.get(API)
    let data = res.data

    console.log(data)
    // quote.innerText = data.body
    // author.innerText = data.author
    // ID.innerText = data.id
})