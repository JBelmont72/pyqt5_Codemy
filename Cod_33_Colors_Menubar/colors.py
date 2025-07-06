'''. Episode 33 of Codemy PyQt5 changing the window color with the menubar
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_youtube_playlist/Cod_33_Colors_Menubar/colors.py


'''
# from PyQt5.QtWidgets import QMenuBar,QMainWindow,QApplication
# from PyQt5 import QtGui
# from PyQt5 import uic
# import sys
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('Cod_33_Colors_Menubar/colors.ui',self)
        
#         ## normally would add findChild widgets
#         ## for the menubar we will add the actions
#         #. Add Menu Triggers the actions from the .ui
#         # <addaction name="actionRed"/> from .ui
#         # <addaction name="actionBlue"/>
#         # <addaction name="actionGreen"/>
#         # <addaction name="actionYellow"/>
#         # <addaction name="actionMagenta"/>
#         # <addaction name="actionBlack"/>
#         # <addaction name="actionWhite"/>
#         # <addaction name="actionGray"/>
        
#         self.actionRed.triggered.connect(lambda : self.change('red')) ## add menu triggers, could make a def .Red etc function for each trigger
#         self.actionBlue.triggered.connect(lambda : self.change('blue')) ## but since all do the same thing will just make one function
#         self.actionGreen.triggered.connect(lambda : self.change('green'))
#         self.actionYellow.triggered.connect(lambda : self.change('yellow'))
#         self.actionMagenta.triggered.connect(lambda : self.change('magenta'))
#         self.actionBlack.triggered.connect(lambda : self.change('black'))
#         self.actionWhite.triggered.connect(lambda : self.change('white'))
#         self.actionGray.triggered.connect(lambda : self.change('gray'))
#         ## open the second Window
#         #  <string>Second Window</string>
#         # </property>
#         # <addaction name="actionSecond_Page"/>
#         self.actionSecond_Page.triggered.connect(lambda : self.second())
        
#     def change(self,color):
#         print('color',color)
#         self.setStyleSheet(f'background-color: {color};')
#         self.setWindowTitle(f'You changed the color to {color.title()}')
            
        
#     def second(self):
#         print('open') 
        
        
from PyQt5.QtWidgets import QMenuBar,QMainWindow,QApplication
from PyQt5 import QtGui
from PyQt5 import uic
import sys
class SecondWindow(QMainWindow):
    def __init__(self, ):
        super(SecondWindow,self).__init__()
        uic.loadUi('Cod_33_Colors_Menubar/secondWindow.ui',self)
        
        self.show()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Cod_33_Colors_Menubar/colors.ui',self)
    
        
        self.actionRed.triggered.connect(lambda : self.change('red')) ## add menu triggers, could make a def .Red etc function for each trigger
        self.actionBlue.triggered.connect(lambda : self.change('blue')) ## but since all do the same thing will just make one function
        self.actionGreen.triggered.connect(lambda : self.change('green'))
        self.actionYellow.triggered.connect(lambda : self.change('yellow'))
        self.actionMagenta.triggered.connect(lambda : self.change('magenta'))
        self.actionBlack.triggered.connect(lambda : self.change('black'))
        self.actionWhite.triggered.connect(lambda : self.change('white'))
        self.actionGray.triggered.connect(lambda : self.change('gray'))
        ## open the second Window
        #  <string>Second Window</string>
        # </property>
        # <addaction name="actionSecond_Page"/>
        self.actionSecond_Page.triggered.connect(lambda : self.second())
        
    def change(self,color):
        print('color',color)
        self.setStyleSheet(f'background-color: {color};')
        self.setWindowTitle(f'You changed the color to {color.title()}')
            
        
    def second(self):
        print('open')
        self.second_window=SecondWindow()
        self.second_window.show()        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
## include second window
