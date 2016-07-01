#!/usr/bin/env python3
"""This program XORs two pngs (broken and crypto) with a same 2D key and shows the results"""

import os
import math
import operator
from PIL import Image

if __name__ == "__main__":
    broken = Image.open('broken.bmp')
    crypto = Image.open('crypto.bmp')

    assert broken.size == crypto.size

    squareImgDim = broken.size[0]

    assert squareImgDim % 8 == 0

    imgDimByteCount = int(squareImgDim / 8)

    # Generate uniform random key for XOR from random bytes

    keyData = os.urandom(imgDimByteCount * squareImgDim)
    keyImg = Image.frombytes('1', (squareImgDim, squareImgDim), keyData)

    keyImg.save('key.bmp')

    # Do the XOR and save the results

    brokenData = broken.tobytes()
    cryptoData = crypto.tobytes()

    bXkData = bytes(map(operator.xor, brokenData, keyData))
    cXkData = bytes(map(operator.xor, cryptoData, keyData))
    bXcData = bytes(map(operator.xor, bXkData, cXkData))

    brokenCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), bXkData)
    cryptoCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), cXkData)
    brokenCryptoCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), bXcData)

    brokenCipherImg.save('broken-cipher.bmp')
    cryptoCipherImg.save('crypto-cipher.bmp')
    brokenCryptoCipherImg.save('broken-crypto-cipher.bmp')
