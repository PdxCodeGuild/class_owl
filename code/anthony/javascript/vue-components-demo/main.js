Vue.component('dropdown', {
    props: {
        title: String,
        things: Array,
        callback: Function,
    },
    methods:{
        execute: function(url){
            console.log(this.callback)
            if(this.callback){
                this.callback(url)
            }
        }
    },
    template: `
    <div class="dropdown col">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        {{title}}
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
        <a v-for="stuff in things" class="dropdown-item" v-on:click="execute(stuff.url)">{{stuff.name}}</a>
        </div>
    </div>
    `
})



let app = new Vue({
    el: '#app',
    data: {
        baseURL: 'https://www.dnd5eapi.co',
        races: [],
        classes: [],
        selectedRace: '',
        selectedClass: '',
        attributes: {
            CHA: 8,
            CON: 8, 
            DEX: 8, 
            INT: 8,
            STR: 8,
            WIS: 8,
        }
    },
    methods: {
        getRace: function(raceURL){
            let url = this.baseURL + raceURL
            axios.get(url)
            .then(function(response){
                // console.log(response.data)
                app.selectedRace = response.data
            })
        },
        getClass: function(classURL){
            let url = this.baseURL + classURL
            axios.get(url)
            .then(function(response){
                app.selectedClass = response.data
            })
        },
        increaseStat: function(stat){
            if(this.remaining > 0){
                this.attributes[stat] += 1
            }
        },
        decreaseStat: function(stat){
            if(this.attributes[stat] > 0){
                this.attributes[stat] -= 1
            }
        }
    },
    computed: {
        remaining: function(){
            let total = 0
            for(key in this.attributes){
                total += this.attributes[key]
            }

            return 55 - total
        }
    },
    created(){
        axios.get(this.baseURL + '/api/races/')
        .then(function(response){
            app.races = response.data.results
        })
        axios.get(this.baseURL + '/api/classes/')
        .then(function(response){
            app.classes = response.data.results
        })
    }
}) 