import cv2
import os

from django.core.files import File

from face_detection.settings import BASE_DIR
from .models import DetectedFaces, DetectionImages


def detect_faces(image_object: DetectionImages,
                 cascPath=str(BASE_DIR) + f'/xml/haarcascade_frontalface_default.xml'):
    """
        Face detection service.
    :param image_object: image object to be processed.
    :param cascPath: cascade classifier trained by the traincascade application.
    """

    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(image_object.input_image.path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        DetectedFaces.objects.create(detection_image=image_object,
                                     x1=x,
                                     y1=y,
                                     x2=x+w,
                                     y2=y+h)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imwrite(str(BASE_DIR) +'/output_images/random.jpg', image)
    image_object.output_image.save(f'output_images/{image_object.owner.username}.jpg',
                                   File(open(str(BASE_DIR) +'/output_images/random.jpg', 'rb')))
    os.remove(str(BASE_DIR) + '/output_images/random.jpg')
    image_object.status = 'finished'
    image_object.save()
