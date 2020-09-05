let number = 4.2    //number
let day = 3         //number
let month = "Sept"  //string
// let year = null     //null

// alert("Todays date is " + day + " " + month + " " + year)


const make = document.querySelector('#make')
const model = document.querySelector('#model')
const year = document.querySelector('#year')
const color = document.querySelector('#color')
let submitButton = document.querySelector('#submitButton')


const updateUser = () => {
// function updateUser() {
    let user = {
        make: "",
        model: "",
        year: "",
        color: ""
        }

    // console.log("I clicked")
    user.make = make.value
    user.model = model.value
    user.year = year.value
    user.color = color.value


    let output = `
        <table>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
            </tr>
            <tr>
                <td>${user.make}</td>
                <td>${user.model}</td>
                <td>${user.year}</td>
                <td>${user.color}</td>
            </tr>
        </table>
    `
    document.write(output)
}

// submitButton.addEventListener('click', console.log('click'))