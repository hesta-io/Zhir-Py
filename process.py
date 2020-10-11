from skimage import data
from skimage import viewer
#proof of concept for skimage
coffe = data.coffee()
imgviewr = viewer.ImageViewer(coffe)
imgviewr.show()

