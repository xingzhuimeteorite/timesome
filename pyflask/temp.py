import cv2 


if __name__=='__main__':
    imgpath = "static/groot/grootdun.jpg"
    img = cv2.imread(imgpath)
    cv2.imshow('demo',img)
    cv2.waitKey(0)