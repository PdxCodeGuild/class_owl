const API = "https://favqs.com/api/quotes"

let getQuote = document.querySelector("#get-quote")
let quote = document.querySelector("#quote")
let author = document.querySelector("#Author")
let id = document.querySelector("#ID")

getQuote.addEventListener("click", async function(){
    let page = document.querySelector("#page")
    let filt = document.querySelector("#filt")
    FI = filt.value
    pa = page.value



    let Auth = {
        headers: {
            Authorization: 'Token token="ac86928f59b6bb892c7d2bbd38bb771e"'
        }
    }
    let res = await axios.get(`https://favqs.com/api/quotes?filter=${FI}&pages=${pa}`, Auth)
    let data = res.data
    let stuff = ""
    for (let i of data.quotes){
        stuff = stuff + `<p>${i.body}-${i.author}</p>`
    }
    console.log(data.quotes)
    qs.innerHTML = stuff
    // let i = Math.floor(Math.random()* data.quotes.length)
    // quote.innerText = "Quote: " + data.quotes[i].body;
    // author.innerText = "Author: " + data.quotes[i].author;
    // id.innerText = "ID: " + data.quotes[i].id;
})