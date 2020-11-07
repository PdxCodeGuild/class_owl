let app = new Vue({
    el: "#app",
    data: {
        contacts: [],
        firstName: '',
        lastName: '',
        phone: '',
        email: '',
        currentContact: null
    },
    methods: {
        addContact: function () {
            if (this.firstName === '' || this.lastName === '' || this.phone === '' || this.email === '') {
                return
            }

            this.contacts.push({
                name: this.firstName + " " + this.lastName,
                phone: this.phone,
                email: this.email
            })

            // this.firstName = ''
            // this.lastName = ''
            // this.phone = ''
            // this.email = ''
            this.firstName = this.lastName = this.phone = this.email = ''
        },
        deleteContact: function (i) {
            this.contacts.splice(i, 1)
        },
        editContact: function (i) {
            this.toggleModal()
            let contact = this.contacts[i]
            this.firstName = contact.name.split(' ')[0]
            this.lastName = contact.name.split(' ')[1]
            this.email = contact.email
            this.phone = contact.phone
            this.currentContact = i
        },
        saveContact: function () {
            this.contacts[this.currentContact] = {
                name: this.firstName + " " + this.lastName,
                email: this.email,
                phone: this.phone
            }

            this.toggleModal()
        },
        toggleModal: function () {
            let modal = document.querySelector('.modal')
            modal.classList.toggle('is-active')
            this.firstName = this.lastName = this.email = this.phone = ''
            this.currentContact = null
        }
    },
    async created() {
        let res = await axios.get('https://jsonplaceholder.typicode.com/users')

        for (contact of res.data) {
            let person = {
                name: contact.name,
                phone: contact.phone,
                email: contact.email
            }
            this.contacts.push(person)
        }
    }
})