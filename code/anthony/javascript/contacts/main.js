let fname = document.getElementById('fname')
let lname = document.getElementById('lname')
let phone = document.getElementById('phone')
let email = document.getElementById('email')
let add = document.getElementById('add')
let contacts = document.getElementsByClassName('contacts')
contacts = contacts[0]


add.addEventListener('click', addContact)


function addContact() {
    let firstName = fname.value
    let lastName = lname.value
    let phoneNumber = phone.value
    let emailAddress = email.value

    let card = document.createElement('div')
    let h3 = document.createElement('h3')
    let h4 = document.createElement('h4')
    let p1 = document.createElement('p')
    let p2 = document.createElement('p')
    let btn = document.createElement('button')
    let favorite = document.createElement('button')
    let update = document.createElement('button')

    card.className = 'card'

    h3.innerText = `First Name: ${firstName}`
    card.appendChild(h3)
    h4.innerText = `Last Name: ${lastName}`
    card.appendChild(h4)
    p1.innerText = `Phone Number: ${phoneNumber}`
    card.appendChild(p1)
    p2.innerText = `Email: ${emailAddress}`
    card.appendChild(p2)

    btn.addEventListener('click', function() {
        contacts.removeChild(this.parentElement)
    })
    btn.innerText = 'Delete'

    favorite.addEventListener('click', function () {
        this.parentElement.classList.toggle('favorite')
    })
    favorite.innerText = 'Favorite'

    update.addEventListener('click', function() {
        fname.value ? this.parentElement.children[0].innerText = `First Name: ${fname.value}` : ''
        this.parentElement.children[1].innerText = `Last Name: ${lname.value}`
        this.parentElement.children[2].innerText = `Phone Number: ${phone.value}`
        this.parentElement.children[3].innerText = `Email: ${email.value}`

        fname.value = ''
        lname.value = ''
        phone.value = ''
        email.value = ''
    })
    update.innerText = 'Update'

    card.appendChild(btn)
    card.appendChild(favorite)
    card.appendChild(update)

    contacts.appendChild(card)

    fname.value = ''
    lname.value = ''
    phone.value = ''
    email.value = ''
}