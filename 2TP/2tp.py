#!/usr/bin/env python3
"""This program XORs two pngs (broken and crypto) with a same 2D key and shows the results"""

import os
import math
from PIL import Image

if __name__ == "__main__":
    broken = Image.open('broken.png')
    crypto = Image.open('crypto.png')

    assert broken.size == crypto.size
    assert broken.size % 8 == 0

    squareImgDim = broken.size[0]
    imgDimByteCount = squareImgDim / 8

    # Generate random key for XOR
    key = os.urandom(imgDimByteCount * squareImgDim)
    keyImg = Image.frombytes('1', (squareImgDim, squareImgDim), key)

    # Do the XOR and save the results
    keyImg.save('key.bmp')
