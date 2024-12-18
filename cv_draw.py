import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(111,111),(255,0,255),5)
cv2.rectangle(img,(111,111),(222,222),(255,123,111),3)
cv2.circle(img,(333,333),100,(111,111,111),8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'hello',(100,500),font,5,(255,123,123))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
