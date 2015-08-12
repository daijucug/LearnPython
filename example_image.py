#!/usr/bin/env python

import numpy as np
import skimage.io
from scipy.ndimage import zoom
from skimage.transform import resize

img_file = '/data1/NLPRMNT/lidangwei/test.jpg'

skimage.io.use_plugin('qt')

img = skimage.io.imread( img_file )

skimage.io.imshow(img)

skimage.io.show()

