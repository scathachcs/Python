import cv2
import numpy as np

image = cv2.imread("C:/Users/14282/Desktop/Code/Python/cv/0.png",0) #将图片以灰度图导入
h = image.shape[0]
w = image.shape[1]

threshold, new_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("new",new_image)
print('阈值：'+str(threshold))

n = 0
new_image = np.zeros((h,w),np.uint8)
for i in range(h):
    for j in range(w):
        if(image[i,j]> threshold ):
            new_image[i,j] = 255
            n+=1
        else:
            new_image[i,j] = 0

print('黄色部分所占比例:'+str(n/(h*w)))

cv2.waitKey()