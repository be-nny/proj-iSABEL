if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
    navigator.mediaDevices.getUserMedia(
        {
            video: {
                width: {
                    min: 1280,
                    ideal: 1920,
                    max: 1920,
                },
                height: {
                    min: 720,
                    ideal: 1080,
                    max: 1080,
                },
                facingMode: 'environment'
            }
        });
}

async function getDevices() {
  const devices = await navigator.mediaDevices.enumerateDevices();
}