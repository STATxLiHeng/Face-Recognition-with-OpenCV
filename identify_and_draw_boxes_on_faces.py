import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

# Load a sample picture and learn how to recognize it.
andy_image = face_recognition.load_image_file("images/andy.jpg")
andy_face_encoding = face_recognition.face_encodings(andy_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("images/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    andy_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "andy",
    "Joe Biden"
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("images/bigfour.jpg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

img = cv2.imread('images/bigfour.jpg')

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 3)

    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,name,(left,bottom),font,1,(0,255,0),3)



cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
