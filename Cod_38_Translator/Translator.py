''' Tanslator app for languages
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_38_Translator/Translator.py
# dependencies 
need to install 'googletrans'  used uv add googletrans, 
Note : not using textblob in this appliocation 

If googletrans still gives errors, you may need to switch to deep-translator, translate, or the official Google Cloud Translation API.

ou're correct that the translate() method from the TextBlob library no longer works as expected. The translate() and detect_language() methods relied on the Google Translate unofficial API, which has been shut down or now requires an API key (and is not integrated into TextBlob by default anymore).

✅ Solution: Use googletrans directly
Since you're already importing googletrans, you should stop using TextBlob for translation and instead use googletrans.Translator() directly.
mportant Notes About googletrans:
Some versions of googletrans (e.g., googletrans==4.0.0rc1) are broken because of changes to the Google Translate web API.
Recommended to install the actively maintained fork:
pip install googletrans==4.0.0-rc1
or the forked alternative:

pip install googletrans==4.0.0rc1
If googletrans still gives errors, you may need to switch to deep-translator, translate, or the official Google Cloud Translation API.
'''
# I believe the translate attribute for textblob library has been cahnged. What would be the correct syntax. my error mesasage is that there is no translate attribute.
# Shared_Folders/pyqt5_Codemy/Cod_38_Translator/Translator.py
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QComboBox,QMessageBox
import sys
from PyQt5 import uic
import googletrans
# import textblob
from googletrans import Translator
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi('Cod_38_Translator/Translator.ui',self)
        self.textEdit_1 =self.findChild(QTextEdit,'textEdit_1')
        self.textEdit_2 =self.findChild(QTextEdit,'textEdit_2')
        self.comboBox_1 = self.findChild(QComboBox,'comboBox_1')
        self.comboBox_2 = self.findChild(QComboBox,'comboBox_2')
        self.translate=self.findChild(QPushButton,'translate')
        self.Close= self.findChild(QPushButton,'close')
        
        self.translate.clicked.connect(lambda : self.Translate(self))
        self.Close.clicked.connect(lambda : self.clear())
        
        self.languages = googletrans.LANGUAGES
        # print(self.languages)#'es' is spanish 'la': 'latin' 'ja': 'japanese''eo': 'esperanto''en': 'english'
        # ## list of languages , the values
        self.languages_list=list(self.languages.values())
        # print(self.languages_list)
        
        ## add items to combo boxes
        self.comboBox_1.addItems(self.languages_list)
        self.comboBox_2.addItems(self.languages_list)
        
        # set default comboitems
        self.comboBox_1.setCurrentText('english')
        self.comboBox_2.setCurrentText('spanish')
        # self.comboBox_2.setCurrentText('english')
 
    def Translate(self, s):
        print('translate')
        s.translate.setStyleSheet('color:red;')
        try:
            from_language_key = None
            to_language_key = None

            # Get language codes from combobox selections
            for key, value in self.languages.items():
                if value == self.comboBox_1.currentText():
                    from_language_key = key
                if value == self.comboBox_2.currentText():
                    to_language_key = key

            if not from_language_key or not to_language_key:
                raise Exception("Could not determine language keys.")

            # Perform the translation
            translator = Translator()
            text = self.textEdit_1.toPlainText()
            translated = translator.translate(text, src=from_language_key, dest=to_language_key)

            # Output translated text
            self.textEdit_2.setText(translated.text)

        except Exception as e:
            QMessageBox.about(self, 'Translator', str(e))


    def clear(self):
        print('close')
        self.textEdit_1.setText('')   # clear the textEdit boxes 
        self.textEdit_2.setText('')    
            #Re-set default comboitems
        self.comboBox_1.setCurrentText('english')
        self.comboBox_2.setCurrentText('spanish')

if __name__ =='__main__':
    app =QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
# <?xml version="1.0" encoding="UTF-8"?>
# <ui version="4.0">
#  <class>MainWindow</class>
#  <widget class="QMainWindow" name="MainWindow">
#   <property name="geometry">
#    <rect>
#     <x>0</x>
#     <y>0</y>
#     <width>734</width>
#     <height>455</height>
#    </rect>
#   </property>
#   <property name="windowTitle">
#    <string>MainWindow</string>
#   </property>
#   <widget class="QWidget" name="centralwidget">
#    <widget class="QTextEdit" name="textEdit_1">
#     <property name="geometry">
#      <rect>
#       <x>33</x>
#       <y>-7</y>
#       <width>231</width>
#       <height>201</height>
#      </rect>
#     </property>
#    </widget>
#    <widget class="QTextEdit" name="textEdit_2">
#     <property name="geometry">
#      <rect>
#       <x>470</x>
#       <y>0</y>
#       <width>231</width>
#       <height>201</height>
#      </rect>
#     </property>
#    </widget>
#    <widget class="QComboBox" name="comboBox_1">
#     <property name="geometry">
#      <rect>
#       <x>20</x>
#       <y>230</y>
#       <width>250</width>
#       <height>70</height>
#      </rect>
#     </property>
#     <property name="currentText">
#      <string/>
#     </property>
#    </widget>
#    <widget class="QComboBox" name="comboBox_2">
#     <property name="geometry">
#      <rect>
#       <x>460</x>
#       <y>240</y>
#       <width>250</width>
#       <height>50</height>
#      </rect>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="translate">
#     <property name="geometry">
#      <rect>
#       <x>270</x>
#       <y>30</y>
#       <width>191</width>
#       <height>71</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>24</pointsize>
#      </font>
#     </property>
#     <property name="text">
#      <string>Translate</string>
#     </property>
#    </widget>
#    <widget class="QPushButton" name="close">
#     <property name="geometry">
#      <rect>
#       <x>310</x>
#       <y>150</y>
#       <width>112</width>
#       <height>51</height>
#      </rect>
#     </property>
#     <property name="font">
#      <font>
#       <pointsize>18</pointsize>
#      </font>
#     </property>
#     <property name="text">
#      <string>close</string>
#     </property>
#    </widget>
#   </widget>
#   <widget class="QMenuBar" name="menubar">
#    <property name="geometry">
#     <rect>
#      <x>0</x>
#      <y>0</y>
#      <width>734</width>
#      <height>37</height>
#     </rect>
#    </property>
#   </widget>
#   <widget class="QStatusBar" name="statusbar"/>
#  </widget>
#  <resources/>
#  <connections/>
# </ui>
