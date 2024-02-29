import cv2
from keras.models import load_model
import numpy as np


def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img) # histogram expanded from 0 to 255
    img = img / 255
    return img


cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 480)

model = load_model("model.keras")

while True:
    success, frame = cap.read()
    if success:
        img = np.asarray(frame)
        img = cv2.resize(img, (28, 28))
        img = preProcess(img)
        img = img.reshape(1, 28, 28, 1)

        #predict
        #classIndex = int(model.predict_classes(img))
        predictions = model.predict(img)
        classIndex = np.argmax(predictions)
        probVal = np.amax(predictions)
        print(classIndex, probVal)

        if probVal > 0.7:
            cv2.putText(frame, str(classIndex) + "  " + str(probVal), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)

        cv2.imshow("digit-recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break