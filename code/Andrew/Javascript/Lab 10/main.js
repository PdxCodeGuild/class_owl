let app = new Vue({
    el: '#app',
    data:{
        input:'',
        evaled: false,
        clearIt: false

    },
    methods: {
        calcEval: function(){
            let fndr = /\d/i
            let temp = this.input[this.input.length-1]
            if(this.input && fndr.test(temp)){

                this.input = math.evaluate(this.input)
                this.input = this.input.toString()
            }

            this.evaled = true

        },
        inputMod: function(num){
            if("/+*-".indexOf(num) !== -1 && this.input.length === 0 || num === "/100" && this.input.length === 0){
                return 
            }
            else{
                
                 if(this.evaled && '1234567890'.indexOf(num) !== -1){
                    this.input = ''
                    this.evaled = false
                }
                else if('+-/*'.indexOf(num) !== -1 || num === "/100"){
                    this.evaled = false
                }
                
                this.input += num

            }
        },
        negatizer: function(){

            
            let temp2 = true

            let temp = this.input.split("")
            temp - temp.reverse()

            for (let x in temp){
                if (temp[x] === "+"){
                    temp[x] = '-'
                    temp2 =false
                    break
                }
                else if(temp[x] === '-'){
                    temp[x]= '+'
                    temp2 =false
                    break
                }
            }

            temp = temp.reverse()
            this.input = temp.join('')

            if(temp2){
                temp3 = this.input
                this.input = '-'.concat(temp3)
            }

        },

        backspace: function(){
            if (this.input.length > 1){

                let temp = this.input.split('')
                temp.pop()
                this.input = temp.join('')
            }
            else{
                this.input = ''

            }
        },
        clear: function(){

            console.clear()
            this.clearIt = true
            setTimeout(function(){
                app.input = ''
                app.clearIt = false
            }, 485)
        },

        noHands: function(event){
            console.log(event)
        }
        



    },
    created:{

    }

})