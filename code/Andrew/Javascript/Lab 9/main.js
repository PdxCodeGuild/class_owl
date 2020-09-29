let prg = new Vue({

    el: "#app",
    data: {
        inputItem:'',
        toDoObject: [],
        toDoneObject: [],
        ind: null,

    },

    methods: {

        addToList: function(){
            let toDo = this.toDoObject
            toDo.push(
                {inputItem: [this.inputItem, true]}

            )
            console.log(toDo)
            this.inputItem =''
        }
        
    },

    computed: {
        
    },


})