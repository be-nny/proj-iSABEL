const html5QrCode = new Html5Qrcode("reader");
let prev_code = "";
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    let code_Result = decodedResult.result.format.formatName
    if (code_Result !== 'QR_CODE'){
        if(prev_code !== decodedText) {
            prev_code = decodedText
            if (decodedText === "") {
                updateUserFromBCode("0");
            } else {
                console.log(decodedText);
                updateUserFromBCode(decodedText);
            }
        }
    } else{
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
