import glob
import math
import os

import cv2 as cv
import numpy as np

path = '../afterProcess/'


#단일 이미지간 rmse(rgb) 비교
img1 = cv.imread(os.path.join(path + '(result284)Ground_Truth.png'))
img2 = cv.imread(os.path.join(path + '(result284)Predicted_Image.png'))

print(img1.shape)
print(img2.shape)
err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)


for i in range(0,256):
    print(img1.astype("float")[i][123])
    print(img2.astype("float")[i][123])


err /= float(img1.shape[0] * img1.shape[1] * img1.shape[2])

print(err)


#gray 변환 이후 비교
# img1 = cv.imread(os.path.join(path + 'I_output_0.png'))
# img2 = cv.imread(os.path.join(path + 'I_output_12.png'))

img1 = cv.cvtColor(img1, cv.COLOR_RGB2GRAY)
img2 = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)

# print(img1.shape)

err = np.sum((img1.astype("float") - img2.astype("float")) ** 2)
err /= float(img1.shape[0] * img1.shape[1])
err = math.sqrt(err)

print(err)


cv.waitKey(0)
cv.destroyAllWindows()

