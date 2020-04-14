# import the necessary packages
import cv2
# from pyimagesearch import imutils
from skimage import exposure
import numpy as np
import imutils

class ShapeDetector:
    def __init__(self, filename, calValues):
        # Initiate image containing shapes to be identified
        if int(calValues[2]) == 1:
            self.shapeColour = 1
        else:
            self.shapeColour = 0
        self.sourceImage = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        # cv2.imshow('Source Image', cv2.resize(self.sourceImage, (960, 540)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # self.colourImage = cv2.cvtColor(self.sourceImage,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Coloured Image', cv2.resize(self.colourImage, (960, 540)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.thresholdCalibrationValue = calValues[8]
        self.filteredImage = cv2.bilateralFilter(self.sourceImage, 11, 50, 50)
        # cv2.imshow('Filtered Image', cv2.resize(self.filteredImage, (960, 540)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.filteredImage = cv2.Canny(self.filteredImage, self.thresholdCalibrationValue * 0.9, self.thresholdCalibrationValue)
        # cv2.imshow('Filtered Image', cv2.resize(self.filteredImage, (960, 540)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.DMDSizeX = int(calValues[0])
        self.DMDSizeY = int(calValues[1])
        self.rotation = calValues[5]
        self.positionX = int(calValues[3])
        self.positionY = int(calValues[4])
        self.width = int(calValues[6])
        self.height = int(calValues[7])

    def detectCalibration(self):
        # Detect calibration from input image
        contours = cv2.findContours(self.filteredImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:10]
        calibrationContour = None
        widthImage, heightImage = self.filteredImage.shape
        areaImage = widthImage * heightImage
        for cntr in contours:
            peri = cv2.arcLength(cntr, True)
            approx = cv2.approxPolyDP(cntr, 0.015 * peri, True)
            if len(approx) == 4:
                calibrationContour = approx
                break
        return calibrationContour
        


