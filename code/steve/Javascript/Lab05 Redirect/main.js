
function sitePicker() {

    let wsite = ['https://www.whitehouse.org/',
    'https://www.whitehouse.com/',
    'https://www.whitehouse.net/',
    'https://www.whitehouse.cam/',
    'https://www.whitehouse.gov/']



    let index = Math.floor(Math.random() * wsite.length)

    let randoSite = wsite[index]
    return randoSite

}

// setInterval(function() {
//     alert("You will be redirected after 5 seconds")
// }, 1000)

setTimeout( function() {
    window.location = sitePicker()}, 5000)

// window.location = 'http://www.google.com'
console.log('anything')