# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalii.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    import playsound
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, shutil
from librosa.core.spectrum import _spectrogram
import numpy as np
import pyqtgraph as pg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from datetime import datetime
import pyqtgraph
import pyqtgraph.exporters
import matplotlib.pyplot as plt
#from main_layout import Ui_MainWindow
import scipy.io.wavfile
import librosa.display
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
import numpy.fft as fft
import scipy.signal
from scipy import fftpack
from scipy import signal
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import matplotlib.pyplot as plt
import wx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, FigureCanvasQTAgg
from matplotlib.figure import Figure
import sounddevice as sd



class MplCanvas(FigureCanvasQTAgg):

   def __init__(self, parent=None, width=5, height=5, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.tight_layout()
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1782, 989)
        MainWindow.setStyleSheet("QMainWindow { background-color:white; }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.main_tab.setFont(font)
        self.main_tab.setStyleSheet("QPushButton { background-color: yellow; }")
        self.main_tab.setIconSize(QtCore.QSize(50, 151))
        self.main_tab.setElideMode(QtCore.Qt.ElideNone)
        self.main_tab.setObjectName("main_tab")
        self.tab_equalizer = QtWidgets.QWidget()
        self.tab_equalizer.setObjectName("tab_equalizer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_equalizer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.equalizer_splitter = QtWidgets.QSplitter(self.tab_equalizer)
        self.equalizer_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.equalizer_splitter.setObjectName("equalizer_splitter")
        self.equalizer_splitter.setStyleSheet("QSplitter {background-image:url(18\.jpg);background-position: center;}")
        
        self.graph_splitter = QtWidgets.QSplitter(self.equalizer_splitter)
        self.graph_splitter.setOrientation(QtCore.Qt.Vertical)
        self.graph_splitter.setObjectName("graph_splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.graph_splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph_layout.setContentsMargins(0, 0, 0, 0)
        self.graph_layout.setObjectName("graph_layout")
        self.music_signal = PlotWidget(self.verticalLayoutWidget)
        self.music_signal.setObjectName("music_signal")
        self.music_signal.setBackground('w')
        
        self.graph_layout.addWidget(self.music_signal)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem)
        self.stop_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop_button.setMaximumSize(QtCore.QSize(90, 90))
        self.stop_button.setStyleSheet("QPushButton { background-color:black ; \n"
"                     border-radius : 45;}")
        self.stop_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/stop-button2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon)
        self.stop_button.setIconSize(QtCore.QSize(90, 90))
        self.stop_button.setAutoDefault(False)
        self.stop_button.setDefault(False)
        self.stop_button.setFlat(False)
        self.stop_button.setObjectName("stop_button")
        self.buttons_layout.addWidget(self.stop_button)
        self.play_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.play_button.setMaximumSize(QtCore.QSize(90, 90))
        self.play_button.setAutoFillBackground(False)
        self.play_button.setStyleSheet("QPushButton { background-color:black ;\n"
"                      border-radius : 45; }")
        self.play_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/play-button2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QtCore.QSize(90, 90))
        self.play_button.setObjectName("play_button")
        self.buttons_layout.addWidget(self.play_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttons_layout.addItem(spacerItem1)
        self.graph_layout.addLayout(self.buttons_layout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.graph_splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.spectrogram_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.spectrogram_layout.setContentsMargins(0, 0, 0, 0)
        self.spectrogram_layout.setObjectName("spectrogram_layout")
        self.spectrogram_title_layout = QtWidgets.QHBoxLayout()
        self.spectrogram_title_layout.setObjectName("spectrogram_title_layout")
        self.spectrogram_title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spectrogram_title.setFont(font)
        self.spectrogram_title.setStyleSheet("QLabel { color: blue;}")
        self.spectrogram_title.setAlignment(QtCore.Qt.AlignCenter)
        self.spectrogram_title.setObjectName("spectrogram_title")
        self.spectrogram_title_layout.addWidget(self.spectrogram_title)
        self.spectrogram_layout.addLayout(self.spectrogram_title_layout)
        self.spectro_widget = QtWidgets.QWidget(self.verticalLayoutWidget_3)
        self.spectro_widget=MplCanvas(self)
        
        self.spectro_widget.setObjectName("spectro_widget")
        self.spectrogram_layout.addWidget(self.spectro_widget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.equalizer_splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.setting_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.setting_layout.setContentsMargins(0, 0, 0, 0)
        self.setting_layout.setObjectName("setting_layout")
        self.setting_layout2 = QtWidgets.QVBoxLayout()
        self.setting_layout2.setObjectName("setting_layout2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.setting_layout2.addItem(spacerItem2)
        self.volume_layout = QtWidgets.QHBoxLayout()
        self.volume_layout.setObjectName("volume_layout")
        self.volume_line1 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.volume_line1.setStyleSheet("Line { color: white; }")
        self.volume_line1.setMidLineWidth(5)
        self.volume_line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.volume_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.volume_line1.setObjectName("volume_line1")
        self.volume_layout.addWidget(self.volume_line1)
        self.volume_level_title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.volume_level_title.setFont(font)
        self.volume_level_title.setStyleSheet("QLabel { color: blue;}")
        self.volume_level_title.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_level_title.setObjectName("volume_level_title")
        self.volume_layout.addWidget(self.volume_level_title)
        self.volume_line2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.volume_line2.setStyleSheet("Line { color: blue; }")
        self.volume_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.volume_line2.setLineWidth(1)
        self.volume_line2.setMidLineWidth(5)
        self.volume_line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.volume_line2.setObjectName("volume_line2")
        self.volume_layout.addWidget(self.volume_line2)
        self.setting_layout2.addLayout(self.volume_layout)
        self.volume_control = QtWidgets.QDial(self.verticalLayoutWidget_2)
        self.volume_control.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.volume_control.setFont(font)
        self.volume_control.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.volume_control.setStyleSheet("QDial { background-color:blue; }")
        self.volume_control.setProperty("value", 25)
        self.volume_control.setSliderPosition(25)
        self.volume_control.setOrientation(QtCore.Qt.Horizontal)
        self.volume_control.setWrapping(False)
        self.volume_control.setNotchesVisible(True)
        self.volume_control.setObjectName("volume_control")
        self.setting_layout2.addWidget(self.volume_control)
        self.music_layout = QtWidgets.QHBoxLayout()
        self.music_layout.setObjectName("music_layout")
        self.musical_line1 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.musical_line1.setMidLineWidth(5)
        self.musical_line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.musical_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.musical_line1.setObjectName("musical_line1")
        self.music_layout.addWidget(self.musical_line1)
        self.musical_setting_title = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.musical_setting_title.setFont(font)
        self.musical_setting_title.setStyleSheet("QLabel { color: blue;}")
        self.musical_setting_title.setAlignment(QtCore.Qt.AlignCenter)
        self.musical_setting_title.setObjectName("musical_setting_title")
        self.music_layout.addWidget(self.musical_setting_title)
        self.musical_line2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.musical_line2.setMidLineWidth(5)
        self.musical_line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.musical_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.musical_line2.setObjectName("musical_line2")
        self.music_layout.addWidget(self.musical_line2)
        self.setting_layout2.addLayout(self.music_layout)
        self.musical_setting_layout = QtWidgets.QHBoxLayout()
        self.musical_setting_layout.setObjectName("musical_setting_layout")
        self.drums_layout = QtWidgets.QVBoxLayout()
        self.drums_layout.setObjectName("drums_layout")
        self.drums_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.drums_slider.setMaximumSize(QtCore.QSize(35, 500))
        self.drums_slider.setProperty("value", 50)
        self.drums_slider.setOrientation(QtCore.Qt.Vertical)
        self.drums_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.drums_slider.setTickInterval(5)
        self.drums_slider.setObjectName("drums_slider")
        self.drums_layout.addWidget(self.drums_slider)
        self.drums_icon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.drums_icon.setMaximumSize(QtCore.QSize(50, 50))
        self.drums_icon.setStyleSheet("QLabel { background-color: white; }")
        self.drums_icon.setText("")
        self.drums_icon.setPixmap(QtGui.QPixmap("drum-kit.png"))
        self.drums_icon.setScaledContents(True)
        self.drums_icon.setObjectName("drums_icon")
        self.drums_layout.addWidget(self.drums_icon)
        self.musical_setting_layout.addLayout(self.drums_layout)
        self.piano_layout = QtWidgets.QVBoxLayout()
        self.piano_layout.setObjectName("piano_layout")
        self.piano_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.piano_slider.setMaximumSize(QtCore.QSize(35, 500))
        self.piano_slider.setProperty("value", 50)
        self.piano_slider.setOrientation(QtCore.Qt.Vertical)
        self.piano_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.piano_slider.setTickInterval(5)
        self.piano_slider.setObjectName("piano_slider")
        self.piano_layout.addWidget(self.piano_slider)
        self.piano_icon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.piano_icon.setMaximumSize(QtCore.QSize(50, 50))
        self.piano_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.piano_icon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.piano_icon.setText("")
        self.piano_icon.setPixmap(QtGui.QPixmap("preview.jpg"))
        self.piano_icon.setScaledContents(True)
        self.piano_icon.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.piano_icon.setObjectName("piano_icon")
        self.piano_layout.addWidget(self.piano_icon)
        self.musical_setting_layout.addLayout(self.piano_layout)
        self.flute_layout = QtWidgets.QVBoxLayout()
        self.flute_layout.setObjectName("flute_layout")
        self.flute_slider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.flute_slider.setMaximumSize(QtCore.QSize(35, 500))
        self.flute_slider.setStyleSheet("QSliderl { color: blue; }")
        self.flute_slider.setProperty("value", 50)
        self.flute_slider.setOrientation(QtCore.Qt.Vertical)
        self.flute_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.flute_slider.setTickInterval(5)
        self.flute_slider.setObjectName("flute_slider")
        self.flute_layout.addWidget(self.flute_slider)
        self.flute_icon = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.flute_icon.setMaximumSize(QtCore.QSize(50, 50))
        self.flute_icon.setText("")
        self.flute_icon.setPixmap(QtGui.QPixmap("flute.jpg"))
        self.flute_icon.setScaledContents(True)
        self.flute_icon.setObjectName("flute_icon")
        self.flute_layout.addWidget(self.flute_icon)
        self.musical_setting_layout.addLayout(self.flute_layout)
        self.setting_layout2.addLayout(self.musical_setting_layout)
        self.setting_layout.addLayout(self.setting_layout2)
        self.gridLayout_2.addWidget(self.equalizer_splitter, 0, 0, 1, 1)
        self.main_tab.addTab(self.tab_equalizer, "")
        self.virtual_intrument_tab = QtWidgets.QWidget()
        self.virtual_intrument_tab.setObjectName("virtual_intrument_tab")
        self.tabWidget = QtWidgets.QTabWidget(self.virtual_intrument_tab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1931, 941))
        self.tabWidget.setObjectName("tabWidget")
        self.piano_tab = QtWidgets.QWidget()
        self.piano_tab.setObjectName("piano_tab")
        self.piano = QtWidgets.QLabel(self.piano_tab)
        self.piano.setGeometry(QtCore.QRect(30, 40, 1571, 641))
        self.piano.setText("")
        self.piano.setPixmap(QtGui.QPixmap("img/484-4844993_keyboard-cartoon-piano-hd-png-download.png"))
        self.piano.setScaledContents(True)
        self.piano.setObjectName("piano")
        self.C_piano = QtWidgets.QPushButton(self.piano_tab)
        self.C_piano.setGeometry(QtCore.QRect(210, 170, 151, 501))
        self.C_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C_piano.setText("")
        self.C_piano.setObjectName("C_piano")
        self.D_piano = QtWidgets.QPushButton(self.piano_tab)
        self.D_piano.setGeometry(QtCore.QRect(360, 170, 141, 501))
        self.D_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D_piano.setText("")
        self.D_piano.setObjectName("D_piano")
        self.E_piano = QtWidgets.QPushButton(self.piano_tab)
        self.E_piano.setGeometry(QtCore.QRect(500, 170, 151, 501))
        self.E_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.E_piano.setText("")
        self.E_piano.setObjectName("E_piano")
        self.F_piano = QtWidgets.QPushButton(self.piano_tab)
        self.F_piano.setGeometry(QtCore.QRect(650, 170, 151, 501))
        self.F_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.F_piano.setText("")
        self.F_piano.setObjectName("F_piano")
        self.G_piano = QtWidgets.QPushButton(self.piano_tab)
        self.G_piano.setGeometry(QtCore.QRect(800, 170, 151, 501))
        self.G_piano.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.G_piano.setText("")
        self.G_piano.setObjectName("G_piano")
        self.B_piano = QtWidgets.QPushButton(self.piano_tab)
        self.B_piano.setGeometry(QtCore.QRect(950, 170, 141, 501))
        self.B_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B_piano.setText("")
        self.B_piano.setObjectName("B_piano")
        self.A_piano = QtWidgets.QPushButton(self.piano_tab)
        self.A_piano.setGeometry(QtCore.QRect(1090, 170, 151, 501))
        self.A_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A_piano.setText("")
        self.A_piano.setObjectName("A_piano")
        self.D2_piano = QtWidgets.QPushButton(self.piano_tab)
        self.D2_piano.setGeometry(QtCore.QRect(1240, 170, 151, 501))
        self.D2_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D2_piano.setText("")
        self.D2_piano.setObjectName("D2_piano")
        self.E2_piano = QtWidgets.QPushButton(self.piano_tab)
        self.E2_piano.setGeometry(QtCore.QRect(1390, 170, 141, 501))
        self.E2_piano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.E2_piano.setText("")
        self.E2_piano.setObjectName("E2_piano")
        self.c_piano = QtWidgets.QPushButton(self.piano_tab)
        self.c_piano.setGeometry(QtCore.QRect(320, 170, 81, 281))
        self.c_piano.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.c_piano.setText("")
        self.c_piano.setObjectName("c_piano")
        self.d2_paino = QtWidgets.QPushButton(self.piano_tab)
        self.d2_paino.setGeometry(QtCore.QRect(1350, 170, 81, 281))
        self.d2_paino.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.d2_paino.setText("")
        self.d2_paino.setObjectName("d2_paino")
        self.d_piano = QtWidgets.QPushButton(self.piano_tab)
        self.d_piano.setGeometry(QtCore.QRect(460, 170, 81, 281))
        self.d_piano.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.d_piano.setText("")
        self.d_piano.setObjectName("d_piano")
        self.f_piano = QtWidgets.QPushButton(self.piano_tab)
        self.f_piano.setGeometry(QtCore.QRect(760, 170, 81, 281))
        self.f_piano.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.f_piano.setText("")
        self.f_piano.setObjectName("f_piano")
        self.g_piano = QtWidgets.QPushButton(self.piano_tab)
        self.g_piano.setGeometry(QtCore.QRect(920, 170, 81, 281))
        self.g_piano.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.g_piano.setText("")
        self.g_piano.setObjectName("g_piano")
        self.a_piano = QtWidgets.QPushButton(self.piano_tab)
        self.a_piano.setGeometry(QtCore.QRect(1200, 170, 81, 281))
        self.a_piano.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.a_piano.setText("")
        self.a_piano.setObjectName("a_piano")
        self.tone_slider = QtWidgets.QSlider(self.piano_tab)
        self.tone_slider.setGeometry(QtCore.QRect(1690, 80, 41, 541))
        self.tone_slider.setOrientation(QtCore.Qt.Vertical)
        self.tone_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.tone_slider.setTickInterval(5)
        self.tone_slider.setObjectName("tone_slider")
        self.keyboard = QtWidgets.QLabel(self.piano_tab)
        self.keyboard.setGeometry(QtCore.QRect(290, 760, 901, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboard.setFont(font)
        self.keyboard.setStyleSheet("QLabel { color: blue;}")
        self.keyboard.setAlignment(QtCore.Qt.AlignCenter)
        self.keyboard.setObjectName("keyboard")
        self.tone_label = QtWidgets.QLabel(self.piano_tab)
        self.tone_label.setGeometry(QtCore.QRect(1660, 630, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tone_label.setFont(font)
        self.tone_label.setStyleSheet("QLabel { color: blue;}")
        self.tone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tone_label.setObjectName("tone_label")
        self.tabWidget.addTab(self.piano_tab, "")
        self.guitar_tap = QtWidgets.QWidget()
        self.guitar_tap.setObjectName("guitar_tap")
        self.guitar = QtWidgets.QLabel(self.guitar_tap)
        self.guitar.setGeometry(QtCore.QRect(50, 40, 1651, 741))
        self.guitar.setText("")
        self.guitar.setPixmap(QtGui.QPixmap("img/unnamed.png"))
        self.guitar.setScaledContents(True)
        self.guitar.setObjectName("guitar")
        self.E1_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.E1_guitar.setGeometry(QtCore.QRect(950, 430, 211, 16))
        self.E1_guitar.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.E1_guitar.setText("")
        self.E1_guitar.setFlat(True)
        self.E1_guitar.setObjectName("E1_guitar")
        self.B_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.B_guitar.setGeometry(QtCore.QRect(410, 440, 151, 16))
        self.B_guitar.setStyleSheet("background-color: rgb(213, 164, 111);")
        self.B_guitar.setText("")
        self.B_guitar.setFlat(True)
        self.B_guitar.setObjectName("B_guitar")
        self.D_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.D_guitar.setGeometry(QtCore.QRect(420, 390, 111, 16))
        self.D_guitar.setStyleSheet("background-color: rgb(208, 159, 110);")
        self.D_guitar.setText("")
        self.D_guitar.setFlat(True)
        self.D_guitar.setObjectName("D_guitar")
        self.A_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.A_guitar.setGeometry(QtCore.QRect(440, 350, 91, 16))
        self.A_guitar.setStyleSheet("background-color: rgb(208, 157, 102);")
        self.A_guitar.setText("")
        self.A_guitar.setFlat(True)
        self.A_guitar.setObjectName("A_guitar")
        self.E_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.E_guitar.setGeometry(QtCore.QRect(990, 360, 131, 16))
        self.E_guitar.setStyleSheet("background-color: rgb(88, 84, 84);")
        self.E_guitar.setText("")
        self.E_guitar.setFlat(True)
        self.E_guitar.setObjectName("E_guitar")
        self.G_guitar = QtWidgets.QPushButton(self.guitar_tap)
        self.G_guitar.setGeometry(QtCore.QRect(1000, 400, 93, 16))
        self.G_guitar.setStyleSheet("background-color: rgb(64, 59, 57);")
        self.G_guitar.setText("")
        self.G_guitar.setFlat(True)
        self.G_guitar.setObjectName("G_guitar")
        self.tabWidget.addTab(self.guitar_tap, "")
        self.drums_tab = QtWidgets.QWidget()
        self.drums_tab.setObjectName("drums_tab")
        self.drum = QtWidgets.QLabel(self.drums_tab)
        self.drum.setGeometry(QtCore.QRect(30, 30, 1771, 871))
        self.drum.setText("")
        self.drum.setPixmap(QtGui.QPixmap("img/images.jpg"))
        self.drum.setScaledContents(True)
        self.drum.setObjectName("drum")
        self.drum_center = QtWidgets.QPushButton(self.drums_tab)
        self.drum_center.setGeometry(QtCore.QRect(750, 320, 441, 71))
        self.drum_center.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.drum_center.setText("")
        self.drum_center.setFlat(True)
        self.drum_center.setObjectName("drum_center")
        self.drum_buttom = QtWidgets.QPushButton(self.drums_tab)
        self.drum_buttom.setGeometry(QtCore.QRect(750, 570, 411, 51))
        self.drum_buttom.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.drum_buttom.setText("")
        self.drum_buttom.setFlat(True)
        self.drum_buttom.setObjectName("drum_buttom")
        self.tabWidget.addTab(self.drums_tab, "")
        self.main_tab.addTab(self.virtual_intrument_tab, "")
        self.horizontalLayout.addWidget(self.main_tab)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1782, 26))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_action.setFont(font)
        self.open_action.setObjectName("open_action")
        self.menuOpen.addAction(self.open_action)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spectrogram_title.setText(_translate("MainWindow", "Spectrogram"))
        self.volume_level_title.setText(_translate("MainWindow", "Volume level"))
        self.musical_setting_title.setText(_translate("MainWindow", "Musical settings"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.tab_equalizer), _translate("MainWindow", "Equalizer"))
        self.C_piano.setShortcut(_translate("MainWindow", "A"))
        self.D_piano.setShortcut(_translate("MainWindow", "S"))
        self.E_piano.setShortcut(_translate("MainWindow", "D"))
        self.F_piano.setShortcut(_translate("MainWindow", "F"))
        self.G_piano.setShortcut(_translate("MainWindow", "H"))
        self.B_piano.setShortcut(_translate("MainWindow", "G"))
        self.A_piano.setShortcut(_translate("MainWindow", "J"))
        self.D2_piano.setShortcut(_translate("MainWindow", "K"))
        self.E2_piano.setShortcut(_translate("MainWindow", "L"))
        self.c_piano.setShortcut(_translate("MainWindow", "Z"))
        self.d2_paino.setShortcut(_translate("MainWindow", "N"))
        self.d_piano.setShortcut(_translate("MainWindow", "X"))
        self.f_piano.setShortcut(_translate("MainWindow", "C"))
        self.g_piano.setShortcut(_translate("MainWindow", "V"))
        self.a_piano.setShortcut(_translate("MainWindow", "B"))
        self.keyboard.setText(_translate("MainWindow", "If you want to use keyboard, press keys: A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N"))
        self.tone_label.setText(_translate("MainWindow", "Tones"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.piano_tab), _translate("MainWindow", "piano"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.guitar_tap), _translate("MainWindow", "guitar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.drums_tab), _translate("MainWindow", "drums"))
        self.main_tab.setTabText(self.main_tab.indexOf(self.virtual_intrument_tab), _translate("MainWindow", "Virtual instruments"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.open_action.setText(_translate("MainWindow", "Upload the signal"))
#------------------------------setting------------------------------------------

# --------------------------- equalizer tab setting------------------------
        self.timer1 = QtCore.QTimer()
        self.drawing_pen = pg.mkPen(color=(0, 0, 255), width=0.5)
        self.player = QMediaPlayer()  
        
        self.drums_slider.setValue(50)
        self.piano_slider.setValue(50)
        self.flute_slider.setValue(50)
        self.spectro_widget.hide()
        self.spectrogram_title.hide()
        
        self.open_action.triggered.connect(lambda:self.open_audio_file())
        self.volume_control.valueChanged.connect(lambda:self.volume_change())
        self.play_button.clicked.connect(lambda: self.play() )
        self.stop_button.clicked.connect(lambda: self.stop() )
        self.piano_slider.sliderReleased.connect(lambda:self.piano_frequency())
        self.flute_slider.sliderReleased.connect(lambda:self.flute_frequency())
        self.drums_slider.sliderReleased.connect(lambda:self.drums_frequency())
 # --------------------------- instrument tab setting------------------------

        #white buttons  piano
        self.C_piano.clicked.connect(lambda:self.get_song_data(0))
        self.A_piano.clicked.connect(lambda:self.get_song_data(2))
        self.D_piano.clicked.connect(lambda:self.get_song_data(4))
        self.B_piano.clicked.connect(lambda:self.get_song_data(5))
        self.E_piano.clicked.connect(lambda:self.get_song_data(7))
        self.F_piano.clicked.connect(lambda:self.get_song_data(9))
        self.D2_piano.clicked.connect(lambda:self.get_song_data(11))
        self.E2_piano.clicked.connect(lambda:self.get_song_data(12))
        self.G_piano.clicked.connect(lambda:self.get_song_data(13))
        #black buttons piano
        
        self.c_piano.clicked.connect(lambda:self.get_song_data(1))
        self.d_piano.clicked.connect(lambda:self.get_song_data(3))
        self.g_piano.clicked.connect(lambda:self.get_song_data(6))
        self.f_piano.clicked.connect(lambda:self.get_song_data(8))
        self.a_piano.clicked.connect(lambda:self.get_song_data(10))
        self.d2_paino.clicked.connect(lambda:self.get_song_data(14))
        
        
        #guitar
        self.E_guitar.clicked.connect(lambda:self.get_Guitar_note(0))
        self.A_guitar.clicked.connect(lambda:self.get_Guitar_note(1))
        self.D_guitar.clicked.connect(lambda:self.get_Guitar_note(2))
        self.G_guitar.clicked.connect(lambda:self.get_Guitar_note(3))
        self.B_guitar.clicked.connect(lambda:self.get_Guitar_note(4))
        self.E1_guitar.clicked.connect(lambda:self.get_Guitar_note(5))
        
        
        
        #drums
        self.drum_center.clicked.connect(lambda:self.drums(2))
        self.drum_buttom.clicked.connect(lambda:self.drums(0))
       
        #-------------------------------------------------------------------------------------------
 ##piano generation     
        self.tone_slider.setMinimum(2)
        self.tone_slider.setMaximum(20)
        self.tone_slider.setValue(0)
        self.tone_slider.setTickInterval(2)


#----------------------------function----------------------------------
    open_flag=1
    def open_audio_file(self):
        self.music_signal.clear()
        if self.open_flag==1: 
            self.sound_file = QtWidgets.QFileDialog.getOpenFileName(None, 'Load Audio', './', "Audio File(*.wav)")[0]
            self.path_soundfile=self.sound_file
            self.sampling_rate1, self.samples1 = scipy.io.wavfile.read(self.sound_file)
            self.spectrum_before_update=self.spectrum_original()
        
        self.sampling_rate_copy, self.samples_copy = scipy.io.wavfile.read(self.path_soundfile)
        peak_value = np.amax(self.samples_copy)
        self.normalized_data = self.samples_copy / peak_value
        length = self.samples_copy.shape[0] / self.sampling_rate_copy
        self.time = list(np.linspace(0, length, self.samples_copy.shape[0]))
        self.data_line = self.music_signal.plot(self.time, self.normalized_data, pen=self.drawing_pen)
        self.idx1 = 0
        self.timer1.setInterval(20)
        self.timer1.timeout.connect(self.update_plot_data)
        self.timer1.start()
        url = QUrl.fromLocalFile(self.path_soundfile)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
        self.player.setVolume(20)
        self.volume_change()
        self.spectrogram()
        
    def update_plot_data(self):
        x_next = self.time[:self.idx1]
        y_next= self.normalized_data[:self.idx1]
        self.idx1 += 8000
        # shrink range of x-axis
        self.music_signal.plotItem.setXRange(
        max(x_next, default=0)-9, max(x_next, default=0))
        # Plot the new data
        self.data_line.setData(x_next, y_next)  
    
    current_value_volume=20   
    def volume_change(self):
        
        if self.volume_control.value() > self.current_value_volume:
            self.current_value_volume= self.volume_control.value()
            self.player.setVolume(self.current_value_volume+self.current_value_volume*(self.volume_control.value()/100))
       
        elif  self.volume_control.value() < self.current_value_volume:
            self.current_value_volume= self.volume_control.value()
            self.player.setVolume(self.current_value_volume-self.current_value_volume*(self.volume_control.value()/100))
        
        elif  self.volume_control.value() == self.current_value_volume:
            self.player.setVolume(self.current_value_volume)

        elif  self.volume_control.value() == 0:
            self.player.setVolume(0)
            
    def play(self): 
       
        self.player.play()
        self.timer1.start()

    def stop(self):
         self.player.pause()
         self.timer1.stop()
         
    def spectrogram(self):
        self.spectrogram_title.show()

        VMIN = None 
        VMAX = -40
        dt = np.mean(np.diff(self.time))
        fs = int(1/dt)
        self.amp = self.normalized_data 
        self.spectro_widget.show()
        self.spectro_widget.fig.clear()
        self.axes=self.spectro_widget.fig.add_subplot(111)
        self.spectro_widget.draw()
        pxx,  freq, t, cax=self.axes.specgram(self.amp, Fs=fs,cmap='viridis',vmin=VMIN,vmax=VMAX)
        self.axes.set_xlabel('time')
        self.axes.set_ylabel('frequency')
        self.spectro_widget.fig.colorbar(cax)
        self.spectro_widget.draw()
        
    no_change=1
    new_file_pointer=-1
    list_file=["newsound.wav","newsound1.wav"]
    def create_new_sound(self,slider_value):
            
        if self.new_file_pointer==1:
          os.remove("newsound.wav")
          os.remove("newsound1.wav")
          self.new_file_pointer=-1
        self.signal = self.samples_copy[:]
        self.spectrum =np.fft.rfft(self.signal)
        self.freq = np.fft.rfftfreq(self.signal.size, d=1./self.sampling_rate_copy) 
        for i,f in enumerate(self.freq):
            if (f >= self.lower_frequency) and (f<=self.higher_frequency)  :
                self.spectrum[i] =self.spectrum_before_update[i]*slider_value/50
           
        self.newSound = np.fft.irfft(self.spectrum)
        self.new_file_pointer+=1
        scipy.io.wavfile.write(self.list_file[self.new_file_pointer], self.sampling_rate_copy, self.newSound.astype(np.int16))
        self.path_soundfile=self.list_file[self.new_file_pointer]   
        self.open_flag=0
        self.open_audio_file()
        
    def piano_frequency (self):
        self.lower_frequency=0
        self.higher_frequency=2000 
        self.create_new_sound(self.piano_slider.value())         
    def flute_frequency (self):
        self.lower_frequency=2000
        self.higher_frequency=5500
        self.create_new_sound(self.flute_slider.value()) 
    def drums_frequency (self):
        self.lower_frequency=5500
        self.higher_frequency=10500
        self.create_new_sound(self.drums_slider.value()) 
        
        
    def spectrum_original(self):
        self.signal_nature = self.samples1[:]
        self.spectrum_nature =np.fft.rfft(self.signal_nature)
        return self.spectrum_nature
#--------------------------------------------------------------------------------------------------------------------------------
#                                         virtual instrument functions:    
    sample_rate = 56100 #Hz

    def get_wave(self,freq, duration=0.5):
        self.amplitude = 4096
        a=self.tone_slider.value()  
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        self.wave = self.amplitude * np.sin(a* np.pi * freq * t)

        return (self.wave)

    def get_piano_notes(self):
        self.octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B','D','E','d']
        self.base_freq = 261.63

        self.note_freqs = {self.octave[i]:self.base_freq*pow(2, (i/12)) for i in range(len(self.octave))}
        self.note_freqs[''] = 0.0
        
        return self.note_freqs

    def get_song_data(self,i):
        self.octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B','D','E','d']
    
        note_freqs = self.get_piano_notes()
        self.sound=self.octave[i]
        self.song = [self.get_wave(self.note_freqs[note]) for note in self.sound.split('-')]
        self.song = np.concatenate(self.song)
        self.data=self.song.astype(np.int16)
        self.data = self.data * (16300/np.max(self.data))
        self.data2=self.data.astype(np.int16)

        sd.play(self.data2)
        status = sd.wait() 
## guitar generation
        
    def karplus_strong( self,wavetable, n_samples):
     

        self.samples = []
        self.current_sample = 0
        self.previous_value = 0

        while len(self.samples) < n_samples:
            wavetable[self.current_sample] = 0.5 * (wavetable[self.current_sample] + self.previous_value)
            self.samples.append(wavetable[self.current_sample])
            self.previous_value = self.samples[-1]
            self.current_sample += 1
            self.current_sample = self.current_sample % wavetable.size
        self.wave=np.array(self.samples)



    def get_guitar_freqs(self):
        octave = ['E','A','D','G','B','E_2']

        base_freq = 105  # Frequency of Note C4

        self.note_freqs = [base_freq + 5*i for i in range(len(octave))]
        
    samplerate=44100
    def get_Guitar_note(self, freq):
        self.get_guitar_freqs()
        print(self.note_freqs[freq])

        
        self.wavetable_size = self.samplerate //self.note_freqs[freq]
        self.wavetable = (2 * np.random.randint(0, 2,self.wavetable_size) - 1).astype(np.float)
        self.karplus_strong(self.wavetable, self.samplerate)
        self.stringwave = self.wave
        sd.play(self.stringwave, self.samplerate, blocking=True)    
        
        
       #drums generation 
    def karplus_strong_drum(self, wavetable, n_samples, prob):
      
        samples = []
        current_sample = 0
        previous_value = 0
        while len(samples) < n_samples:
            r = np.random.binomial(1, prob)
            sign = float(r == 1) * 2 - 1
            wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)
            samples.append(wavetable[current_sample])
            previous_value = samples[-1]
            current_sample += 1
            current_sample = current_sample % wavetable.size
        return np.array(samples)

    def drums (self,index):
        self.parameter_b_values = [0.3, 0.7, 0.5]
        self.parameter_fs_values = [8000, 12000, 10000]
        self.parameter_b = self.parameter_b_values [index]
        fs = self.parameter_fs_values[index]

        wavetable_size = fs // 40
        wavetable = np.ones(wavetable_size)
        sample = self.karplus_strong_drum(wavetable, 1 * fs, self.parameter_b)
        sd.play(sample, fs, blocking=True)

    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        

from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
