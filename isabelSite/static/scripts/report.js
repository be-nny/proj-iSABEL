document.addEventListener('DOMContentLoaded', function () {
        var reportButton = document.getElementById('reportButton');
        var reportForm = document.getElementById('reportForm');

        // Toggle the display of the form when the button is clicked
        reportButton.addEventListener('click', function () {
            reportForm.classList.toggle('hide');
        });
    });