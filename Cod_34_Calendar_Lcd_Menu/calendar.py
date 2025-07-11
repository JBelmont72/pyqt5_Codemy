'''Codemy 33,34,35 Use Menubar,QCalendarWidget,QLCDNumber, Open multiple windows using uic
In the mainWIndow has calendar and secondWindow LCD Number
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_34_Calendar_Lcd_Menu/calendar.py
https://www.tutorialspoint.com/pyqt/pyqt_qtimeedit.htm
https://pythonpyqt.com/pyqt-qtextedit/
mdi is multiple defined interface

'''
/Shared_Folders/pyqt5_Codemy/Cod_34_Calendar_Lcd_Menu/calendar.py
from PyQt5.QtWidgets import QApplication,QMainWindow,QCalendarWidget,QLabel,QPushButton,QMenuBar,QLCDNumber,QTimeEdit
import sys
from PyQt5 import QtGui
from PyQt5 import uic
## imprt a QTimer
from PyQt5.QtCore import QTime,QTimer
from datetime import datetime

class LCD_Window(QMainWindow):
    def __init__(self, ):
        super(LCD_Window,self).__init__()
        uic.loadUi('Cod_34_Calendar_Lcd_Menu/LCD_Window.ui',self)
        self.setStyleSheet('background-color:blue;')
        self.LCD=self.findChild(QLCDNumber,'lcdNumber')
        self.timeLabel=self.findChild(QLabel,'label')
        ## using QTimeEdit. https://www.tutorialspoint.com/pyqt/pyqt_qtimeedit.htm
        self.timeEdit=self.findChild(QTimeEdit,'timeEdit')
        self.timeEdit.setTime(QTime.currentTime()) # Set initial time to current time
        self.timeEdit.setDisplayFormat("hh:mm:ss AP") # Set display format
        
        ## create a Timer
        self.timer=QTimer()
        self.timer.timeout.connect(self.lcd_number)
        # start the timer and updte every second ( in milliseconds)
        self.timer.start(1000)
        ## !!! call the lcd_number function
        self.lcd_number()
        
        ## menubar actions for time and timeEdit under -Time
        self.actionTime.triggered.connect(lambda : self.myTime())
        self.actionTime_Edit.triggered.connect(lambda: self.importTime(self))

        self.show()
    def lcd_number(self):       # connected to QTimer
        # get the time
        time=datetime.now()     ## %H is 24 hr time, %I is regualr time
        formatted_time =time.strftime('%H:%M:%S %p')
        # set number of digits for clock default is 4
        self.LCD.setDigitCount(12)
        ## to make the text flat if desired
        self.LCD.setSegmentStyle(QLCDNumber.Flat)
        
        
        
        self.LCD.display(formatted_time)
        self.timeLabel.setText(formatted_time)
    
    def myTime(self):
        print('the time')
    def importTime(self,s):
        # s is an instance of LCD_Window
        print(s)  # prints the object representation

        # Access the QTimeEdit widget and get the current time
        current_time = s.timeEdit.time()
        print("Current time in QTimeEdit:", current_time.toString())

        # Set the LCD display to show the time from QTimeEdit
        formatted_time = current_time.toString("hh:mm:ss AP")
        s.LCD.display(formatted_time)
        s.timeLabel.setText(formatted_time)

        # Change the background color of only the QTimeEdit widget
        s.timeEdit.setStyleSheet('background-color: green;')

        # Access the LCD digit count
        digit_count = s.LCD.digitCount()
        print("LCD digit count:", digit_count)

        # You can also stop the timer if needed
        # s.timer.stop()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Cod_34_Calendar_Lcd_Menu/calendar.ui',self)
        self.color='red'
        self.var =0
        ## first add actions for the menubar, do not use 'findChild'
    # <addaction name="actionOpen_Calendar"/>
    # <addaction name="actionOption_1"/>
    # <addaction name="actionOption_2"/>
        self.actionOpen_Calendar.triggered.connect(lambda :self.open_calendar())
        self.actionOption_1.triggered.connect(lambda: self.option_1(self.var))  ## option_1 is the LCD Window
        self.actionOption_2.triggered.connect(lambda: self.option_2(self.color)) ## option_2 is the color change
        
        ## for menuLCD_Clock
        self.actionOpen_Clock.triggered.connect(lambda: self.Open_Clock(self.var)) # Open LCD Clock
        self.actionClock_Option_1.triggered.connect(lambda: self.ClockOption(self.var))
        self.pushButton=self.findChild(QPushButton,'pushButton')
        self.date=self.findChild(QLabel,'label')
        self.time=self.findChild(QLabel,'label_2')
        ## add the Calendar widget
        self.calendar=self.findChild(QCalendarWidget,'calendarWidget')
        # connect the calendar to a function
        self.calendar.selectionChanged.connect(lambda :self.myCalendar())
        
        
    def myCalendar(self):
        dateSelected= self.calendar.selectedDate()
        # self.label.setText(str(dateSelected))    
        # self.label.setText(str(dateSelected.toPyDate()))   ## workd year-month-date 
        self.label.setText(str(dateSelected.toString()))   ## gives day of week,name of month,day number,year
        print(str(dateSelected.toJulianDay()))  
        
        
    def open_calendar(self):
        print('calendar opened')
        self.setStyleSheet(f'background-color: lightgreen;')
        self.setWindowTitle(f'This is Judsons Calendar')
        
    def option_1(self,var):
        print(var)
        self.second_window=LCD_Window()
        self.second_window.show()
    def option_2(self,color):
        print('color',color)
        self.mycolor =color
        self.setStyleSheet(f'background-color: {color};')
        self.setWindowTitle(f'You changed the color to {color.title()}')
        if self.mycolor=='red':
            self.color= 'yellow'
        else:
            self.color ='red'
    def Open_Clock(self,var):
        print('Open LCD Clock')
    def ClockOption(self,var):
        print('Clock Option ',var)
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


