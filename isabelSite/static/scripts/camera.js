

// This method will trigger user permissions
Html5Qrcode.getCameras().then(devices => {
  /**
   * devices would be an array of objects of type:
   * { id: "id", label: "label" }
   */
  if (devices && devices.length) {
    var cameraId = devices[0].id;
    console.log(cameraId);
  }
}).catch(err => {
  // handle err
});

const html5QrCode = new Html5Qrcode(/* element id */ "reader");
html5QrCode.start(
  cameraId,
  {
    fps: 10,    // Optional, frame per seconds for qr code scanning
    qrbox: { width: 250, height: 250 }  // Optional, if you want bounded box UI
  },
  (decodedText, decodedResult) => {
    // do something when code is read
  },
  (errorMessage) => {
    // parse error, ignore it.
  })
.catch((err) => {
  // Start failed, handle it.
});

const html5QrCode = new Html5Qrcode("reader", /* verbose= */ true);

const html5QrCode = new Html5Qrcode("reader");
const qrCodeSuccessCallback = (decodedText, decodedResult) => {
    /* handle success */
};
const config = { fps: 10, qrbox: { width: 250, height: 250 } };

// If you want to prefer back camera
html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);

html5QrCode.stop().then((ignore) => {
  // QR Code scanning is stopped.
}).catch((err) => {
  // Stop failed, handle it.
});