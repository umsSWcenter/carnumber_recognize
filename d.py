import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract



img_ori = cv2.imread('C:/1.jpg',cv2.IMREAD_COLOR)
print(img_ori.shape)
#height, width, channel = np.shape(img_ori)

