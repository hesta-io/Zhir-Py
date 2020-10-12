from skimage import io
from skimage import color
from skimage import viewer
from skimage import filters
from skimage import transform
from functions import deskew
#proof of concept for skimage
imgPath = "./images/4.jpg"
img = io.imread(imgPath, as_gray=True)
# binarize input image and apply local theresould
adaptiveThresh = filters.thresholding.threshold_sauvola(img,window_size=71 )
binarizedImage = img >= adaptiveThresh

# Fixing document skew
rotationAngle = deskew(binarizedImage)
fixedImage = transform.rotate(binarizedImage, rotationAngle, cval=1, mode="constant")
fixedImage2 =  fixedImage * 255
imgviewr = viewer.ImageViewer(fixedImage2)
imgviewr.show()
