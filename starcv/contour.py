#! /usr/bin/env python3

import os
import cv2 as cv
import numpy as np
from tkinter import Tk

loadimg = lambda path: cv.imread(path) #, cv.IMREAD_GRAYSCALE)

root = Tk()
root.withdraw()
screenx, screeny = root.winfo_screenwidth()-100, root.winfo_screenheight()-100
del root

def showImg(img, title='Image'):
  cv.namedWindow(title)
  scale = min(screeny/img.shape[0], screenx/img.shape[1])
  if scale < 1:
    scale = (int(img.shape[1]*scale),int(img.shape[0]*scale))
    scaled = cv.resize(img, scale)
    cv.imshow(title, scaled)
  else:
    cv.imshow(title, img)
  cv.moveWindow(title, 20, 20)
  cv.waitKey()
  cv.destroyAllWindows()

# splitimg for the 4x4 phases of image splitting/saving
# truth for getstats
def processImgStream(img, splitimg=False, truth=None):
  if splitimg:
    saveimg = img.copy()[400:800,400:800]
  ret, mask_thresh = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
  kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
  mask_eroded = cv.morphologyEx(mask_thresh, cv.MORPH_OPEN, kernel)
  if splitimg and truth is None:
    saveimg = np.concatenate((saveimg, mask_eroded[400:800,400:800]), axis=1)
  fg_mask = processImgStream.backsub.apply(mask_eroded)
  contours, hierarchy = cv.findContours(fg_mask, cv.RETR_EXTERNAL,
                                        cv.CHAIN_APPROX_TC89_L1)
  #cv.CHAIN_APPROX_SIMPLE)
  if truth is not None:
    if splitimg:
      right = cv.cvtColor(truth[400:800,400:800], cv.COLOR_GRAY2RGB)
      saveimg = np.concatenate((saveimg, right), axis=1)
    tp, fp = 0, 0
    for contour in contours:
      x,y,w,h = cv.boundingRect(contour)
      # if the region is black call this a false positive
      if np.max(truth[y:y+h,x:x+w]) == 0:
        fp += 1
        img = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
      else:
        img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    for contour in contours:
      x,y,w,h = cv.boundingRect(contour)
      # if the region is white call this a positive
      if np.max(truth[y:y+h,x:x+w]) > 0:
        tp += 1
        # zero out this block
        while np.max(truth[y:y+h,x:x+w]) > 0:
          # x,y index of the maximum value of truth within this contour
          seed = truth[y:y+h,x:x+w].argmax()
          seed = (x+seed%w,y+seed//w)
          # fill pixels from the seed to black
          cv.floodFill(truth, None, seed, (0))
    # Find remaining objects within truth
    contours, hierarchy = cv.findContours(truth, cv.RETR_EXTERNAL,
                                          cv.CHAIN_APPROX_SIMPLE)
    # the remaining number of white squares
    missed = len(contours)
    # put a box around each "missing" contour
    for contour in contours:
      x,y,w,h = cv.boundingRect(contour)
      img = cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
    #return img, tp, fp, missed
  else:
    for contour in contours:
      x,y,w,h = cv.boundingRect(contour)
      img = cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
  if not splitimg:
    if truth is not None: return img, tp, fp, missed
    return img
  bottom = cv.cvtColor(fg_mask[400:800,400:800], cv.COLOR_GRAY2RGB)
  bottom = np.concatenate((bottom,img[400:800,400:800]), axis=1)
  saveimg = np.concatenate((saveimg,bottom), axis=0)
  saveimg = cv.line(saveimg, (0,399),(799,399), (102,255,102), 5)
  saveimg = cv.line(saveimg, (399,0),(399,799), (102,255,102), 5)
  if truth is not None: return saveimg, tp, fp, missed
  return saveimg
processImgStream.backsub = cv.createBackgroundSubtractorMOG2()
#processImgStream.backsub = cv.createBackgroundSubtractorKNN()

def markSatellites(imgpath, splitimg=False, show=False, save=True):
  img = loadimg(imgpath)
  if show and not splitimg: showImg(img, 'Input')
  marked = processImgStream(img, splitimg=splitimg)
  if show: showImg(marked, 'Marked')
  if save:
    outname = os.path.join('output',imgpath.split(os.path.sep)[-1])
    cv.imwrite(outname, marked)

# can print field name/val or csv-style
def getStats(imgpath, splitimg=False, show=False, save=True):
  img = cv.imread(imgpath, cv.IMREAD_GRAYSCALE)
  img[img<100] = 0
  # this is img[85:100,62:75] from data/img001.png, the 32fps 1 min data
  sat = np.array([[101,141,0,0,0,0,0,0,0,0,0,0,0],
                 [208,238,180,0,0,0,0,0,0,0,0,0,0],
                 [193,248,239,155,0,0,0,0,0,0,0,0,0],
                 [106,216,251,232,144,0,0,0,0,0,0,0,0],
                 [0,122,220,250,222,115,0,0,0,0,0,0,0],
                 [0,0,128,231,250,218,167,172,212,207,106,0,0],
                 [0,0,0,211,253,252,249,249,254,249,192,0,0],
                 [0,0,160,239,255,255,255,255,255,254,239,144,0],
                 [0,0,159,240,254,255,255,255,255,252,234,151,0],
                 [0,0,0,185,248,255,254,254,255,230,152,0,0],
                 [0,0,0,0,200,234,221,232,252,235,137,0,0],
                 [0,0,0,0,0,118,0,134,220,249,211,106,0],
                 [0,0,0,0,0,0,0,0,126,222,248,202,0],
                 [0,0,0,0,0,0,0,0,0,144,235,243,173],
                 [0,0,0,0,0,0,0,0,0,0,160,212,169]], dtype=np.uint8)
  # the "truth" is a black image with white squares
  truth = np.zeros(img.shape, dtype=np.uint8)
  # use OpenCV's template matching to make white squares
  w, h = sat.shape[::-1]
  res = cv.matchTemplate(img, sat, cv.TM_CCOEFF_NORMED)
  # threshold >= 0.68 and no stars get squares drawn on them
  threshold = 0.68
  loc = np.where(res >= threshold)
  # count the satellites
  numsats = 0
  for pt in zip(*loc[::-1]):
    # this region is black, increment the number of satellites
    if np.max(truth[pt[1]:pt[1]+h,pt[0]:pt[0]+w]) == 0:
      numsats += 1
    # draw the rectangle
    cv.rectangle(truth, pt, (pt[0] + w, pt[1] + h), 255, -1)
  # load the color image
  img = loadimg(imgpath)
  if show and not splitimg: showImg(img, 'Input')
  # processImgStream with the "truth"
  img, tp, fp, missed = processImgStream(img, splitimg=splitimg, truth=truth)
  if show: showImg(img, 'Marked')
  if save:
    outname = os.path.join('output',imgpath.split(os.path.sep)[-1])
    cv.imwrite(outname, img)
  print(f'{imgpath.split(os.path.sep)[-1]},{numsats},{tp},{fp},{missed}')

