let body = document.querySelector('#test')
let apiBtn = document.querySelector('#apiBtn')


apiBtn.addEventListener("click", function(){
    let a = fetch(apiUrl)
    .then(function(response){
        return response.json
    })
    .then(function(data){
        console.log(data)
    })
})









// API Section Start **************
let apiUrl = 'https://api.teleport.org/api/cities/?search=san%20francisco'




// API Section End