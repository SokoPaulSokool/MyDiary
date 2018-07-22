// adds onclick listener to "Already have account" to initialise login form
document.getElementById('login').onclick = function() {
    loginForm = document.getElementById('login-form');
    toggleClass(loginForm, "kool-show", "kool-hidden");
    signupForm = document.getElementById('signup-form');
    toggleClass(signupForm, "kool-show", "kool-hidden");
};

// adds onclick listener to "Create Accout" to initialise signup form
document.getElementById('signup').onclick = function() {
    loginForm = document.getElementById('login-form');
    toggleClass(loginForm, "kool-show", "kool-hidden");
    signupForm = document.getElementById('signup-form');
    toggleClass(signupForm, "kool-show", "kool-hidden");
};



// adds onclick listener to take user to view their entries when submit on signup form is clicked
document.getElementById('submit-signup').onclick = function() {
    window.location.href = "UI/entries.html";
};

// adds onclick listener to take user to view their entries when submit on login form is clicked
document.getElementById('submit-login').onclick = function() {
    window.location.href = "UI/entries.html";
};
// adds onclick listener to show the detailed view of the clicked entry in a list
document.getElementsByClassName('entries-item').onclick = function() {
    alert("bb");
};

// Toggles the classes on the element provided
function toggleClass(element, classA, classB) {

    if (element.classList) {
        element.classList.toggle(classA);
        element.classList.toggle(classB);

    } else {
        classes = element.className.split(" ");
        var b = classes.indexOf(classB);
        var a = classes.indexOf(classA);
        // Checks if classB exists on an element and replaces it with classA if it exists
        if (b > 0) {
            classes.splice(b, 1);
            classes.push(classA);
        }
        // Checks if classA exists on an element and replaces it with classB if it exists
        if (a > 0) {
            classes.splice(a, 1);
            classes.push(classB);
        }
        element.className = classes.join(" ");
    }

}