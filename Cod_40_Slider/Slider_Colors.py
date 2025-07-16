'''
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_40_Slider/Slider_Colors.py
1. Codemy 40 tutorial on Sliders
2. incorporate Paul McWHorter UDP control of LEDS
3. Add second windows using the menubar action

'''
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QPushButton,QSlider,QLabel
from PyQt5 import uic
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_40_Slider/Slider_Colors.ui',self)
        self.red=self.findChild(QPushButton,'pushButton_1')
        self.red.setStyleSheet('background-color: red;')
        self.green=self.findChild(QPushButton,'pushButton_2')
        self.blue=self.findChild(QPushButton,'pushButton_3')
        self.slider =self.findChild(QSlider,'Slider')
        self.label=self.findChild(QLabel,'label')
        ## add menubar
        self.actionwindow_1.triggered.connect(lambda : self.change('red')) ## add menu triggers, could make a def .Red etc function for each trigger
        
        
    def change(self,var):
        print('change',var)  
        
        
if __name__=='__main__':
    app =QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())
    

    #     self.actionRed.triggered.connect(lambda : self.change('red')) ## add menu triggers, could make a def .Red etc function for each trigger
    #     self.actionBlue.triggered.connect(lambda : self.change('blue')) ## but since all do the same thing will just make one function
    #     self.actionGreen.triggered.connect(lambda : self.change('green'))
    #     self.actionYellow.triggered.connect(lambda : self.change('yellow'))
    #     self.actionMagenta.triggered.connect(lambda : self.change('magenta'))
    #     self.actionBlack.triggered.connect(lambda : self.change('black'))
    #     self.actionWhite.triggered.connect(lambda : self.change('white'))
    #     self.actionGray.triggered.connect(lambda : self.change('gray'))
    #     ## open the second Window
    #     #  <string>Second Window</string>
    #     # </property>
    #     # <addaction name="actionSecond_Page"/>
    #     self.actionSecond_Page.triggered.connect(lambda : self.second())
        
    # def change(self,color):
    #     print('color',color)
    #     self.setStyleSheet(f'background-color: {color};')
    #     self.setWindowTitle(f'You changed the color to {color.title()}')
            
        
    # def second(self):
    #     print('open')
    #     self.second_window=SecondWindow()
    #     self.second_window.show()        
        