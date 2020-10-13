var app = new Vue({
    el: '#app',
    data: {
      total: 0
    },
    methods: {
        key: function(num) {
        return this.total += num;
        },
        clear: function() {
        return this.total = 0;
        },
        equal: function() {
         let equal = this.total;
         return this.total = eval(equal);
        }         
    }
});