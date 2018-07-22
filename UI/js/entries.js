// adds onclick listener to add-entry-button to initialise  form
document.getElementById('add-entry-button').onclick = function() {
    hideAllForms();
    addEnteryForm = document.getElementById('add-entry-form');
    toggleClass(addEnteryForm, "kool-show", "kool-hidden");
    formsOverlay = document.getElementById('forms-overlay');
    toggleClass(formsOverlay, "kool-show", "kool-hidden");
};

// adds onclick listener to edit-entry-button to initialise  form
document.getElementById('edit-entry-button').onclick = function() {
    hideAllForms();
    editEnteryForm = document.getElementById('edit-entry-form');
    toggleClass(editEnteryForm, "kool-show", "kool-hidden");
    formsOverlay = document.getElementById('forms-overlay');
    toggleClass(formsOverlay, "kool-show", "kool-hidden");
};

// adds onclick listener to delete-entry-button to initialise  form
document.getElementById('delete-entry-button').onclick = function() {
    hideAllForms();
    deleteEnteryForm = document.getElementById('delete-confirm-view');
    toggleClass(deleteEnteryForm, "kool-show", "kool-hidden");
    formsOverlay = document.getElementById('forms-overlay');
    toggleClass(formsOverlay, "kool-show", "kool-hidden");
};


// adds onclick listener to add-entry-button to initialise  form
document.getElementById('overlay-back-button').onclick = function() {
    hideAllForms();
};

function hideAllForms() {
    formsOverlay = document.getElementById('forms-overlay');
    addEnteryForm = document.getElementById('add-entry-form');
    deleteEnteryForm = document.getElementById('delete-confirm-view');
    editEnteryForm = document.getElementById('edit-entry-form');
    hide(formsOverlay);
    hide(addEnteryForm);
    hide(editEnteryForm);
    hide(deleteEnteryForm);

}

// Hides the element provided
function hide(element) {

    if (element.classList) {
        element.classList.add('kool-hidden');
        element.classList.remove('kool-show');

    } else {
        classes = element.className.split(" ");
        var h = classes.indexOf("kool-hidden");
        var s = classes.indexOf("kool-show");
        // Checks if element has "kool-hidden" and if it doesent then it adds the class
        if (h < 1) {
            classes.push("kool-hidden");
        }
        // Checks if element has "kool-show" and if it doesent then it removes the class  // Checks if element has "kool-show" and if it doesent then it removes the class
        if (s > 0) {
            classes.splice(s, 1);
        }
        element.className = classes.join(" ");
    }

}

// Toggles the classes on the element provided
function show(element) {

    if (element.classList) {
        element.classList.remove('kool-hidden');
        element.classList.add('kool-show');

    } else {
        classes = element.className.split(" ");
        var h = classes.indexOf("kool-hidden");
        var s = classes.indexOf("kool-show");

        // Checks if element has "kool-show" and if it doesent then it adds the class
        if (s < 1) {
            classes.push("kool-hidden");
        }
        // Checks if element has "kool-hidden" and if it doesent then it removes the class  // Checks if element has "kool-show" and if it doesent then it removes the class
        if (h > 0) {
            classes.splice(s, 1);
        }
        element.className = classes.join(" ");
    }

}


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