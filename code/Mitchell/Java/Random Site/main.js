let redirect = document.querySelector('.redirect')



function asiterandom() {
    let wsite = ['https://www.google.com/',
    'https://www.yahoo.com/',
    'https://www.twitch.com',
    'https://thehill.com'
    ]


let index = Math.floor(Math.random() * wsite.length)


let newSite = wsite[index]
return newSite
}


function gobble () {
    window.location = asiterandom()
}

setTimeout(gobble, 5000); 
    setTimeout(function(){ redirect.innerText = "5 seconds" }, 1000);
    setTimeout(function(){ redirect.innerText = "4 seconds" }, 2000);
    setTimeout(function(){ redirect.innerText = "3 seconds" }, 3000);
    setTimeout(function(){ redirect.innerText = "2 seconds" }, 4000);
    setTimeout(function(){ redirect.innerText = "1 seconds" }, 5000);
