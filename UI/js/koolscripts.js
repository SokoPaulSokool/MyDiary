$(document).ready(function() {
    // adds onclick listener to "Already have account" to initialise login form
    $('#login').click(function() {
        $('#login-form').toggleClass('kool-show').toggleClass('kool-hidden');
        $("#signup-form").toggleClass('kool-show').toggleClass('kool-hidden');

    });
    // adds onclick listener to "Create Accout" to initialise signup form
    $('#signup').click(function() {
        $('#login-form').toggleClass('kool-show').toggleClass('kool-hidden');
        $("#signup-form").toggleClass('kool-show').toggleClass('kool-hidden');

    });

    // adds onclick listener to take user to view their entries when submit on signup form is clicked
    $('#submit-login').click(function() {
        window.location.href = "entries.html";
    });

    $('#submit-signup').click(function() {
        window.location.href = "entries.html";
    });

    // adds onclick listener to add-entry-button to initialise  form
    $('#add-entry-button').click(function() {
        hideAllForms();
        $('#add-entry-form').toggleClass('kool-show').toggleClass('kool-hidden');
        $('#forms-overlay').toggleClass('kool-show').toggleClass('kool-hidden');

    });

    // adds onclick listener to edit-entry-button to initialise  form
    $('#edit-entry-button').click(function() {
        hideAllForms();
        $('#add-entry-form').toggleClass('kool-show').toggleClass('kool-hidden');
        $('#forms-overlay').toggleClass('kool-show').toggleClass('kool-hidden');

    });

    // adds onclick listener to delete-entry-button to initialise  form
    $('#delete-entry-button').click(function() {
        hideAllForms();
        $('#delete-confirm-view').toggleClass('kool-show').toggleClass('kool-hidden');
        $('#forms-overlay').toggleClass('kool-show').toggleClass('kool-hidden');

    });


    // adds onclick listener to delete-entry-button to view profile
    $('#view-profile-button').click(function() {
        hideAllForms();
        $('#profile-view').toggleClass('kool-show').toggleClass('kool-hidden');
        $('#forms-overlay').toggleClass('kool-show').toggleClass('kool-hidden');

    });

    // adds onclick listener to logout
    $('#logout-button').click(function() {
        window.location.href = "index.html";

    });


    $('#overlay-back-button').click(function() {
        hideAllForms();
    });


});

// adds onclick listener to add-entry-button to initialise  form
function hideAllForms() {
    formsOverlay = $('#forms-overlay');
    addEnteryForm = $('#add-entry-form');
    deleteEnteryForm = $('#delete-confirm-view');
    editEnteryForm = $('#edit-entry-form');
    editEnteryForm = $('#profile-view');
    editEnteryForm = $('#edit-entry-form');
    hide(formsOverlay);
    hide(addEnteryForm);
    hide(editEnteryForm);
    hide(deleteEnteryForm);


}

// Hides the element provided
function hide(element) {
    element.addClass('kool-hidden').removeClass('kool-show');

}