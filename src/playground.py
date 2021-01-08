import zhirpy as zp
import cv2
import numpy as np
from skimage import io

img = cv2.imread('../images/wraped4.jpg', 0)

cv2.imshow("after",  cv2.resize(img, (540, 960 )) ) 
cv2.waitKey(0)
cv2.destroyAllWindows()
# io.imsave('./after.jpg', img)
 
