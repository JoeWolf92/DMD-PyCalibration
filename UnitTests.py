import sys
import unittest
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtTest
import cv2

import appMainWindow
import ShapeRecognition
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate
import scipy.ndimage
import numpy as np

app = QtWidgets.QApplication(sys.argv)

class appMainWindowTests(unittest.TestCase):
    # Unit tests for the GUI
    # def setUp(self):
    #     # Create the GUI
    #     self.form = appMainWindow.appMainWindow()

    # def test_Defaults(self):
    #     # Test default values of GUI contents
    #     self.assertEqual(self.form.ui.btn_CamImageImport.text(), "Import Camera Image")
    #     self.assertEqual(self.form.ui.btn_DMDMaskGen.text(), "Generate DMD Mask")
    #     self.assertEqual(self.form.ui.btn_DMDMaskSave.text(), "Save Current Mask")
    #     self.assertEqual(self.form.ui.btn_Calibrate.text(), "Calibrate")
    #     self.assertEqual(self.form.ui.cbox_CalibrateCheck.text(), "Lock Calibration?")
    #     self.assertEqual(self.form.ui.cbox_CalibrateCheck.isChecked(), False)
        
    def test_ImageRecognition(self):
        # Test basic funtionality of the shape recognition sub-system with two test images
        # Image 1 is a black rectangle
        testImage = ShapeRecognition.ShapeDetector("./TestImages/CalibrationImage.tif", False, '200')
        # cv2.imshow("BlackRec",testImage.sourceImage)
        # cv2.imshow("Threshold BlackRec", testImage.thresholdImage)
        # cv2.imshow("BlackRecFiltered", cv2.resize(testImage.filteredImage, (960, 540)))
        # cv2.waitKey(3500)
        # cv2.destroyAllWindows()
        testImage.detectCalibration()
        # cv2.imshow("BlackRec with Contours", cv2.resize(testImage.colourImage,(960, 540)))
        # cv2.waitKey(3500)
        # self.assertAlmostEqual(testImage.rotation, -45.19929122924805)
        # self.assertAlmostEqual(testImage.width, 850.6590576171875)
        # self.assertAlmostEqual(testImage.height, 488.5807800292969)
        # self.assertAlmostEqual(testImage.positionX, 795.543212890625)
        # self.assertAlmostEqual(testImage.positionY, 551.9424438476562)
        # # cv2.imshow("BlackRec with Contours", cv2.resize(testImage.colourImage,(960, 540)))
        # # cv2.waitKey(3500)
        # # cv2.destroyAllWindows()
        # # Image 2 is a white rectangle
        # testImage = ShapeRecognition.ShapeDetector("./TestImages/WhiteRectangle.tiff", True)
        # # cv2.imshow("WhiteRec",testImage.sourceImage)
        # # cv2.imshow("Threshold WhiteRec", testImage.thresholdImage)
        # # cv2.imshow("WhiteRecFiltered", cv2.resize(testImage.filteredImage, (960, 540)))
        # # cv2.waitKey(3500)
        # # cv2.destroyAllWindows()
        # testImage.detectCalibration()
        # self.assertAlmostEqual(testImage.rotation, -44.041961669921875)
        # self.assertAlmostEqual(testImage.width, 857.2245483398438)
        # self.assertAlmostEqual(testImage.height, 486.2369384765625)
        # self.assertAlmostEqual(testImage.positionX, 1146.5018310546875)
        # self.assertAlmostEqual(testImage.positionY, 561.4849853515625)
        # cv2.imshow("WhiteRec with Contours", cv2.resize(testImage.colourImage,(960, 540)))
        # cv2.waitKey(3500)
        # cv2.destroyAllWindows()

    # def test_ThresholdImage(self):
    #     # image = plt.imread('./TestImages/WhiteRectangle.tiff')
    #     image = plt.imread('/Users/joewolf/Downloads/CalibrationImage_Exposure-500ms_Ratio-0p1.tif')
    #     plt.imshow(image)
    #     plt.show()
    #     centreYImage = 581
    #     centreXImage = 973
    #     DMDSizeY = 1080
    #     DMDSizeX = 1920
    #     centreYDMD = DMDSizeY/2
    #     centreXDMD = DMDSizeX/2
    #     shiftX = -(centreXImage - centreXDMD)
    #     shiftY = -(centreYImage - centreYDMD)
    #     shiftImage = scipy.ndimage.shift(image, np.array([shiftY, shiftX]))
    #     plt.imshow(shiftImage)
    #     plt.show()
    #     rotatedImage = rotate(shiftImage , angle = -42.83)
    #     plt.imshow(rotatedImage)
    #     plt.show()
    #     calibrationRatio = 0.1
    #     DMDImageWidth = 296 / calibrationRatio
    #     DMDImageHeight = 165 / calibrationRatio
    #     imageSizeY, imageSizeX = rotatedImage.shape
    #     if DMDImageWidth > imageSizeX:
    #         DMDStartX = 0
    #         DMDEndX = int(DMDImageWidth)
    #         padX = int(round(np.abs(imageSizeX-DMDImageWidth) / 2))
    #     else:
    #         DMDStartX = int(round((imageSizeX-DMDImageWidth) / 2))
    #         DMDEndX = int(DMDStartX + DMDImageWidth)
    #         padX = 0
    #     if DMDImageHeight > imageSizeY:
    #         DMDStartY = 0
    #         DMDEndY = int(DMDImageHeight)
    #         padY = int(round(np.abs(imageSizeY-DMDImageHeight) / 2))
    #     else:
    #         DMDStartY = int(round((imageSizeY-DMDImageHeight) / 2))
    #         DMDEndY = int(DMDStartY + DMDImageHeight)
    #         padY = 0
    #     paddedImage = np.pad(rotatedImage, ((padY, padY), (padX, padX)), 'constant')
    #     newImage = paddedImage[DMDStartY:DMDEndY,DMDStartX:DMDEndX]
    #     plt.imshow(newImage)
    #     plt.show()
    #     newImageScaledX = np.arange(0, 1920, 1, dtype = np.uint8)
    #     newImageScaledY = np.arange(0, 1080, 1, dtype = np.uint8)
    #     newImageScaled = cv2.resize(newImage, dsize=(DMDSizeX, DMDSizeY), interpolation=cv2.INTER_CUBIC)
    #     plt.imshow(newImageScaled)
    #     plt.show()

    # def test_CalibrationImageLoad(self):
    #     self.form.ui.btn_CamImageImport.click()
    #     self.

        
if __name__ == '__main__':
    unittest.main()