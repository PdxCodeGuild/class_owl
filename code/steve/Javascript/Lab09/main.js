
let app = new Vue({
    el: '#app',
    data: {
        todoList: [],
        task: '',
    },
    methods: {
        addTask: function(){
            if (this.task === ''){
                return
            }
            this.todoList.push({
                title: this.task,
                completed: false
            })
            this.task = ''

        },

        completed: function(){
            // this.todoList.

        },

        remove: function(i) {
            this.todoList.splice(i, 1)
        },
    }
})