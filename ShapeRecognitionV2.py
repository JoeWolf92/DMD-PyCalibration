# import the necessary packages
import cv2
# from pyimagesearch import imutils
from skimage import exposure
import numpy as np
import imutils

class ShapeDetector:
    def __init__(self, filename, shapeColour, calibrationThreshold):
        # Initiate image containing shapes to be identified
        if shapeColour:
            self.shapeColour = 1
        else:
            self.shapeColour = 0
        # self.sourceImage = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
        self.sourceImage = cv2.imread(filename)
        cv2.imshow('Source Image', cv2.resize(self.sourceImage, (960, 540)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # self.colourImage = cv2.cvtColor(self.sourceImage,cv2.COLOR_RGB2BGR)
        self.colourImage = cv2.cvtColor(self.sourceImage,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Coloured Image', cv2.resize(self.colourImage, (960, 540)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # self.thresholdCalibrationValue = calibrationThreshold
        # if self.shapeColour == 1:
        #     thresholdImageInitial = cv2.bitwise_not(self.sourceImage)
        #     _, self.thresholdImage = cv2.threshold(thresholdImageInitial, self.thresholdCalibrationValue, 255, cv2.THRESH_BINARY)
        # else:
        #     _, thresholdImageInitial = cv2.threshold(self.sourceImage, self.thresholdCalibrationValue, 255, cv2.THRESH_BINARY)
        #     self.thresholdImage = thresholdImageInitial
        # openKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
        # self.filteredImage = cv2.morphologyEx(self.thresholdImage, cv2.MORPH_OPEN, openKernel)
        # closeKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))
        # self.filteredImage = cv2.morphologyEx(self.filteredImage, cv2.MORPH_CLOSE, closeKernel)
        self.filteredImage = cv2.bilateralFilter(self.colourImage, 11, 50, 50)
        cv2.imshow('Filtered Image', cv2.resize(self.filteredImage, (960, 540)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.filteredImage = cv2.Canny(self.filteredImage, 25, 30)
        cv2.imshow('Filtered Image', cv2.resize(self.filteredImage, (960, 540)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.rotation = 0.0
        self.positionX = 0.0
        self.positionY = 0.0
        self.width = 0.0
        self.height = 0.0

    def detectCalibration(self):
        # Detect calibration from input image
        # contours, _ = cv2.findContours(self.filteredImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours = cv2.findContours(self.filteredImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
        calibrationContour = None
        shapeAreas = [cv2.contourArea(cntr) for cntr in contours]
        maxShapeArea = np.max(shapeAreas)
        #print('First Max: ' + str(maxShapeArea))
        #shapeAreas.remove(maxShapeArea)
        #maxShapeArea = np.max(shapeAreas)
        #print('New Max: ' + str(maxShapeArea))
        widthImage, heightImage = self.filteredImage.shape
        areaImage = widthImage * heightImage
        for cntr in contours:
            peri = cv2.arcLength(cntr, True)
            approx = cv2.approxPolyDP(cntr, 0.015 * peri, True)
            if len(approx) == 4:
                calibrationContour = approx
                break
        cv2.drawContours(self.sourceImage, [calibrationContour], -1, (0, 255, 0), 3)
        cv2.imshow("Test Image Calibrated", cv2.resize(self.sourceImage, (960, 540)))
        cv2.waitKey(0)
            # if((( cv2.contourArea(cntr) > maxShapeArea * 0.1) and (cv2.contourArea(cntr) < maxShapeArea) and self.shapeColour == 1 ) or self.shapeColour == 0):
            #     #print(cv2.contourArea(cntr))
            #     rect = cv2.minAreaRect(cntr)
            #     box = cv2.boxPoints(rect)
            #     box = np.int0(box)
            #     # cv2.drawContours(self.colourImage,[box],0,(0,255,0),3)
            #     centre = rect[0]
            #     self.positionX = centre[0]
            #     self.positionY = centre[1]
            #     size = rect[1]
            #     self.width = size[0]
            #     self.height = size[1]
            #     self.rotation = rect[2]
            #     # cv2.circle(self.colourImage,(round(self.positionX),round(self.positionY)), 10, (0,0,255), -1)


