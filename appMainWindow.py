# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from UI_appMainWindow import Ui_MainWindow
import ShapeRecognition as sr
import cv2
import numpy as np

import os.path
from imageio import imwrite
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import rotate
import scipy.ndimage
import scipy.interpolate as interp
from PIL import Image as PILImage
from math import sqrt
import ntpath
from scipy.ndimage.morphology import binary_opening
#import libtiff

class appMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        #libtiff.libtiff_ctypes.suppress_warnings()
        #libtiff.TIFFSetWarningHandler(_null_warning_handler)
        super(appMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sceneCamera = QtWidgets.QGraphicsScene()
        self.sceneMask = QtWidgets.QGraphicsScene()
        self.show()
        self.fileNameCameraImage = ""
        self.ui.btn_CamImageImport.clicked.connect(self.onClick_CamImageImport)
        self.ui.btn_Calibrate.clicked.connect(self.onClick_Calibrate)
        self.ui.btn_SaveCalibration.clicked.connect(self.onClick_SaveCalibration)
        self.ui.cbox_LockCalibration.clicked.connect(self.onClick_LockCalibration)
        self.ui.btn_DMDMaskGen.clicked.connect(self.onClick_DMDMaskGen)
        self.ui.btn_DMDMaskSave.clicked.connect(self.onClick_DMDMaskSave)
        self.ui.btn_getThresholdValues.clicked.connect(self.onClick_GetThresholdValues)
        self.ui.btn_MaskToAdd.clicked.connect(self.onClick_MaskToAddImport)
        self.ui.slider_thresholdValue.valueChanged.connect(self.valueChange_ThresholdValue)
        self.showImageInView("./TestImages/Vialux_DMD.png", self.ui.view_CameraImage)
        self.showImageInView("./TestImages/UoL_logo.jpeg", self.ui.view_DMDMaskImage)
        self.CalibrationValuesFile = './Calibration/CalibrationValues.txt'
        self.CalibrationImageFile = './Calibration/CalibrationImageFile.txt'
        self.maskCountCalibration = 1
        self.maskCountThreshold = 1
        self.maskCountSlit = 1
        self.maskCountPinhole = 1
        if os.path.isfile(self.CalibrationValuesFile) and os.path.isfile(self.CalibrationImageFile):
            self.calibrationValuesStorage = np.loadtxt(self.CalibrationValuesFile, dtype=float)
            self.ui.txt_DMDSizeX.setPlainText(str(self.calibrationValuesStorage[0]))
            self.ui.txt_DMDSizeY.setPlainText(str(self.calibrationValuesStorage[1]))
            self.ui.txt_DMDCalibrationImageRatio.setPlainText(str(self.calibrationValuesStorage[2]))
            if self.calibrationValuesStorage[3] == 1:
                self.ui.radioButton_BlackImageMask.setChecked(True)
            else:
                self.ui.radioButton_WhiteImageMask.setChecked(True)
            self.ui.txt_CentreAdjustX.setPlainText(str(self.calibrationValuesStorage[4]))
            self.ui.txt_CentreAdjustY.setPlainText(str(self.calibrationValuesStorage[5]))
            self.ui.txt_RotationAdjust.setPlainText(str(self.calibrationValuesStorage[6]))
            self.ui.txt_WidthAdjust.setPlainText(str(self.calibrationValuesStorage[7]))
            self.ui.txt_HeightAdjust.setPlainText(str(self.calibrationValuesStorage[8]))
            self.ui.txt_CalibrationThreshold.setPlainText(str(self.calibrationValuesStorage[9]))
            imageFile = open(self.CalibrationImageFile,'r')
            self.fileNameCameraImage = imageFile.read()
            self.calibrationImageStorage = self.fileNameCameraImage
            imageFile.close()
            self.onClick_Calibrate()
        self.MaskGeneratedFlag = False
        return

    def showImageInView(self, image, view):
        if isinstance(image, str):# or type(image) is np.ndarray:
            imagePixMap = QtGui.QPixmap(image)#.scaled(300,300, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        else:
            height, width, chanel = image.shape
            bytesPerChanel = 3 * width
            imagePixMap = QtGui.QImage(image, width, height, bytesPerChanel, QtGui.QImage.Format_RGB888)#.scaled(300,300, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        view.setPixmap(QtGui.QPixmap(imagePixMap))
        view.repaint()
        return
    
    def generateBox(self, calibration):
        # Initialise local input values
        centreX = calibration.positionX
        centreY = calibration.positionY
        theta = calibration.rotation
        phi = 90 - theta
        thetaRad = theta * np.pi / 180
        phiRad = phi * np.pi / 180
        semiW = calibration.width / 2
        semiH = calibration.height / 2
        # A is point to the right of centre half way up the right side of the rectangle
        Ax = int(round(centreX + semiW * np.cos(thetaRad)))
        Ay = int(round(centreY + semiW * np.sin(thetaRad)))
        # B is the bottom right corner of the rectangle
        Bx = int(round(Ax + semiH * np.sin(thetaRad)))
        By = int(round(Ay - semiH * np.cos(thetaRad)))
        # C is the top right corner of the rectangle
        Cx = int(round(Ax - semiH * np.cos(phiRad)))
        Cy = int(round(Ay + semiH * np.sin(phiRad)))
        # D is point to the left of centre half way up the left side of the rectangle
        Dx = int(round(centreX - semiW * np.cos(thetaRad)))
        Dy = int(round(centreY - semiW * np.sin(thetaRad)))
        # E is the bottom left corner of the rectangle
        Ex = int(round(Dx + semiH * np.cos(phiRad)))
        Ey = int(round(Dy - semiH * np.sin(phiRad)))
        # F is the top left corner of the rectangle
        Fx = int(round(Dx - semiH * np.sin(thetaRad)))
        Fy = int(round(Dy + semiH * np.cos(thetaRad)))
        box = np.array([[Fx, Fy], [Ex, Ey], [Bx, By], [Cx, Cy]])
        return box

    def maskGenerationCalibration(self, blackBool):
        xSize = int(float(self.ui.txt_DMDSizeX.toPlainText()))
        ySize = int(float(self.ui.txt_DMDSizeY.toPlainText()))
        ratio = float(self.ui.txt_DMDCalibrationMaskRatio.toPlainText())
        xSizeRatio = round(ratio * xSize)
        ySizeRatio = round(ratio * ySize)
        centreX = round(xSize/2)
        centreY = round(ySize/2)
        calibrationSectionXSemiLow = centreX - round(xSizeRatio/2)
        calibrationSectionYSemiLow = centreY - round(ySizeRatio/2)
        calibrationSectionXSemiHigh = centreX + round(xSizeRatio/2)
        calibrationSectionYSemiHigh = centreY + round(ySizeRatio/2)
        centreCircleRadius = float(self.ui.txt_CentreCircleSize.toPlainText())
        if blackBool:
            localMask = np.zeros((ySize, xSize), dtype=np.uint8)
        else:
            localMask = np.ones((ySize, xSize), dtype=np.uint8) * 255
        for x in range(xSize-1):
            for y in range(ySize-1):
                if x > calibrationSectionXSemiLow and x < calibrationSectionXSemiHigh and y > calibrationSectionYSemiLow and y < calibrationSectionYSemiHigh:
                    if sqrt(((x - centreX) ** 2) + ((y - centreY) ** 2)) < centreCircleRadius:
                        if blackBool:
                            localMask[y, x] = 0
                        else:
                            localMask[y, x] = 255
                    else:
                        if blackBool:
                            localMask[y, x] = 255
                        else:
                            localMask[y, x] = 0
        self.MaskGeneratedFlag = True
        return localMask
        
    def maskGenerationThreshold(self, blackBool):
        if not(self.ui.cbox_LockCalibration.isChecked()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Lock above calibration before generating threshold masks.')
            error_dialog.exec_()
            return
        originalImage = plt.imread(self.fileNameCameraImage)
        centreYImage = round(self.calibration.positionY)
        centreXImage = round(self.calibration.positionX)
        DMDSizeY = int(float(self.ui.txt_DMDSizeY.toPlainText()))
        DMDSizeX = int(float(self.ui.txt_DMDSizeX.toPlainText()))
        centreYDMD = DMDSizeY/2
        centreXDMD = DMDSizeX/2
        shiftX = -(centreXImage - centreXDMD)
        shiftY = -(centreYImage - centreYDMD)
        shiftImage = scipy.ndimage.shift(originalImage, np.array([shiftY, shiftX]))
        rotatedImage = rotate(shiftImage , angle = self.calibration.rotation)
        DMDImageWidth = round(self.calibration.width / float(self.ui.txt_DMDCalibrationImageRatio.toPlainText()))
        DMDImageHeight = round(self.calibration.height / float(self.ui.txt_DMDCalibrationImageRatio.toPlainText()))
        imageSizeX, imageSizeY = rotatedImage.shape
        if DMDImageWidth > imageSizeX:
            DMDStartX = 0
            DMDEndX = int(DMDImageWidth)
            padX = int(round(np.abs(imageSizeX-DMDImageWidth) / 2))
        else:
            DMDStartX = int(round((imageSizeX-DMDImageWidth) / 2))
            DMDEndX = int(DMDStartX + DMDImageWidth)
            padX = 0
        if DMDImageHeight > imageSizeY:
            DMDStartY = 0
            DMDEndY = int(DMDImageHeight)
            padY = int(round(np.abs(imageSizeY-DMDImageHeight) / 2))
        else:
            DMDStartY = int(round((imageSizeY-DMDImageHeight) / 2))
            DMDEndY = int(DMDStartY + DMDImageHeight)
            padY = 0
        paddedImage = np.pad(rotatedImage, ((padY, padY), (padX, padX)), 'constant')
        newImage = paddedImage[DMDStartY:DMDEndY,DMDStartX:DMDEndX]
        newImageScaledX = np.arange(0, 1920, 1, dtype = np.uint8)
        newImageScaledY = np.arange(0, 1080, 1, dtype = np.uint8)
        localMask = cv2.resize(newImage, dsize=(DMDSizeX, DMDSizeY), interpolation=cv2.INTER_CUBIC)
        if self.ui.cBox_FlipLR.isChecked():
            localMask = np.fliplr(localMask)
        if self.ui.cBox_FlipUD.isChecked():
            localMask = np.flipud(localMask)
        localMask = rotate(localMask, angle = int(float(self.ui.txt_maskAdjustRot.toPlainText())))
        localMask = np.roll(localMask, int(float(self.ui.txt_maskAdjustUD.toPlainText())), axis = 0)
        localMask = np.roll(localMask, int(float(self.ui.txt_maskAdjustLR.toPlainText())), axis = 1)
        if not(blackBool):
            localMask = cv2.threshold(localMask, int(float(self.ui.txt_currentThreshold.toPlainText())), 255, cv2.THRESH_BINARY)
        else:
            localMask = cv2.threshold(localMask, int(float(self.ui.txt_currentThreshold.toPlainText())), 255, cv2.THRESH_BINARY_INV)
        if not(self.ui.txt_MaskToAdd.toPlainText() == ''):
            try:
                localMaskToAdd = plt.imread(self.ui.txt_MaskToAdd.toPlainText())
                localMaskToAdd = localMaskToAdd.astype(dtype = np.uint8)
                if localMask[1].shape == localMaskToAdd.shape:
                    localMaskAdded = localMask[1] + localMaskToAdd
                    if not(blackBool):
                        localMaskTuple = cv2.threshold(localMaskAdded, 200, 255, cv2.THRESH_BINARY)
                    else:
                        localMaskTuple = cv2.threshold(localMaskAdded, 200, 255, cv2.THRESH_BINARY_INV)
                    localMask = localMaskTuple[1]
                else:
                    error_dialog = QtWidgets.QErrorMessage()
                    error_dialog.showMessage('Mask to add is different size to new Threshold Mask.')
                    error_dialog.exec_()
                    return
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('File to add to new Threshold Mask not found.')
                error_dialog.exec_()
                return
        else:
            localMask = localMask[1]
        thresholdFilterSize = int(float(self.ui.txt_ThresholdFilterSize.toPlainText()))
        if thresholdFilterSize > 0:
            localMask = binary_opening(localMask, structure=np.ones((thresholdFilterSize, thresholdFilterSize))).astype(np.uint8) * 255
            localMask = cv2.bitwise_not(binary_opening(cv2.bitwise_not(localMask), structure=np.ones((thresholdFilterSize, thresholdFilterSize))).astype(np.uint8) * 255)
        self.MaskGeneratedFlag = True
        return localMask
        
    def maskGenerationSlit(self, blackBool):
        print('Slit')
        self.MaskGeneratedFlag = True
        return

    def maskGenerationPinhole(self, blackBool):
        print('Pinhole')
        self.MaskGeneratedFlag = True
        return

    @pyqtSlot()
    def valueChange_ThresholdValue(self):
        self.ui.txt_currentThreshold.setPlainText(str(self.ui.slider_thresholdValue.value()))
        return
    
    @pyqtSlot()
    def onClick_GetThresholdValues(self):
        localArray = plt.imread(self.fileNameCameraImage)
        minValue = np.amin(localArray)
        maxValue = np.amax(localArray)
        self.ui.label_highValueThreshold.setText(str(maxValue))
        self.ui.label_lowValueThreshold.setText(str(minValue))
        self.ui.txt_currentThreshold.setPlainText(str(minValue))
        self.ui.slider_thresholdValue.setValue(minValue)
        self.ui.slider_thresholdValue.setSliderPosition(minValue)
        self.ui.slider_thresholdValue.setMinimum(minValue)
        self.ui.slider_thresholdValue.setMaximum(maxValue)
        return

    @pyqtSlot()
    def onClick_CamImageImport(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileNameCameraImage, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tiff (*.tiff);;tif (*.tif);;png (*.png)", options=options)
        if self.fileNameCameraImage:
            self.showImageInView(self.fileNameCameraImage, self.ui.view_CameraImage)
        return
    
    @pyqtSlot()
    def onClick_MaskToAddImport(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileNameMaskToAdd, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tiff (*.tiff);;tif (*.tif);;png (*.png)", options=options)
        if self.fileNameMaskToAdd:
            self.showImageInView(self.fileNameMaskToAdd, self.ui.view_DMDMaskImage)
            self.ui.txt_MaskToAdd.setPlainText(self.fileNameMaskToAdd)
            self.ui.txt_MaskToAdd.repaint()
        return

    @pyqtSlot()
    def onClick_Calibrate(self):
        if not self.fileNameCameraImage:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Calibration image must be loaded before calibration can be performed.')
            error_dialog.exec_()
            return
        if not(self.ui.txt_DMDSizeX.toPlainText().replace(".", "", 1).isdigit()) or not(self.ui.txt_DMDSizeY.toPlainText().replace(".", "", 1).isdigit()) or not(self.ui.txt_DMDCalibrationImageRatio.toPlainText().replace(".", "", 1).isdigit()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('DMD calibration ratio and DMD X & Y size must be numeric.')
            error_dialog.exec_()
            return
        try:
            self.calibration = sr.ShapeDetector(self.fileNameCameraImage, self.ui.radioButton_BlackImageMask.isChecked(), int(float(self.ui.txt_CalibrationThreshold.toPlainText())))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Problem with Calibration Threshold level set.')
            error_dialog.exec_()
            return
        self.calibration.detectCalibration()
        self.calibration.positionX = self.calibration.positionX + float(self.ui.txt_CentreAdjustX.toPlainText())
        self.calibration.positionY = self.calibration.positionY + float(self.ui.txt_CentreAdjustY.toPlainText())
        self.calibration.rotation = self.calibration.rotation + float(self.ui.txt_RotationAdjust.toPlainText())
        self.calibration.width = self.calibration.width * float(self.ui.txt_WidthAdjust.toPlainText())
        self.calibration.height = self.calibration.height * float(self.ui.txt_HeightAdjust.toPlainText())
        box = self.generateBox(self.calibration)
        cv2.drawContours(self.calibration.colourImage, [box], 0, (0, 255, 0), 3)
        cv2.circle(self.calibration.colourImage,(round(self.calibration.positionX),round(self.calibration.positionY)), 10, (0,0,255), -1)
        self.showImageInView(self.calibration.colourImage, self.ui.view_CameraImage)
        if self.ui.radioButton_BlackImageMask.isChecked():
            checkState = 1
        else:
            checkState = 0
        self.calibrationValuesStorage = np.array([
            float(self.ui.txt_DMDSizeX.toPlainText()),
            float(self.ui.txt_DMDSizeY.toPlainText()), 
            float(self.ui.txt_DMDCalibrationImageRatio.toPlainText()), 
            float(checkState),
            float(self.ui.txt_CentreAdjustX.toPlainText()), 
            float(self.ui.txt_CentreAdjustY.toPlainText()),
            float(self.ui.txt_RotationAdjust.toPlainText()),
            float(self.ui.txt_WidthAdjust.toPlainText()),
            float(self.ui.txt_HeightAdjust.toPlainText()),
            float(self.calibration.thresholdCalibrationValue),
            float(self.calibration.positionX),
            float(self.calibration.positionY),
            float(self.calibration.rotation),
            float(self.calibration.width),
            float(self.calibration.height)
            ], dtype=float)
        self.calibrationImageStorage = self.fileNameCameraImage
        return

    @pyqtSlot()
    def onClick_SaveCalibration(self):
        np.savetxt(self.CalibrationValuesFile, self.calibrationValuesStorage, fmt='%1.2f')
        imageFile = open(self.CalibrationImageFile, 'w+')
        imageFile.write(self.calibrationImageStorage)
        imageFile.close()
        return

    @pyqtSlot()
    def onClick_LockCalibration(self):
        if self.ui.cbox_LockCalibration.isChecked():
            self.ui.txt_DMDSizeX.setEnabled(False)
            self.ui.txt_DMDSizeY.setEnabled(False)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(False)
            self.ui.txt_CentreAdjustX.setEnabled(False)
            self.ui.txt_CentreAdjustY.setEnabled(False)
            self.ui.radioButton_BlackImageMask.setEnabled(False)
            self.ui.radioButton_WhiteImageMask.setEnabled(False)
            self.ui.txt_RotationAdjust.setEnabled(False)
            self.ui.txt_WidthAdjust.setEnabled(False)
            self.ui.txt_HeightAdjust.setEnabled(False)
            self.ui.btn_SaveCalibration.setEnabled(False)
            self.ui.btn_Calibrate.setEnabled(False)
            self.ui.txt_CalibrationThreshold.setEnabled(False)
        elif not(self.ui.cbox_LockCalibration.isChecked()):
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(True)
            self.ui.txt_CentreAdjustX.setEnabled(True)
            self.ui.txt_CentreAdjustY.setEnabled(True)
            self.ui.radioButton_BlackImageMask.setEnabled(True)
            self.ui.radioButton_WhiteImageMask.setEnabled(True)
            self.ui.txt_RotationAdjust.setEnabled(True)
            self.ui.txt_WidthAdjust.setEnabled(True)
            self.ui.txt_HeightAdjust.setEnabled(True)
            self.ui.btn_SaveCalibration.setEnabled(True)
            self.ui.btn_Calibrate.setEnabled(True)
            self.ui.txt_CalibrationThreshold.setEnabled(True)
        else:
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_DMDCalibrationImageRatio.setEnabled(True)
            self.ui.txt_CentreAdjustX.setEnabled(True)
            self.ui.txt_CentreAdjustY.setEnabled(True)
            self.ui.radioButton_BlackImageMask.setEnabled(True)
            self.ui.radioButton_WhiteImageMask.setEnabled(True)
            self.ui.txt_RotationAdjust.setEnabled(True)
            self.ui.txt_WidthAdjust.setEnabled(True)
            self.ui.txt_HeightAdjust.setEnabled(True)
            self.ui.btn_SaveCalibration.setEnabled(True)
            self.ui.btn_Calibrate.setEnabled(True)
            self.ui.txt_CalibrationThreshold.setEnabled(True)
        self.repaint()
        return

    @pyqtSlot()
    def onClick_DMDMaskGen(self):
        self.Mask = None
        self.MaskGeneratedFlag = False
        if self.ui.tab_MaskFunctionality.currentIndex() == 0:
            self.Mask = self.maskGenerationCalibration(self.ui.radioButton_BlackDMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 1:
            self.Mask = self.maskGenerationThreshold(self.ui.radioButton_BlackDMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 2:
            self.Mask = self.maskGenerationSlit(self.ui.radioButton_BlackDMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 3:
            self.Mask = self.maskGenerationPinhole(self.ui.radioButton_BlackDMDMask.isChecked())
        if not(self.MaskGeneratedFlag):
            return
        else:
            self.MaskChoice = self.ui.tab_MaskFunctionality.currentIndex()
            height1D, width1D = self.Mask.shape
            rgbImage = np.zeros([height1D, width1D, 3] , dtype=np.uint8)
            rgbImage[:,:,0] = self.Mask
            rgbImage[:,:,1] = self.Mask
            rgbImage[:,:,2] = self.Mask
            self.showImageInView(rgbImage, self.ui.view_DMDMaskImage)
        return

    @pyqtSlot()
    def onClick_DMDMaskSave(self):
        if not(self.MaskGeneratedFlag):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Mask must be generated before it can be saved.')
            error_dialog.exec_()
            return
        if self.MaskChoice == 0:
            imwrite('./Masks/Calibration/CalibrationMask-' + str(self.maskCountCalibration) + '_CCSize-' + self.ui.txt_CentreCircleSize.toPlainText() + '_Ratio-' + self.ui.txt_DMDCalibrationMaskRatio.toPlainText() + '.bmp', self.Mask)
            self.maskCountCalibration = self.maskCountCalibration + 1
        elif self.MaskChoice == 1:
            saveMask = self.Mask.astype(np.uint8)
            imwrite('./Masks/Threshold/ThresholdMask-' + str(self.maskCountThreshold) + '_Threshold-' + self.ui.txt_currentThreshold.toPlainText() + '_MaskAdded-' + ntpath.basename(self.ui.txt_MaskToAdd.toPlainText()) + '.bmp', saveMask)
            self.maskCountThreshold = self.maskCountThreshold + 1
        elif self.MaskChoice == 2:
            imwrite('./Masks/Slit/SlitMask-' + str(self.maskCountSlit) + '_NumSlits-' + str(self.ui.spinBox_NumberOfSlits.value()) + '_Width-' + self.ui.txt_SlitWidth.toPlainText() + '_Separation-' + self.ui.txt_SlitSeparation.toPlainText() + '_Rotation' + self.ui.txt_SlitRotation.toPlainText() + '.bmp', self.Mask)
            self.maskCountSlit = self.maskCountSlit + 1
        elif self.MaskChoice == 3:
            imwrite('./Masks/Pinhole/PinholeMask-' + str(self.maskCountPinhole) + '_NumPinholes-' + str(self.ui.spinBox_NumberOfPinholes.value()) + '_Radius-' + self.ui.txt_PinholeRadius.toPlainText() + 'Pitch-' + self.ui.txt_PinholePitch.toPlainText() + '_Rotation' + self.ui.txt_PinholeRotation.toPlainText() + '.bmp', self.Mask)
            self.maskCountPinhole = self.maskCountPinhole + 1
        else:
            imwrite('./Masks/Mask.bmp', self.Mask)
        return

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = appMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
