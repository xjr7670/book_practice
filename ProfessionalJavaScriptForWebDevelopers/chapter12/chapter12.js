var x = 50, y = 60
var xin = true, yin = true
var step = 1
var delay = 10
var obj = document.getElementById('div1');
function floatDiv() {
    var L=T=0;
    //by www.qpsh.com
    var R = document.body.clientWidth-obj.offsetWidth;
    var B = document.body.clientHeight-obj.offsetHeight;
    obj.style.left = x + document.body.scrollLeft;
    obj.style.top = y + document.body.scrollTop;
    x = x + step*(xin?1:-1)
    if (x < L) { 
        xin = true; 
        x = L;
    }
    if (x > R) { 
        xin = false; 
        x = R;
    }

    y = y + step*(yin?1:-1)

    if (y < T) {
        yin = true; 
        y = T ;
    }

    if (y > B) { 
        yin = false; 
        y = B ;
    }
}


var itl = setInterval("floatDiv()", 1000);
obj.onmouseover=function(){
    clearInterval(itl);
}
obj.onmouseout=function(){
    itl=setInterval("floatDiv()", delay);
}