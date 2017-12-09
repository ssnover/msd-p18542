if __name__ == '__main__':
    import numpy as np
    import cv2

    cap = cv2.VideoCapture('vtest.avi')
    fgbg = cv2.createBackgroundSubtractorMOG2()
    while (1):
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        cv2.imshow('fgmask', fgmask)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()