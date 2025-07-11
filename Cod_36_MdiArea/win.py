'''
Codemy PyQt5 Course - MDI Area Example
This script demonstrates how to create a Multiple Document Interface (MDI) application using PyQt5.
It includes a main window with a menu to open child windows, each containing a text editor. 
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_36_MdiArea/win.py
Sylesheets
QLineEdit {
background:rgb(255, 169, 105);
border: 10px solid rgb(63, 255, 236);
border-radius: 280 px}

QLineEdit:focus{ border:10px rgb(255, 82, 48);
background: rgb(137, 255, 179)}
QPushButton{
background: rgb(111, 195, 255);
bprder: 2 px solid rgb(250, 255, 72);
border-radius: 20 px;
color:black}
QPushButton:hover{background-color:rgb(255, 149, 79);
border:2 px solid rgb(255, 138, 74);
border-radius: 20 px:
color:green}
'''
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_36_MdiArea/win.ui
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QMenuBar,QMdiArea, QLabel,QPushButton,QMdiSubWindow,QTextEdit
import sys
from PyQt5 import uic
from PyQt5 import QtGui

class MainWindow(QMainWindow):
    count =0 ## will access this by calling it MainWIndow.count
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Cod_36_MdiArea/win.ui',self)
        ## add menubar and menus
        # <addaction name="actionWindow_1"/>
        # <addaction name="actionWindow_2"/>
        # <addaction name="actionWindow_3"/>
        self.idx =None
        self.actionWindow_1.triggered.connect( lambda  idx =self.idx: self.Window_1(self,idx))
        self.actionWindow_2.triggered.connect(lambda : self.Window_1(self))
        self.actionWindow_3.triggered.connect(lambda : self.Window_1(self))
        ## add the pushbutton,label,mdiArea
        self.label=self.findChild(QLabel,'label')
        self.pushbutton =self.findChild(QPushButton,'pushButton')
        self.mdi=self.findChild(QMdiArea,'mdiArea')
        ## create a pushbutton clicked connect to open a window
        self.pushbutton.clicked.connect(self.open_window)

    def Window_1(self,s,idx):
        print('actionWindow_1',s)
        print(idx)
        s.label.setStyleSheet('color:red;')
        s.mdi.setStyleSheet('color:red;')
        
    def open_window(self):  # to show app
        MainWindow.count += 1
        # create sub windows\
        sub =QMdiSubWindow()
        ## have it do something
        sub.setWidget(QTextEdit())
        ## set the titlebar  or the subWIndow
        sub.setWindowTitle(f'My Sub Window  {MainWindow.count}')
        ## ADD the sub window into our midiWidget
        self.mdi.addSubWindow(sub)
        ## show the new sub
        sub.show()
        
		# Position the sub windows
		# tile them
		# self.mdi.tileSubWindows()

		# Cascade them
        self.mdi.cascadeSubWindows()

		# Do more fun stuff...
		# self.mdi.closeActiveSubWindow()
		# self.mdi.removeSubWindow()
		# self.mdi.subWindowList()
        
        
if __name__ =='__main__':
    app =QApplication(sys.argv)
    window =MainWindow()
    window.show()
    sys.exit(app.exec_())