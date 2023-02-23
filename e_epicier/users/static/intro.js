// let header = document.querySelector('#intro');

// let anim = [
//     { t: "|", ms: 400 },
//     { t: "", ms: 400 },
//     { t: "|", ms: 400 },
//     { t: "", ms: 400 },
//     { t: "|", ms: 400 },
//     { t: "|بَّ", ms: 400 },
//     { t: "|بَّا", ms: 400 },
//     { t: "|بَّاع", ms: 400 },
//     { t: "|بَّاعل", ms: 400 },
//     { t: "|بَّاعلي", ms: 400 },
//     { t: "|بَّاعلي ي", ms: 400 },
//     { t: "|بَّاعلي ير", ms: 400 },
//     { t: "|بَّاعلي يرح", ms: 400 },
//     { t: "|بَّاعلي يرحب", ms: 400 },
//     { t: "|بَّاعلي يرحب ب", ms: 400 },
//     { t: "|بَّاعلي يرحب بك", ms: 400 },
//     { t: "|بَّاعلي يرحب بكم", ms: 400 },
//     { t: "بَّاعلي يرحب بكم", ms: 700 },
//     { t: "|بَّاعلي يرحب بكم", ms: 700 },
//     { t: "بَّاعلي يرحب بكم", ms: 700 },
//     { t: "|بَّاعلي يرحب بكم", ms: 700 },
//     { t: "بَّاعلي يرحب بكم", ms: 700 },
// ];
// let stepDenominator = 1;
// if (window.localStorage.stepDenominator)
//     stepDenominator = window.localStorage.stepDenominator;
// let i = 0;
// let update = () => {
//     let step = anim[i];
//     header.innerText = step.t;
//     i++;

//     if (i < anim.length)
//         setTimeout(update, step.ms / stepDenominator);
//     else {
//         header.classList.add('top');
//         setTimeout(() => {
//             document.getElementById('container').style.opacity = 1;
//             initGlobe();
//         }, 500);
//         window.localStorage.stepDenominator = 2;
//     }
// }
// update();

var TxtType = function(el, toRotate, period) {
    this.toRotate = toRotate;
    this.el = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TxtType.prototype.tick = function() {
    var i = this.loopNum % this.toRotate.length;
    var fullTxt = this.toRotate[i];

    if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

    var that = this;
    var delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
    } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
    }

    setTimeout(function() {
    that.tick();
    }, delta);
};

window.onload = function() {
    var elements = document.getElementsByClassName('typewrite');
    for (var i=0; i<elements.length; i++) {
        var toRotate = elements[i].getAttribute('data-type');
        var period = elements[i].getAttribute('data-period');
        if (toRotate) {
          new TxtType(elements[i], JSON.parse(toRotate), period);
        }
    }
    // INJECT CSS
    // var css = document.createElement("style");
    // css.type = "text/css";
    // css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}";
    // document.body.appendChild(css);
};