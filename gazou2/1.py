import cv2

img = cv2.imread("hoge.jpeg")

# 画像の表示
cv2.imshow("Image", img)

# キー入力待ち(ここで画像が表示される)
cv2.waitKey()