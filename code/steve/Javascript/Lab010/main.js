let app = new Vue({
    el: '#app',
    data: {
        logList: "",
        answer: "",
        
    },
    methods: {
        append: function(character) {
            this.logList = `${this.logList}${character}`;
            console.log(this.logList)
        },

        clear: function() {
            this.logList = ""
            this.answer = ""
        },

        backSpace: function(){
            this.logList = this.logList.slice(0, -1)

        },

        equal: function() {
                this.answer = math.evaluate(this.logList)
        }
        
        },
})