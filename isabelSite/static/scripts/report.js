document.addEventListener('DOMContentLoaded', function () {
        var reportButton = document.getElementById('reportButton');
        var reportForm = document.getElementById('reportFormDiv');

        // Toggle the display of the form when the button is clicked
        reportButton.addEventListener('click', function () {
            reportForm.classList.toggle('hide');
        });
    })

document.getElementById('reportForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission
    var form = this;
    var formData = new FormData(form);

    var csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Report saved successfully!');
                form.reset(); // Clear form fields
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });