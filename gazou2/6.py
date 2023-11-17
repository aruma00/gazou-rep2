import cv2
import numpy as np

img = cv2.imread("hoge.jpeg")

bbox = cv2.selectROI(img, fromCenter=False, showCrosshair=False)
"""
cv2.selectROI() 関数を使用して、マウスを使って画像上の領域を選択。
この関数は、選択された領域を表す矩形の座標を返す。
fromCenter パラメータは矩形の中心から選択を開始するかどうかを指定し、
showCrosshair パラメータは十字線の表示を制御する。
"""

left, top, width, height = map(int, bbox)
cropped_img = img[top : top + height, left : left + width] # 選択した領域の保存

"""
bbox の形式は (x, y, w, h) で、それぞれの要素は以下のようになる。
x: 矩形の左上隅の x 座標
y: 矩形の左上隅の y 座標
w: 矩形の幅 (width)
h: 矩形の高さ (height)

map()は、bbox 内の各要素を整数に変換するためのマップ関数

top : top + height は、縦方向 (y 軸) の切り出し範囲を指定。
　　top は矩形の上端の y 座標で、height は矩形の高さを表す。
left : left + width は、横方向 (x 軸) の切り出し範囲を指定。
　　left は矩形の左端の x 座標で、width は矩形の幅を表す。
"""


color = (0, 255, 255)  # 黄色
thickness = 2  # 矩形の境界線の太さ
cv2.rectangle(img, (left, top), (left + width, top + height), color, thickness)

"""
矩形の座標 (left, top) と (left + width, top + height)、
矩形の色 (color)、境界線の太さ (thickness) が渡される
"""

cv2.imshow("Image with Selected Region", img)
cv2.waitKey(0)
