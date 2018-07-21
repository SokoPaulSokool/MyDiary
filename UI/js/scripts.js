$(document).ready(function() {
    // $('#form-section').addClass("kool-show ");
    $('#signup').on('click', function() {
        $('#kool-signup').toggleClass("kool-hidden");
        $('#kool-login').toggleClass("kool-hidden");
    });
    $('#login').on('click', function() {
        $('#kool-signup').toggleClass("kool-hidden");
        $('#kool-login').toggleClass("kool-hidden");
    });
});