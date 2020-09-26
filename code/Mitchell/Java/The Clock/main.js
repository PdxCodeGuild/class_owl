
setInterval(function clocktime () {
    var d = new Date();
    document.getElementById("clock").innerText = d; 
}, 1000);



clocktime();