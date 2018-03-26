import numpy as np
import cv2 as cv
img = cv.imread('aarow.png', 0)
ret,thresh = cv.threshold(img,127,255,0)
img2, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv.moments(cnt)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])


rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img2 = cv.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 3)
cv.imshow('img2', img2)
k = cv.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv.destroyAllWindows()
