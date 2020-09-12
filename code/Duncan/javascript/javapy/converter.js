// convert to meters

let Meters = document.getElementById("Meters")
let Feet = document.getElementById("Feet")
let Miles = document.getElementById("Miles")
let Kilometers = document.getElementById("Kilometers")
let Yards = document.getElementById("Yards")
let Inches = document.getElementById("Inches")
let Amount = document.getElementById("Amount")
let converted = document.getElementById("converted")
let Uconvert = document.getElementById("Uconvert")
let Units = document.getElementById("unit_selector")

Uconvert.addEventListener("click", event => {
    if (Units.value == "Meters") {
        converted.innerText = `${Amount.value} Meters is ${Amount.value * 1} Meters`
        console.log("clicky");
} 
    else if (Units.value == "Feet"){
        converted.innerText = `${Amount.value} Feet is ${Amount.value * 0.3048} Meters`
        console.log("clacky");
    }
    else if (Units.value == "Miles"){
        converted.innerText = `${Amount.value} Miles is ${Amount.value * 1609.34} Meters`
        console.log("clocky");
    }
    else if (Units.value == "Kilometers"){
        converted.innerText = `${Amount.value} Kilometers is ${Amount.value * 1000} Meters`
        console.log("clucky");
    }
    else if (Units.value == "Yards"){
        converted.innerText = `${Amount.value} Yards is ${Amount.value * 0.9144} Meters`
        console.log("clecky");
    }
    else if (Units.value == "Inches"){
        converted.innerText = `${Amount.value} Inches is ${Amount.value * 0.0254} Meters`
        console.log("clycky");
    }

}) 