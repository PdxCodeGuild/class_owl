



  function currentTime() {
    let date = new Date();
    let hour = date.getHours();
    let min = date.getMinutes();
    let sec = date.getSeconds();


    hour = updateTime(hour);
    min = updateTime(min);
    sec = updateTime(sec);
    startClock = setTimeout(function(){ currentTime() }, 1000); 
    document.getElementById("clock").innerHTML = hour + " : " + min + " : " + sec;
  }
  
  function updateTime(unit) {
    if (unit < 10) {
      return "0" + unit;
    }
    else {
      return unit;
    }
  }
 
currentTime();