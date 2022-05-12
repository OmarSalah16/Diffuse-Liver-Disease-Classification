window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

function validateName() {
    let name = document.forms["addPatient"]["fullname"].value;
    if (/\d/.test(name)) {
        document.getElementById("nameError").hidden = false;
        document.getElementById("nameError").innerHTML = "Name cannot contain numbers.";
    }
    else 
        document.getElementById("nameError").hidden = true;
}

function validateNumber() {
    let number = document.forms["addPatient"]["phoneno"].value;
    if (number.match(/[^$,.\d]/)) {
        document.getElementById("numberError").hidden = false;
        document.getElementById("numberError").innerHTML = "Name cannot contain numbers.";
    }
    else 
        document.getElementById("numberError").hidden = true;
}