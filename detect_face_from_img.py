import cv2
from PIL import Image

img = cv2.imread('images/andy1.jpg')
# 获取路径
load_path = cv2.data.haarcascades
# 加载分类器
face_cascade = cv2.CascadeClassifier(load_path + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(load_path + 'haarcascade_eye.xml')

# 灰度处理
gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# 检测人脸
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print(faces)
size = (128,128)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    roi_gray = gray[y:y+h,x:x+w]
    pil_image = Image.fromarray(roi_gray)
    # pil_image.show()
    pil_image.thumbnail(size)
    pil_image.save('test.jpg', quality=95, subsampling=0)


# cv2.imshow('img',img)
# cv2.waitKey(0)
cv2.destroyAllWindows()


