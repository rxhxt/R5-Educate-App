
$('.oa').click(function() {
    $('.sss').prop('value', "a");
  })

  $('.ob').click(function() {
   
    $('.sss').prop('value', "b");
  })


  $('.oc').click(function() {
    $('.sss').prop('value', "c");
  })


$('.od').click(function() {
    $('.sss').prop('value', "d");
  })



$('.op1').click(function() {
    $(this).find('.left').find('.c2').click();
});


$('.c2').click(function() {
    if ($(this).hasClass('clicked')) {
        $(this).removeClass('clicked');
        $(this).find('p').removeClass('hide');
        $(this).parent().parent().parent().removeClass('glow');
    } else {
        $(this).addClass('clicked');
        $(this).parent().parent().parent().addClass('glow');
        $(this).find('p').addClass('hide');
        if ($(this).attr("id") != "a") {
            $("#a").removeClass('clicked');
            $("#a > p").removeClass('hide');
            $("#a").parent().parent().parent().removeClass('glow');
        }
        if ($(this).attr("id") != 'b') {
            $('#b').removeClass('clicked');
            $("#b > p").removeClass("hide");
            $("#b").parent().parent().parent().removeClass('glow');
            
        }
        if ($(this).attr("id") != 'c') {
            $('#c').removeClass('clicked');
            $("#c > p").removeClass("hide");
            $("#c").parent().parent().parent().removeClass('glow');
        }
        if ($(this).attr("id") != 'd') {
            $('#d').removeClass('clicked');
            $("#d > p").removeClass("hide");
            $("#d").parent().parent().parent().removeClass('glow');
        }
    }

});


$(function() {
    $('on-hover').hover(function() {
        $('on-hover').attr('i', 'fa fa-bookmark');
    })
});






// The JS for the timer


$(document).ready(function() {
    TweenLite.defaultEase = Expo.easeOut;

    initTimer("10:11"); // other ways --> "0:15" "03:5" "5:2"

    //var reloadBtn = document.querySelector('.reload');
    var timerEl = document.querySelector('.timer');

    function initTimer(t) {

        var self = this,
            timerEl = document.querySelector('.timer'),
            minutesGroupEl = timerEl.querySelector('.minutes-group'),
            secondsGroupEl = timerEl.querySelector('.seconds-group'),

            minutesGroup = {
                firstNum: minutesGroupEl.querySelector('.first'),
                secondNum: minutesGroupEl.querySelector('.second')
            },

            secondsGroup = {
                firstNum: secondsGroupEl.querySelector('.first'),
                secondNum: secondsGroupEl.querySelector('.second')
            };

        var time = {
            min: t.split(':')[0],
            sec: t.split(':')[1]
        };

        var timeNumbers;

        function updateTimer() {

            var timestr;
            var date = new Date();

            date.setHours(0);
            date.setMinutes(time.min);
            date.setSeconds(time.sec);

            var newDate = new Date(date.valueOf() - 1000);
            var temp = newDate.toTimeString().split(" ");
            var tempsplit = temp[0].split(':');

            time.min = tempsplit[1];
            time.sec = tempsplit[2];

            timestr = time.min + time.sec;
            timeNumbers = timestr.split('');
            updateTimerDisplay(timeNumbers);


            if (timestr === '1000') {
                $('.num').addClass("red");
                $('.clock-separator').addClass("red");
            }

            if (timestr === '0000')
                countdownFinished();

            if (timestr != '0000')
                setTimeout(updateTimer, 1000);

        }

        function updateTimerDisplay(arr) {

            animateNum(minutesGroup.firstNum, arr[0]);
            animateNum(minutesGroup.secondNum, arr[1]);
            animateNum(secondsGroup.firstNum, arr[2]);
            animateNum(secondsGroup.secondNum, arr[3]);

        }

        function animateNum(group, arrayValue) {

            TweenMax.killTweensOf(group.querySelector('.number-grp-wrp'));
            TweenMax.to(group.querySelector('.number-grp-wrp'), 1, {
                y: -group.querySelector('.num-' + arrayValue).offsetTop
            });

        }

        setTimeout(updateTimer, 1000);

    }

    function countdownFinished() {
        setTimeout(function() {
            //TweenMax.set(reloadBtn, { scale: 0.8, display: 'block' });
            TweenMax.to(timerEl, 1, { opacity: 0 });
            //TweenMax.to(reloadBtn, 0.5, { scale: 1, opacity: 1 });
            document.body.style.backgroundColor = "black";
        }, 1000);
    }
});