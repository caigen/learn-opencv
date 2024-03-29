"""
ref:
https://realpython.com/face-recognition-with-python/
https://github.com/shantnu/FaceDetect/
"""

import cv2

image_path = "faces.jpg"
casc_path = "haarcascade_frontalface_default.xml"

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(casc_path)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(5, 5)
)

print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.imwrite("result.png", image)
cv2.waitKey(0)