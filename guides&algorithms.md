
## Dewarping

`dewarp.py` contains implementations of two dewarping algorithms:

* [Kim et al. 2015, Document dewarping via text-line based optimization](http://www.sciencedirect.com/science/article/pii/S003132031500165X)
* [Meng et al. 2011, Metric rectification of curved document images](http://ieeexplore.ieee.org/abstract/document/5975161/)

Focal length is currently assumed to be that of the iPhone 7, because that’s what I have been using to test. Change the f value at the top of this file if using a different camera.

The Kim et al. algorithm seems to actually work (and be fast enough to process large numbers of pages in a reasonable amount of time); you can use it directly or via `batch.py --dewarp`.

## Binarization

`binarize.py` contains a ton of binarization algorithms, which should all have mostly-optimized implementations.

* Niblack binarization
* [Sauvola and Pietikäinen 2000, Adaptive document image binarization](http://www.sciencedirect.com/science/article/pii/S0031320399000552)
* [Kamel and Zhao 1993, Extraction of binary character/graphics images from grayscale document images](http://www.sciencedirect.com/science/article/pii/S016786551200311X)
* [Yang and Yan 2000, An adaptive logical method for binarization of degraded document images](http://www.sciencedirect.com/science/article/pii/S0031320399000941)
* [Lu et al. 2010, Document image binarization using background estimation and stroke edges](https://link.springer.com/article/10.1007%2Fs10032-010-0130-8?LI=true) (background estimation portion incomplete)
* [Su et al. 2013, Robust document image binarization technique for degraded document images](https://link.springer.com/article/10.1007%2Fs10032-010-0130-8?LI=true) (DIBCO 2013 champion)
* [Ntirogiannis et al. 2014, A combined approach for the binarization of handwritten document images](http://www.sciencedirect.com/science/article/pii/S016786551200311X)

The last algorithm is the best I've found on this set of inputs.

## Text Structuring

`block.py` contains some text-structuring stuff. I intended to use this as a replacement for the current text-line detection system, but I haven't been able to get it to work.

* [Koo and Choo 2010, State estimation in a document image and its applciation in text block identification and text line extraction](https://link.springer.com/chapter/10.1007/978-3-642-15552-9_31)

## Super-resolution

`upscale.py` has some (incomplete) routines for single-image superresolution using text as a prior.

* [Lee et al. 2007, Efficient sparse coding algorithms](http://papers.nips.cc/paper/2979-efficient-sparse-coding-algorithms.pdf)
* [Walha et al. 2012, Super-resolution of single text image by sparse representation](http://doi.acm.org/10.1145/2432553.2432558)
* [Liu et al. 2014, Blockwise coordinate descent schemes for sparse representation](http://ieeexplore.ieee.org/document/6854608/)

## Building

Requirements: Numpy/Scipy, OpenCV (with python bindings), Cython

I don’t know how to make a proper build system for Cython modules, so just do:

`python setup.py build_ext --inplace`

I'd love to convert this all to Python 3, but there's something wrong with Cython. PRs are, of course, welcome.

