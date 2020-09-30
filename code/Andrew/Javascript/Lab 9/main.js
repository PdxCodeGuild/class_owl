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
                
                if( this.inputItem.length >0 && this.inputItem.length <=50){

                    toDo.push(
                        {inputItem: [this.inputItem, true]}
                        
                        )
                        console.log(toDo)
                        this.inputItem =''
                    }
                else if( this.inputItem.length >50) {
                    alert('Input must be less than 50 Characters')
                    this.inputItem = this.inputItem.slice(0,52)
                }
        },
        removeItem: function(i){
            this.toDoObject.splice(i,1)

        },

        removeDoneItem: function(i){
            this.toDoneObject.splice(i,1)
        },

        completeItem: function(i){
            let a = this.toDoObject.splice(i,1)
            console.log()
            this.toDoneObject.push(a[0]['inputItem'][0])
        
        },

        clearAll: function(){
            this.inputItem = ''
            this.toDoObject =  []
            this.toDoneObject = []
        },


        
    },


})