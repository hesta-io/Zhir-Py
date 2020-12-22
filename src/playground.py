import zhirpy as zp
import cv2
import numpy as np
from skimage import io

img = cv2.imread('../images/table-1.jpg', 0)
# io.imsave('./before.jpg', img)

after = cv2.fastNlMeansDenoising(img,None,10,7,21)

row, col = after.shape[:2]
bottom = after[row-2:row, 0:col]
mean = cv2.mean(bottom)[0]

bordersize = 10
after = cv2.copyMakeBorder(
    after,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=0
)


cv2.imshow("before",   cv2.resize(img, (540 , 960 )) ) 
cv2.imshow("after",  cv2.resize(after, (540, 960 )) ) 
cv2.waitKey(0)
cv2.destroyAllWindows()
# io.imsave('./after.jpg', img)
 
