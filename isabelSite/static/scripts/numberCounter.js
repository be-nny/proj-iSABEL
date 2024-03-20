// This jQuery function waits for the DOM to be fully loaded. Once loaded,
// it targets all elements with the class 'counter-count-dec' and animates
// their text content from 0 to their initial value. During this animation,
// it updates the displayed value with two decimal places using the 'toFixed(2)'
// method. The animation duration is set to 2000 milliseconds with a swing easing effect.
jQuery(document).ready(function($) {
    $('.counter-count-dec').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 2000,
            easing: 'swing',
            step: function (now) {
                $(this).text(now.toFixed(2));
            }
        });
    });
});

// Similar to the previous function, this jQuery function waits for the DOM to
// be fully loaded. It targets all elements with the class 'counter-count' and
// animates their text content from 0 to their initial value. During this animation,
// it updates the displayed value by rounding up the current value to the nearest
// integer using the 'Math.ceil()' function. The animation duration is set to
// 2000 milliseconds with a swing easing effect.
jQuery(document).ready(function($) {
    $('.counter-count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        }, {
            duration: 2000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now));
            }
        });
    });
});

