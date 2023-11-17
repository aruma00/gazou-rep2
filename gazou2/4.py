import cv2

# 画像を読み込み
def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # RGBの各チャンネルのデータを一度に取得
        pixel = img[y, x]  # (y, x) の順序でアクセスすることに注意
        print(pixel)
       

img = cv2.imread('hoge.jpeg')
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', onMouse)
cv2.waitKey(0)

"""
指定された (x, y) 座標が画像のサイズを超えているとエラーが起きる。
画像のサイズは (height, width) の形式で表現されるため、
img のインデックスアクセスは (y, x) の順序で行う必要がある。
"""
    
