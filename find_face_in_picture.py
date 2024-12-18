from PIL import Image
import face_recognition
import cv2

# 加载图片到numpy array
image = face_recognition.load_image_file("images/girls.jpg")
img_color = cv2.imread("images/girls.jpg")

# 定位人脸
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # 使用cv2画出人脸
    # cv2.rectangle(img_color,(left,top),(right,bottom),(255,0,0),3)

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

cv2.imshow('img',img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()