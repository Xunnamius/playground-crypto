#!/usr/bin/env python3
"""This program XORs two pngs (broken and crypto) with a same 2D key and shows the results"""

import os
import math
import operator
from PIL import Image

if __name__ == "__main__":
    broken = Image.open('1. broken.bmp')
    crypto = Image.open('2. crypto.bmp')

    assert broken.size == crypto.size

    squareImgDim = broken.size[0]

    assert squareImgDim % 8 == 0

    imgDimByteCount = int(squareImgDim / 8)

    # Generate uniform random key for XOR from random bytes and generate an img
    keyData = os.urandom(imgDimByteCount * squareImgDim)
    keyImg = Image.frombytes('1', (squareImgDim, squareImgDim), keyData)

    # Save the results of the above operation
    keyImg.save('3. key.bmp')

    # Do the XORs and save the results

    brokenData = broken.tobytes()
    cryptoData = crypto.tobytes()

    # broken XOR key
    bXkData = bytes(map(operator.xor, brokenData, keyData))
    # crypto XOR key
    cXkData = bytes(map(operator.xor, cryptoData, keyData))
    # broken XOR key XOR crypto XOR key
    bXcData = bytes(map(operator.xor, bXkData, cXkData))

    brokenCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), bXkData)
    cryptoCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), cXkData)
    brokenCryptoCipherImg = Image.frombytes('1', (squareImgDim, squareImgDim), bXcData)

    # Save the results
    brokenCipherImg.save('4. broken-xor-key.bmp')
    cryptoCipherImg.save('5. crypto-xor-key.bmp')
    brokenCryptoCipherImg.save('6. broken-xor-key-xor-crypto-xor-key.bmp')
