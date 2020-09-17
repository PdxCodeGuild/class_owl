let input = document.querySelector('#input')
let inUnits = document.querySelector('#inUnits')
let output =  document.querySelector('#output')
let outUnits = document.querySelector('#outUnits')

const conversion = {
    feet: .3048,
    miles: 1609.34,
    meter: 1,
    kilometer: 1000,
    yard: .0144,
    inches: .0254,
}

function convertToMeters(distance, unit) {
    return distance * conversion[unit]
}

function convertToUnit(distance, unit) {
    return distance / conversion[unit]
}

function handleConversion() {
    let unit = inUnits.value
    let outUnit = outUnits.value
    let distance = input.value

    let convertedUnit = convertToMeters(distance, unit)
    convertedUnit = convertToUnit(convertedUnit, outUnit)
    output.innerText = `${convertedUnit} ${outUnit}`
}

inUnits.addEventListener('input', handleConversion)
outUnits.addEventListener('input', handleConversion)
input.addEventListener('keydown', function (event){
    if (event.key === "Enter"){
        handleConversion()
    }
})

