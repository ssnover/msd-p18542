if __name__ == '__main__':
    import cv2



    def nothing(x):
        pass


    img_noblur = cv2.imread('Terrain_Map_Red_Green.png', 0)
    img = cv2.blur(img_noblur, (7, 7))

    canny_edge = cv2.Canny(img, 0, 0)

    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)

    cv2.createTrackbar('min_value', 'canny_edge', 0, 500, nothing)
    cv2.createTrackbar('max_value', 'canny_edge', 0, 500, nothing)

while (1):
    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)

    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')

    canny_edge = cv2.Canny(img, min_value, max_value)

    k = cv2.waitKey(37)
    if k == 27:
        break

        cv2.imwrite('messigray.png', img)
        cv2.destroyAllWindows()