import zhirpy as zp
import cv2
import numpy as np
from skimage import io

img = cv2.imread('../images/wraped4.jpg', 0)

def shadow_remove(img):
    rgb_planes = cv2.split(img)
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        result_norm_planes.append(norm_img)
    shadowremov = cv2.merge(result_norm_planes)
    return shadowremov

after  = shadow_remove(img)
cv2.imshow("before",   cv2.resize(img, (540 , 960 )) ) 
cv2.imshow("after",  cv2.resize(after, (540, 960 )) ) 
cv2.waitKey(0)
cv2.destroyAllWindows()
# io.imsave('./after.jpg', img)
 
