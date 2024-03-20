//AUTHOR: Merve Ipek Bal

document.addEventListener('DOMContentLoaded', function () {
    // Retrieve the reference to the report button element
    var reportButton = document.getElementById('reportButton');
    // Retrieve the reference to the report form element
    var reportForm = document.getElementById('reportFormDiv');

    // Toggle the display of the form when the button is clicked
    reportButton.addEventListener('click', function () {
        reportForm.classList.toggle('hide');
    });
})