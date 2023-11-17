import cv2

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread('hoge.jpeg')
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', onMouse)
cv2.waitKey(0)