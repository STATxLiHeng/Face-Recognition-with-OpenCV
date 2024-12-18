import cv2

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output1.avi', fourcc, fps, size)
while True:
    ret, frame = cap.read()
    cv2.imshow('camera',frame)
    out.write(frame)
    k = cv2.waitKey(20)

    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()