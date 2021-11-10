# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
import time
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot

from UI_appMainWindow import Ui_MainWindow
import ShapeRecognitionV2 as sr
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
import skimage.exposure as exposure
#import libtiff

import worker
from PyQt5.QtCore import QThread
import ctypes as ct

from ALP4 import *

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
        self.ui.btn_SendCalParameters.clicked.connect(self.onClick_SendCalParameters)
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
            if self.calibrationValuesStorage[2] == 1:
                self.ui.radioButton_CamDMD2ImageMask.setChecked(True)
            else:
                self.ui.radioButton_CamDMD1ImageMask.setChecked(True)
            self.ui.txt_CalPositionX.setPlainText(str(self.calibrationValuesStorage[3]))
            self.ui.txt_CalPositionY.setPlainText(str(self.calibrationValuesStorage[4]))
            self.ui.txt_CalRotation.setPlainText(str(self.calibrationValuesStorage[5]))
            self.ui.txt_CalWidth.setPlainText(str(self.calibrationValuesStorage[6]))
            self.ui.txt_CalHeight.setPlainText(str(self.calibrationValuesStorage[7]))
            self.ui.txt_CalibrationThreshold.setPlainText(str(self.calibrationValuesStorage[8]))
            imageFile = open(self.CalibrationImageFile,'r')
            self.fileNameCameraImage = imageFile.read()
            self.calibrationImageStorage = self.fileNameCameraImage
            imageFile.close()
            #if self.calibrationImageStorage
            try:
                self.onClick_Calibrate()
            except:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage('Calibration Image Not Found.')
                error_dialog.exec_()
        self.MaskGeneratedFlag = False
        self.DMDConnectFlag = False
        self.DMDConnectionLostFlag = False
        self.DMDDisplayFlag = False
        self.DMDReconnectCount = 0
        self.DMDReconnectAttemptLimit = 10
        self.ui.btn_ConnectDMD.clicked.connect(self.onClick_ConnectDMD)
        self.ui.btn_DisconnectDMD.clicked.connect(self.onClick_DisconnectDMD)
        self.ui.btn_HaltDMD.clicked.connect(self.onClick_HaltDMD)
        self.ui.btn_CamDMD1DMD.clicked.connect(self.onClick_CamDMD1DMD)
        self.ui.btn_CamDMD2DMD.clicked.connect(self.onClick_CamDMD2DMD)
        self.ui.btn_DisplayCurrentDMD.clicked.connect(self.onClick_DMDDisplayCurrentMask)
        self.ui.btn_DisplayFileDMD.clicked.connect(self.onClick_DMDDisplayFileMask)
        ###### Threading
        # Create worker and thread inside form - no parents!
        self.workerObj = worker.Worker()
        self.thread = QThread()
        # Connect Workers Signals to Form method slots to post data.
        self.workerObj.statusCheckDMDTimer.connect(self.statusCheckDMD)
        # Move the Worker object to the Thread object
        self.workerObj.moveToThread(self.thread)
        # Connect Worker Signals to the Thread slots
        self.workerObj.finished.connect(self.thread.quit)
        # Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.workerObj.procCounter)
        # * - Thread finished signal will close the app if you want!
        #self.thread.finished.connect(app.exit)
        # Start the thread
        self.thread.start()
        #############
        self.onClick_ConnectDMD()
        if self.DMDConnectFlag:
            self.onClick_CamDMD1DMD()
        return

    def statusCheckDMD(self):
        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S")
        if self.DMDConnectFlag and not(self.DMDConnectionLostFlag):
            try:
                testVal = int(self.DMD.DevInquire(inquireType = ALP_USB_CONNECTION).value)
                if testVal != 0:
                    self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/orange.png"))
                    self.DMDConnectionLostFlag = True
                    self.DMDReconnectCount = 0
                    print('Disconnected at: ', currentTime)
                else:
                    self.DMDConnectFlag = True
                    #print('Connected at: ', currentTime)
            except:
                self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/orange.png"))
                self.DMDConnectionLostFlag = True
                self.DMDReconnectCount = 0
                print('Disconnected at: ', currentTime)
        if self.DMDConnectFlag and self.DMDConnectionLostFlag and self.DMDReconnectCount < self.DMDReconnectAttemptLimit:
            try:
                self.DMD.Halt()
                if self.DMDDisplayFlag == True:
                    self.DMD.FreeSeq()
                self.DMD.Free()
                self.DMDConnectFlag = False
            except:
                self.DMDConnectionCount = self.DMDConnectionCount + 1
        if not(self.DMDConnectFlag) and self.DMDConnectionLostFlag and self.DMDReconnectCount < self.DMDReconnectAttemptLimit:
            try:
                self.DMD = ALP4(version = '4.3', libDir = 'C:/Program Files/ALP-4.3/ALP-4.3 API')
                self.DMD.Initialize()
                self.DMDConnectFlag = True
                self.DMDConnectionLostFlag = False
                self.DMDReconnectCount = 0
                self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/green.png"))
                return
            except:
                self.DMDConnectionCount = self.DMDConnectionCount + 1
        if self.DMDReconnectCount >= self.DMDReconnectAttemptLimit:
            self.DMDConnectFlag = False
            self.DMDDisplayFlag = False
            self.DMDConnectionLostFlag = False
            self.DMDReconnectCount = 0
            self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/red.png"))
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('DMD connection lost!')
            error_dialog.exec_()
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

    def maskGenerationCalibration(self, CamDMD2Bool):
        xSize = int(float(self.ui.txt_DMDSizeX.toPlainText()))
        ySize = int(float(self.ui.txt_DMDSizeY.toPlainText()))
        maskCentreX = int(float(self.ui.txt_DMDCalibrationMaskPositionX.toPlainText()))
        maskCentreY = int(float(self.ui.txt_DMDCalibrationMaskPositionY.toPlainText()))
        maskHeight = int(float(self.ui.txt_DMDCalibrationMaskHeight.toPlainText()))
        maskWidth = int(float(self.ui.txt_DMDCalibrationMaskWidth.toPlainText()))
        maskRotation = float(self.ui.txt_DMDCalibrationMaskRotation.toPlainText())
        centreCircleRadius = float(self.ui.txt_CentreCircleSize.toPlainText())
        if CamDMD2Bool:
            localMask = np.zeros((maskHeight, maskWidth), dtype=np.uint8)
        else:
            localMask = np.ones((maskHeight, maskWidth), dtype=np.uint8) * 255
        for x in range(maskWidth):
            for y in range(maskHeight):
                if sqrt(((x - (maskWidth/2)) ** 2) + ((y - (maskHeight/2)) ** 2)) < centreCircleRadius:
                    if CamDMD2Bool:
                        localMask[y, x] = 255
                    else:
                        localMask[y, x] = 0
        shiftX = -maskCentreX
        shiftY = -maskCentreY
        if CamDMD2Bool:
            localMask = rotate(localMask, angle = maskRotation, mode='constant', cval=255)
            rotHeight, rotWidth = localMask.shape
            padY = round((ySize - rotHeight) / 2)
            padX = round((xSize - rotWidth) / 2)
            localMask = np.pad(localMask, ((padY, padY), (padX, padX)), 'constant', constant_values = (255, 255))
            if localMask.shape[0] < 1080 or localMask.shape[1] < 1920:
                localMask = np.pad(localMask, ((0, 1), (0, 1)), 'constant', constant_values = (255, 255))
            localMask = localMask[0:int(float(self.ui.txt_DMDSizeY.toPlainText())),0:int(float(self.ui.txt_DMDSizeX.toPlainText()))]
            localMask = scipy.ndimage.shift(localMask, np.array([shiftY, shiftX]), cval=255)
        else:
            localMask = rotate(localMask, angle = maskRotation, mode='constant', cval=0)
            rotHeight, rotWidth = localMask.shape
            padY = int((ySize - rotHeight) / 2)
            padX = int((xSize - rotWidth) / 2)
            localMask = np.pad(localMask, ((padY, padY), (padX, padX)), 'constant', constant_values = (0, 0))
            if localMask.shape[0] < 1080 or localMask.shape[1] < 1920:
                localMask = np.pad(localMask, ((0, 1), (0, 1)), 'constant', constant_values = (255, 255))
            localMask = localMask[0:int(float(self.ui.txt_DMDSizeY.toPlainText())),0:int(float(self.ui.txt_DMDSizeX.toPlainText()))]
            localMask = scipy.ndimage.shift(localMask, np.array([shiftY, shiftX]), cval=0)
        self.MaskGeneratedFlag = True
        return localMask
        
    def maskGenerationThreshold(self, CamDMD2Bool):
        if not(self.ui.cbox_LockCalibration.isChecked()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Lock above calibration before generating threshold masks.')
            error_dialog.exec_()
            return
        originalImage = plt.imread(self.fileNameCameraImage)
        pts = self.cntrPoints.reshape(4,2)
        rect = np.zeros((4,2), dtype='float32')
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)] # tl
        rect[2] = pts[np.argmax(s)] # br
        diff = np.diff(pts, axis=1)
        rect[3] = pts[np.argmin(diff)] # tr
        rect[1] = pts[np.argmax(diff)] # bl
        (tl, tr, br, bl) = rect
        # width of new image
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        # height of new image
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        # Max of A&B is are final dimensions
        maxWidth = max(int(widthA), int(widthB))
        maxHeight = max(int(heightA), int(heightB))
        # Destination points which image will be mapped to
        dst = np.array([
            [0, 0],
            [0, maxWidth - 1],
            [maxHeight - 1, maxWidth - 1],
            [maxHeight - 1, 0]], dtype = "float32")
        # Calculate perspective transform matrix
        M = cv2.getPerspectiveTransform(rect, dst)
        # Warp perspective based on calculated transform
        warpImage = cv2.warpPerspective(originalImage, M, (maxHeight, maxWidth))
        # Scale warped section to actual size on DMD
        warpImageScaled = cv2.resize(warpImage, dsize=(self.calibration.width, self.calibration.height), interpolation=cv2.INTER_LANCZOS4)
        # Pad settings based on calibration mask parameters
        DMDHalfHeight = self.calibration.DMDSizeY / 2
        DMDHalfWidth = self.calibration.DMDSizeX / 2
        offsetX = self.calibration.positionX
        offsetY = self.calibration.positionY
        # Rotate and pad scaled section of DMD mask to full DMD mask
        if not(CamDMD2Bool):
            rotatedImage = rotate(warpImageScaled, angle=self.calibration.rotation, cval=0.0)
            maskHalfWidth = rotatedImage.shape[1] / 2
            maskHalfHeight = rotatedImage.shape[0] / 2
            padYTop = int(DMDHalfHeight - maskHalfHeight + offsetY)
            padYBottom = int(DMDHalfHeight - maskHalfHeight - offsetY)
            padXLeft = int(DMDHalfWidth - maskHalfWidth + offsetX)
            padXRight = int(DMDHalfWidth - maskHalfWidth - offsetX)    
            localMask = np.pad(rotatedImage, ((padYTop, padYBottom), (padXLeft, padXRight)), 'constant', constant_values=0.0)
            localMask = cv2.threshold(localMask, int(float(self.ui.txt_currentThreshold.toPlainText())), 255, cv2.THRESH_BINARY)
        else:
            rotatedImage = rotate(warpImageScaled, angle=self.calibration.rotation, cval=255.0)
            maskHalfWidth = rotatedImage.shape[1] / 2
            maskHalfHeight = rotatedImage.shape[0] / 2
            padYTop = int(DMDHalfHeight - maskHalfHeight + offsetY)
            padYBottom = int(DMDHalfHeight - maskHalfHeight - offsetY)
            padXLeft = int(DMDHalfWidth - maskHalfWidth + offsetX)
            padXRight = int(DMDHalfWidth - maskHalfWidth - offsetX)
            localMask = np.pad(rotatedImage, ((padYTop, padYBottom), (padXLeft, padXRight)), 'constant', constant_values=255.0)
            localMask = cv2.threshold(localMask, int(float(self.ui.txt_currentThreshold.toPlainText())), 255, cv2.THRESH_BINARY_INV)
        localMask = localMask[1]
        # Flip mask as required
        if self.ui.cBox_FlipLR.isChecked():
            localMask = np.fliplr(localMask)
        if self.ui.cBox_FlipUD.isChecked():
            localMask = np.flipud(localMask)   
        # Add to existing mask as required
        if not(self.ui.txt_MaskToAdd.toPlainText() == ''):
            try:
                localMaskToAdd = plt.imread(self.ui.txt_MaskToAdd.toPlainText())
                localMaskToAdd = localMaskToAdd.astype(dtype = np.uint8)
                if localMask.shape == localMaskToAdd.shape:
                    localMaskAdded = localMask + localMaskToAdd
                    if not(CamDMD2Bool):
                        localMaskTuple = cv2.threshold(localMaskAdded, 200, 255, cv2.THRESH_BINARY)
                    else:
                        localMaskTuple = cv2.threshold(localMaskAdded, 500, 255, cv2.THRESH_BINARY)
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
        thresholdFilterSize = int(float(self.ui.txt_ThresholdFilterSize.toPlainText()))
        if thresholdFilterSize > 0:
            localMask = binary_opening(localMask, structure=np.ones((thresholdFilterSize, thresholdFilterSize))).astype(np.uint8) * 255
            localMask = cv2.bitwise_not(binary_opening(cv2.bitwise_not(localMask), structure=np.ones((thresholdFilterSize, thresholdFilterSize))).astype(np.uint8) * 255)
        self.MaskGeneratedFlag = True
        return localMask
        
    def maskGenerationSlit(self, CamDMD2Bool):
        xSize = int(float(self.ui.txt_DMDSizeX.toPlainText()))
        ySize = int(float(self.ui.txt_DMDSizeY.toPlainText()))
        localMask = np.zeros((ySize, xSize), dtype=np.uint8)
        self.MaskGeneratedFlag = True
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Feature under development. Blank mask returned.')
        error_dialog.exec_()
        return localMask

    def maskGenerationPinhole(self, CamDMD2Bool):
        xSize = int(float(self.ui.txt_DMDSizeX.toPlainText()))
        ySize = int(float(self.ui.txt_DMDSizeY.toPlainText()))
        # pinholeNum = int(float(self.ui.spinBox_NumberOfPinholes.Value()))
        # pinholeRadius = int(float(self.ui.txt_PinholeRadius.toPlainText()))
        # pinholePitch = int(float(self.ui.txt_PinholePitch.toPlainText()))
        # pinholeRotation = int(float(self.ui.txt_PinholeRotation.toPlainText()))
        # pinholeX = int(float(self.ui.txt_PinholeX.toPlainText()))
        # pinholeY = int(float(self.ui.txt_PinholeY.toPlainText()))
        # if CamDMD2Bool:
        #     localMask = np.zeros((ySize, xSize), dtype=np.uint8)
        # else:
        #     localMask = np.ones((ySize, xSize), dtype=np.uint8) * 255
        # for x in range(xSize):
        #     for y in range(ySize):
        #         if sqrt(((x - (maskWidth/2)) ** 2) + ((y - (maskHeight/2)) ** 2)) < centreCircleRadius:
        #             if CamDMD2Bool:
        #                 localMask[y, x] = 255
        #             else:
        #                 localMask[y, x] = 0
        # shiftX = -maskCentreX
        # shiftY = -maskCentreY
        # if CamDMD2Bool:
        #     localMask = rotate(localMask, angle = maskRotation, mode='constant', cval=255)
        #     rotHeight, rotWidth = localMask.shape
        #     padY = round((ySize - rotHeight) / 2)
        #     padX = round((xSize - rotWidth) / 2)
        #     localMask = np.pad(localMask, ((padY, padY), (padX, padX)), 'constant', constant_values = (255, 255))
        #     if localMask.shape[0] < 1080 or localMask.shape[1] < 1920:
        #         localMask = np.pad(localMask, ((0, 1), (0, 1)), 'constant', constant_values = (255, 255))
        #     localMask = localMask[0:int(float(self.ui.txt_DMDSizeY.toPlainText())),0:int(float(self.ui.txt_DMDSizeX.toPlainText()))]
        #     localMask = scipy.ndimage.shift(localMask, np.array([shiftY, shiftX]), cval=255)
        # else:
        #     localMask = rotate(localMask, angle = maskRotation, mode='constant', cval=0)
        #     rotHeight, rotWidth = localMask.shape
        #     padY = int((ySize - rotHeight) / 2)
        #     padX = int((xSize - rotWidth) / 2)
        #     localMask = np.pad(localMask, ((padY, padY), (padX, padX)), 'constant', constant_values = (0, 0))
        #     if localMask.shape[0] < 1080 or localMask.shape[1] < 1920:
        #         localMask = np.pad(localMask, ((0, 1), (0, 1)), 'constant', constant_values = (255, 255))
        #     localMask = localMask[0:int(float(self.ui.txt_DMDSizeY.toPlainText())),0:int(float(self.ui.txt_DMDSizeX.toPlainText()))]
        #     localMask = scipy.ndimage.shift(localMask, np.array([shiftY, shiftX]), cval=0)
        localMask = np.zeros((ySize, xSize), dtype=np.uint8)
        self.MaskGeneratedFlag = True
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Feature under development. Blank mask returned.')
        error_dialog.exec_()
        return localMask

    @pyqtSlot()
    def valueChange_ThresholdValue(self):
        self.ui.txt_currentThreshold.setPlainText(str(self.ui.slider_thresholdValue.value()))
        self.ui.txt_currentThreshold.repaint()
        return
    
    @pyqtSlot()
    def onClick_GetThresholdValues(self):
        localArray = plt.imread(self.fileNameCameraImage)
        minValue = np.amin(localArray)
        maxValue = np.amax(localArray)
        self.ui.label_highValueThreshold.setText(str(maxValue))
        self.ui.label_lowValueThreshold.setText(str(minValue))
        self.ui.slider_thresholdValue.setMinimum(minValue)
        self.ui.slider_thresholdValue.setMaximum(maxValue)
        self.ui.slider_thresholdValue.setValue(maxValue/2)
        self.ui.slider_thresholdValue.setSliderPosition(maxValue/2)
        self.ui.txt_currentThreshold.setPlainText(str(maxValue/2))
        self.repaint()
        return
    
    @pyqtSlot()
    def onClick_SendCalParameters(self):
        if self.ui.cbox_LockCalibration.isChecked():
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Unlock above calibration before transferring values.')
            error_dialog.exec_()
            return
        self.ui.txt_CalPositionX.setPlainText(self.ui.txt_DMDCalibrationMaskPositionX.toPlainText())
        self.ui.txt_CalPositionY.setPlainText(self.ui.txt_DMDCalibrationMaskPositionY.toPlainText())
        self.ui.txt_CalRotation.setPlainText(self.ui.txt_DMDCalibrationMaskRotation.toPlainText())
        self.ui.txt_CalWidth.setPlainText(self.ui.txt_DMDCalibrationMaskWidth.toPlainText())
        self.ui.txt_CalHeight.setPlainText(self.ui.txt_DMDCalibrationMaskHeight.toPlainText())
        self.repaint()
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
        if not(self.ui.txt_DMDSizeX.toPlainText().replace(".", "", 1).isdigit()) or not(self.ui.txt_DMDSizeY.toPlainText().replace(".", "", 1).isdigit()):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('DMD calibration ratio and DMD X & Y size must be numeric.')
            error_dialog.exec_()
            return
        if self.ui.radioButton_CamDMD2ImageMask.isChecked():
            checkState = 1
        else:
            checkState = 0
        calValues = np.array([
            float(self.ui.txt_DMDSizeX.toPlainText()),
            float(self.ui.txt_DMDSizeY.toPlainText()), 
            float(checkState),
            float(self.ui.txt_CalPositionX.toPlainText()), 
            float(self.ui.txt_CalPositionY.toPlainText()),
            float(self.ui.txt_CalRotation.toPlainText()),
            float(self.ui.txt_CalWidth.toPlainText()),
            float(self.ui.txt_CalHeight.toPlainText()),
            float(self.ui.txt_CalibrationThreshold.toPlainText())
        ])
        try:
            self.calibration = sr.ShapeDetector(self.fileNameCameraImage, calValues)
        except ValueError:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Problem with Calibration Image File.')
            error_dialog.exec_()
            return
        try:
            self.cntrPoints = self.calibration.detectCalibration()
            height1D, width1D = self.calibration.sourceImage.shape
            rgbImage = np.zeros([height1D, width1D, 3] , dtype=np.uint8)
            rgbImage[:,:,0] = self.calibration.sourceImage
            rgbImage[:,:,1] = self.calibration.sourceImage
            rgbImage[:,:,2] = self.calibration.sourceImage
            cv2.drawContours(rgbImage, [self.cntrPoints], 0, (255, 0, 0), 5)
            self.showImageInView(rgbImage, self.ui.view_CameraImage)
            self.calibrationValuesStorage = np.array([
                float(self.calibration.DMDSizeX),
                float(self.calibration.DMDSizeY), 
                float(self.calibration.shapeColour),
                float(self.calibration.positionX),
                float(self.calibration.positionY),
                float(self.calibration.rotation),
                float(self.calibration.width),
                float(self.calibration.height),
                float(self.calibration.thresholdCalibrationValue)
                ], dtype=float)
            self.calibrationImageStorage = self.fileNameCameraImage
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Problem with Calibration Threshold level set.')
            error_dialog.exec_()
            return
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
            self.ui.txt_CalPositionX.setEnabled(False)
            self.ui.txt_CalPositionY.setEnabled(False)
            self.ui.radioButton_CamDMD2ImageMask.setEnabled(False)
            self.ui.radioButton_CamDMD1ImageMask.setEnabled(False)
            self.ui.txt_CalRotation.setEnabled(False)
            self.ui.txt_CalWidth.setEnabled(False)
            self.ui.txt_CalHeight.setEnabled(False)
            self.ui.btn_SaveCalibration.setEnabled(False)
            self.ui.btn_Calibrate.setEnabled(False)
            self.ui.txt_CalibrationThreshold.setEnabled(False)
        elif not(self.ui.cbox_LockCalibration.isChecked()):
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_CalPositionX.setEnabled(True)
            self.ui.txt_CalPositionY.setEnabled(True)
            self.ui.radioButton_CamDMD2ImageMask.setEnabled(True)
            self.ui.radioButton_CamDMD1ImageMask.setEnabled(True)
            self.ui.txt_CalRotation.setEnabled(True)
            self.ui.txt_CalWidth.setEnabled(True)
            self.ui.txt_CalHeight.setEnabled(True)
            self.ui.btn_SaveCalibration.setEnabled(True)
            self.ui.btn_Calibrate.setEnabled(True)
            self.ui.txt_CalibrationThreshold.setEnabled(True)
        else:
            self.ui.txt_DMDSizeX.setEnabled(True)
            self.ui.txt_DMDSizeY.setEnabled(True)
            self.ui.txt_CalPositionX.setEnabled(True)
            self.ui.txt_CalPositionY.setEnabled(True)
            self.ui.radioButton_CamDMD2ImageMask.setEnabled(True)
            self.ui.radioButton_CamDMD1ImageMask.setEnabled(True)
            self.ui.txt_CalRotation.setEnabled(True)
            self.ui.txt_CalWidth.setEnabled(True)
            self.ui.txt_CalHeight.setEnabled(True)
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
            self.Mask = self.maskGenerationCalibration(self.ui.radioButton_CamDMD2DMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 1:
            self.Mask = self.maskGenerationThreshold(self.ui.radioButton_CamDMD2DMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 2:
            self.Mask = self.maskGenerationSlit(self.ui.radioButton_CamDMD2DMDMask.isChecked())
        elif self.ui.tab_MaskFunctionality.currentIndex() == 3:
            self.Mask = self.maskGenerationPinhole(self.ui.radioButton_CamDMD2DMDMask.isChecked())
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
            DefaultSaveName = './Masks/Calibration/CalibrationMask-' + str(self.maskCountCalibration) + '_CCSize-' + self.ui.txt_CentreCircleSize.toPlainText() + '.bmp'
            self.maskCountCalibration = self.maskCountCalibration + 1
        elif self.MaskChoice == 1:
            DefaultSaveName = './Masks/Threshold/ThresholdMask-' + str(self.maskCountThreshold) + '.bmp'
            self.maskCountThreshold = self.maskCountThreshold + 1
        elif self.MaskChoice == 2:
            DefaultSaveName = './Masks/Slit/SlitMask-' + str(self.maskCountSlit) + '_NumSlits-' + str(self.ui.spinBox_NumberOfSlits.value()) + '_Width-' + self.ui.txt_SlitWidth.toPlainText() + '_Separation-' + self.ui.txt_SlitSeparation.toPlainText() + '_Rotation' + self.ui.txt_SlitRotation.toPlainText() + '.bmp'
            self.maskCountSlit = self.maskCountSlit + 1
        elif self.MaskChoice == 3:
            DefaultSaveName = './Masks/Pinhole/PinholeMask-' + str(self.maskCountPinhole) + '_NumPinholes-' + str(self.ui.spinBox_NumberOfPinholes.value()) + '_Radius-' + self.ui.txt_PinholeRadius.toPlainText() + 'Pitch-' + self.ui.txt_PinholePitch.toPlainText() + '_Rotation' + self.ui.txt_PinholeRotation.toPlainText() + '.bmp'
            self.maskCountPinhole = self.maskCountPinhole + 1
        else:
            imwrite('./Masks/Mask.bmp', self.Mask)
        saveMask = self.Mask.astype(np.uint8)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",DefaultSaveName,"All Files (*);;Bitmap (*.bmp)", options=options)
        imwrite(fileName, saveMask)
        return

    @pyqtSlot()
    def onClick_ConnectDMD(self):
        try:
            if self.DMDConnectFlag == False:
                self.DMD = ALP4(version = '4.3', libDir = 'C:/Program Files/ALP-4.3/ALP-4.3 API')
            self.DMD.Initialize()
            self.DMDConnectFlag = True
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('DMD not connected.')
            error_dialog.exec_()
            return
        if self.DMD.nSizeX != int(float(self.ui.txt_DMDSizeX.toPlainText())) or self.DMD.nSizeY != int(float(self.ui.txt_DMDSizeY.toPlainText())):
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Size of DMD connected (' + str(self.DMD.nSizeX) + 'x' + str(self.DMD.nSizeY) + ' is not the same as the calibration settings. Calibration required.')
            error_dialog.exec_()
            self.onClick_LockCalibration()
            self.ui.cbox_LockCalibration.setChecked(False)
        self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/green.png"))
        return

    @pyqtSlot()
    def onClick_DisconnectDMD(self):
        try:
            self.DMD.Halt()
            if self.DMDDisplayFlag == True:
                self.DMD.FreeSeq()
            self.DMD.Free()
            self.ui.view_DMDConnectionStatus.setPixmap(QtGui.QPixmap("./TestImages/red.png"))
            self.DMDConnectFlag = False
            self.DMDDisplayFlag = False
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return

    @pyqtSlot()
    def onClick_CamDMD1DMD(self):
        try:
            mask = np.ones([self.DMD.nSizeY, self.DMD.nSizeX])*(2**8-1)
            # Binary amplitude image (0 or 1)
            bitDepth = 1    
            # Allocate the onboard memory for the image sequence
            self.DMD.SeqAlloc(nbImg = 1, bitDepth = bitDepth)
            # Send the image sequence as a 1D list/array/numpy array
            self.DMD.SeqPut(imgData = mask)
            # Set image rate to 50 Hz
            #DMD.SetTiming(pictureTime = 20000)
            self.DMD.Run()
            self.DMDConnectFlag = True
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return

    @pyqtSlot()
    def onClick_CamDMD2DMD(self):
        try:
            mask = np.zeros([self.DMD.nSizeY,self.DMD.nSizeX])
            # Binary amplitude image (0 or 1)
            bitDepth = 1    
            # Allocate the onboard memory for the image sequence
            self.DMD.SeqAlloc(nbImg = 1, bitDepth = bitDepth)
            # Send the image sequence as a 1D list/array/numpy array
            self.DMD.SeqPut(imgData = mask)
            # Set image rate to 50 Hz
            #DMD.SetTiming(pictureTime = 20000)
            self.DMD.Run()
            self.DMDConnectFlag = True
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return

    @pyqtSlot()
    def onClick_HaltDMD(self):
        try:
            self.DMD.Halt()
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return

    @pyqtSlot()
    def onClick_DMDDisplayCurrentMask(self):
        try:
            mask = self.Mask
            # Binary amplitude image (0 or 1)
            bitDepth = 1    
            # Allocate the onboard memory for the image sequence
            self.DMD.SeqAlloc(nbImg = 1, bitDepth = bitDepth)
            # Send the image sequence as a 1D list/array/numpy array
            self.DMD.SeqPut(imgData = mask)
            # Set image rate to 50 Hz
            #DMD.SetTiming(pictureTime = 20000)
            self.DMD.Run()
            self.DMDConnectFlag = True
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return

    @pyqtSlot()
    def onClick_DMDDisplayFileMask(self):
        try:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileNameMaskDisplay, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;tiff (*.tiff);;tif (*.tif);;png (*.png)", options=options)
            maskToDisplay = plt.imread(fileNameMaskDisplay)
            maskToDisplay = maskToDisplay.astype(dtype = np.uint8)
            # Binary amplitude image (0 or 1)
            bitDepth = 1    
            # Allocate the onboard memory for the image sequence
            self.DMD.SeqAlloc(nbImg = 1, bitDepth = bitDepth)
            # Send the image sequence as a 1D list/array/numpy array
            self.DMD.SeqPut(imgData = maskToDisplay)
            # Set image rate to 50 Hz
            #DMD.SetTiming(pictureTime = 20000)
            self.DMD.Run()
            self.DMDConnectFlag = True
            return
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No DMD Connected.")
            error_dialog.exec_()
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = appMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
