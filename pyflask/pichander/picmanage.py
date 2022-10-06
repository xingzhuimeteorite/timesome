# 使用 cv2 压缩图片
# 图片等比缩小
import cv2
from math import ceil


class Picture:
    def __init__(self, path: str):
        self.path = path

    def getcvimg(self):
        img = cv2.imread(self.path)
        return img


def resizePic(img, max_size: int):
    # 读取图片 传入的 是 cv图像
    width = img.shape[1]
    height = img.shape[0]
    small_rate = round(max(width, height)/max_size, 2)
    n_width = int(width/small_rate)
    n_height = int(height/small_rate)
    new_img = cv2.resize(img, (n_width, n_height))
    return new_img


if __name__ == "__main__":
    img = Picture("grootdun.jpg")
    cv2.imshow("img", img.getcvimg())
    cv2.waitKey(0)
