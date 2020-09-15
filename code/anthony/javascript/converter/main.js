let input = document.querySelector('#input')
let inunits = document.querySelector('#inunits')
let outunits = document.querySelector('#outunits')
let output = document.querySelector('#output')


const conversion = {
    inches: .0254,
    feet: .3048,
    yard: .9144,
    miles: 1609.34,
    meter: 1,
    kilometer: 1000
}

function convertToMeters(distance, unit) {
    return distance * conversion[unit]
}

function convertToUnit(distance, unit){
    return distance / conversion[unit]
}

function handleConversion() {
    let unit = inunits.value
    let outunit = outunits.value
    let distance = input.value

    let convertedUnit = convertToMeters(distance, unit)
    convertedUnit = convertToUnit(convertedUnit, outunit)
    output.innerText = `${convertedUnit} ${outunit}`
}

inunits.addEventListener('input', handleConversion)
outunits.addEventListener('input', handleConversion)
input.addEventListener('keydown', function (event){
    if (event.key === "Enter"){
        handleConversion()
    }
})