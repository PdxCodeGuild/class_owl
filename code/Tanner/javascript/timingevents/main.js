let stop = document.getElementById('stop')

// Settimeout with un named function
// setTimeout(function() {
//     alert("Hello from timeout")
// }, 3000)


//  Settimeout with named function
// setTimeout(sayHello, 3000)


function sayHello() {
    console.log('Hello!')
}

// Settimeout is non blocking code, javascript will continue to run
// console.log("Goodbye")

// Clear timeout example
// let timeout = setTimeout(sayHello, 3000)
// stop.addEventListener('click', function(){
//     clearTimeout(timeout)
//     console.log(`Stopped timeout: ${timeout}`)
// })


// let interval = setInterval(sayHello, 100)
// stop.addEventListener('click', function(){
//     clearInterval(interval)
//     console.log(`Stopped interval: ${interval}`)
//     window.location = 'https://google.com'
// })