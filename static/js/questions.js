/*global $*/

$(document).ready(function() {
    $("html, body").animate({ scrollTop: $(document).height() }, 1000);

    $('#check').attr('disabled', true);
    $('#user-input').keyup(function() {
        if ($(this).val().length != 0)
            $('#check').attr('disabled', false);
        else
            $('#check').attr('disabled', true);
    })
});
