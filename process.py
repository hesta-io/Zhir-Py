from skimage import io
from skimage import color
from skimage import viewer
from skimage import filters
#proof of concept for skimage
imgPath = "./images/3.jpg"
img = io.imread(imgPath, as_gray=True)
# binarize input image and apply local theresould
adaptiveThresh = filters.thresholding.threshold_sauvola(img,window_size=75 )
binarizedImage = img >= adaptiveThresh

imgviewr = viewer.ImageViewer(binarizedImage)
imgviewr.show()

