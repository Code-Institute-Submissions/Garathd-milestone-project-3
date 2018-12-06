/*global $*/

//Regex for letters only used on search fields
function lettersonly(ob) {
    var invalidChars = /([^A-Za-z\s])/;
    if (invalidChars.test(ob.value)) {
        ob.value = ob.value.replace(invalidChars, "");
    }
}

//Regex for small letters only used on search fields
function smalllettersonly(ob) {
    var invalidChars = /([^a-z\s])/;
    if (invalidChars.test(ob.value)) {
        ob.value = ob.value.replace(invalidChars, "");
    }
}

$(document).ready(function() {
    //Scroll to top button
    var scrollTop = $(".scrollTop");

    $(scrollTop).click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;

    });
});
