import sys,cv2

# 対象画像読み込み
img = cv2.imread("hoge.jpeg")

# 画像の大きさを取得
height, width, channels = img.shape[:3] 
print("width: " + str(width))
print("height: " + str(height))

"""
shape プロパティは、タプル (height, width, channels) を返す。
このタプルから各要素を取り出し、それぞれの変数に格納している。
"""