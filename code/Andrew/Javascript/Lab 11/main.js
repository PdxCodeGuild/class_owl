
let app = new Vue({
    el: "#app",
    data:{
        headerObj:{headers:{Authorization: 'Token token="d61d1ae7ecaca320b07fa0335c15d8c1"'}
        },
        url: "https://favqs.com/api/quotes/",
        filterText: '',
        adderValue: "",
        pages: 1,
        quoteLst: [],
        thing: false,
        picker: true,
        count: "",
        selecter: '',
        modder: '',
        pickedQuote: null
    },
    methods:{
        getQuoteBtn: async function(){
            if (this.adderValue === 'invalid'){
                return this.thing = true
            }
            else{
                this.thing = false
            }

            // + '&type=tag'

            if (this.selecter){
                this.modder = '&type=' + encodeURIComponent(this.selecter)
            }

            let filterText = this.adderValue? "&filter=" + this.adderValue: ''
            if (this.modder){
                filterText += this.modder
            }
            
            
            let url = app.url +'?page=' + this.pages + filterText   
            
            let response = await axios.get(url,this.headerObj)
            
            this.quoteLst = response.data.quotes
            this.picker = true
            this.adderValue = null
            this.selecter = null
            this.modder = null

            console.log(this.quoteLst)
            console.log(response)                 
        
        },      
        
        turner: function(number){
            if(number === -1 && this.pages >1){
                this.pages -= 1
                a.count -= 1
                // this.getQuoteBtn()
            }
            else if(number === 1 && this.pages <25){
                this.pages++
                a.count++
                // this.getQuoteBtn()
            }
            else{
                console.log('Nuh uh ah, didn\'t say the magic word!')
            }
        },
        focuser: function(item){
            this.pickedQuote = item
            setTimeout(function(){
                app.pickedQuote = null
            }, 3000)
        }
    },
    watch: {
        pages:function(newpages, oldpages){
            this.getQuoteBtn()
            console.log(newpages, 'new')
            console.log(oldpages, 'old')
        },
        adderValue: function(newV,oldV){
            if (newV === 'pickOwn'){
                this.picker = false
                this.adderValue=''
            }
        }
    },
       



})





// new Vue({el:"#special"})