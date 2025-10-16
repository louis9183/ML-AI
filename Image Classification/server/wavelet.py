import numpy as np
import pywt
import cv2

def w2d(img,mode='haar',level=1):
    imArray = img
    #datatype conversion
    #convert to grayscale
    imArray = cv2.cvtColor(imArray,cv2.COLOR_BGRA2BGR)
    #convert to float
    imArray = np.float32(imArray)
    imArray /= 255;
    #compute coefficients
    coeffs=pywt.wavedec2(imArray,mode)

    #process coefficients
    coeffs_H = list(coeffs)
    #coeffs_H = np.array(coeffs)
    coeffs_H[0] *=0;

    #reconstruction
    imArray_H = pywt.waverec2(coeffs_H,mode)
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)
    return imArray_H