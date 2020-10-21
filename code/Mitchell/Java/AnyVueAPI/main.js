let prg = new Vue({

    el: "#main",
    data: {
        ichooseyou: " ",
        pokeName: " "
    },
    methods: {
           PokePull: function () {
            axios.get(`https://pokeapi.co/api/v2/pokemon-form/${prg.ichooseyou}/`)
            .then(function (response) {
                console.log(response.data)
                let data = response.data.pokemon
                console.log(data)

                prg.pokeName = response.data.pokemon.name
            })
           }
    },
})