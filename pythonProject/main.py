import cv2
import numpy
import os


def delete_files(filepath):
    files = os.scandir(filepath)
    for file in files:
        os.remove(file)


def face_recognition(image, i, input_folder):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    if len(faces_rect) > 0:
        cv2.imwrite(f'{input_folder}/DetectedFace{i}.png', img)


def find_images_in_dict(extraction_filepath, input_folder):
    delete_files(input_folder)
    files = os.listdir(extraction_filepath)
    i = 0
    for file in files:
        face_recognition(os.path.join(extraction_filepath, file), i, input_folder)
        i += 1


if __name__ == '__main__':
    find_images_in_dict('images', 'DetectedFaces')

