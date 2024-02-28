const html5QrCode = new Html5Qrcode("reader");
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    console.log(decodedText)
    console.log(decodedResult)
    let code_Result = decodedResult.result.format.formatName
    if (code_Result != 'QR_CODE'){
        //TODO run python point calculator
    }
};
const config = { fps: 10, qrbox: { width: 400, height: 400 } };

// If you want to prefer back camera
html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);