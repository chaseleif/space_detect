#! /usr/bin/env python3

import cv2 as cv
import numpy as np
from tkinter import Tk

loadimg = lambda path: cv.imread(path) #, cv.IMREAD_GRAYSCALE)
upscaleimg = lambda img: np.array(img*255,dtype=np.uint8)
downscaleimg = lambda img: np.array(img/255,dtype=np.float32)
gaussian = lambda img: cv.GaussianBlur(img,(5,5),0)

root = Tk()
root.withdraw()
screenx, screeny = root.winfo_screenwidth(), root.winfo_screenheight()
del root

def showImg(img, title='Image'):
  if showImg.scale is None:
    scale = min(1,min(img.shape[0]/screeny, img.shape[1]/screenx))
    if scale < 1:
      showImg.scale = (img.shape[0]*scale,img.shape[1]*scale)
    else:
      showImg.scale = False
  cv.namedWindow(title)
  if isinstance(showImg.scale, tuple):
    scaled = cv.resize(img, showImg.scale)
    cv.imshow(title, scaled)
  else:
    cv.imshow(title, img)
  cv.moveWindow(title, 1, 1)
  cv.waitKey()
  cv.destroyAllWindows()
showImg.scale = None

def processImgStream(img):
  ret, mask_thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
  kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
  mask_eroded = cv.morphologyEx(mask_thresh, cv.MORPH_OPEN, kernel)
  fg_mask = processImgStream.backsub.apply(mask_eroded)
  contours, hierarchy = cv.findContours(fg_mask, cv.RETR_EXTERNAL,
                                        cv.CHAIN_APPROX_SIMPLE)
  for contour in contours:
    x,y,w,h = cv.boundingRect(contour)
    img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
  return img
processImgStream.backsub = cv.createBackgroundSubtractorMOG2()

def markSatellites(imgpath):
  img = loadimg(imgpath)
  showImg(img, 'Input')
  marked = processImgStream(img)
  showImg(marked, 'Marked')

