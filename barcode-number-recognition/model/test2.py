##AUTHORS: Ellis Mackness, Ben Abbott
import cv2

camera_id = 0
delay = 1
window_name = 'OpenCV Barcode'

bd = cv2.barcode_BarcodeDetector()
cap = cv2.VideoCapture(camera_id)
is_camera = True

while is_camera:
    ret, frame = cap.read()

    if ret:
        ret_bc = bd.detectAndDecode(frame)[0]
        if len(ret_bc) > 0:
            final = ret_bc
            print(final)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        is_camera = False

cv2.destroyWindow(window_name)
