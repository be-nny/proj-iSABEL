const html5QrCode = new Html5Qrcode("reader");
// to store the previously scanned QR code
let prev_code = "";

// Callback function called when QR code is successfully decoded
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    // Extracting the format of the QR code
    let code_Result = decodedResult.result.format.formatName
     // Checking if the QR code format is not 'QR_CODE'
    if (code_Result !== 'QR_CODE'){
        // Ensure the same code is not scanned again
        if(prev_code !== decodedText) {
            prev_code = decodedText
            // Update user information based on the decoded text
            if (decodedText === "") {
                updateUserFromBCode("0");
            } else {
                updateUserFromBCode(decodedText);
            }
        }
    } else{
        // Ensure the same code is not scanned again
        if(prev_code !== decodedText) {
            prev_code = decodedText
            checkout();
        }
        console.log(decodedText);
    }
};

const config = { fps: 10, qrbox: { width: 400, height: 400 } };
// If you want to prefer back camera
html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);

function updateUserFromBCode(decodedText) {
    // Send AJAX request to Django view
    fetch(`update_user_from_bcode?code=${decodedText}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Update successful:', data);
        // Handle success if needed
    })
    .catch(error => {
        console.error('Error updating user:', error);
        // Handle error if needed
    });
}

function checkout() {
    // Send AJAX request to Django view
    fetch(`checkout`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Checkout successful:', data);
        // Handle success if needed
    })
    .catch(error => {
        console.error('Error Checking out user:', error);
        // Handle error if needed
    });
}
