''' Tanslator app for languages
/Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_38_Translator/Translator.py
# dependencies 
need to install 'googletrans'  used uv add googletrans, 
Note : not using textblob in this appliocation 

If googletrans still gives errors, you may need to switch to deep-translator, translate, or the official Google Cloud Translation API.

ou're correct that the translate() method from the TextBlob library no longer works as expected. The translate() and detect_language() methods relied on the Google Translate unofficial API, which has been shut down or now requires an API key (and is not integrated into TextBlob by default anymore).

✅ Solution: Use googletrans directly
Since you're already importing googletrans, you should stop using TextBlob for translation and instead use googletrans.Translator() directly.
Important Notes About googletrans:
Some versions of googletrans (e.g., googletrans==4.0.0rc1) are broken because of changes to the Google Translate web API.
Recommended to install the actively maintained fork:
pip install googletrans==4.0.0-rc1
or the forked alternative:

pip install googletrans==4.0.0rc1
If googletrans still gives errors, you may need to switch to deep-translator, translate, or the official Google Cloud Translation API.

JBelmont72: isn't the value always equal to the self.comboBox_1.currentText() because we are selecting that value  and it is always the the same?

GitHub.copilot-chat.github.copilot.editor: Not always. Here’s why:

- `self.languages.items()` is a dictionary of language codes and their display names, e.g. `{ 'en': 'English', 'fr': 'French' }`.
- `self.comboBox_1.currentText()` returns the currently selected display name in the combo box, e.g. `'French'`.

The loop:
```python
for key, value in self.languages.items():
    if value == self.comboBox_1.currentText():
        from_language_key = key
```
checks each language name (`value`) against the selected combo box text. Only the matching language gets its key assigned to `from_language_key`.

**Why this is needed:**  
The combo box only stores/display names (e.g. `'French'`), but you need the code (e.g. `'fr'`) for translation. The loop finds the code for the selected language.

**Gotcha:**  
If your combo box contains all values from `self.languages`, then yes, one of the values will always match the current text, but not all will. The loop is necessary to find which key matches the selected value.

**Example:**
- Combo box shows: English, French, Spanish
- User selects "French"
- Loop finds that `'French'` matches, so `from_language_key = 'fr'`

**Summary:**  
The value is only equal to `self.comboBox_1.currentText()` for the selected language, not for every item in the loop. The loop is needed to map the display name back to its code.
'''
# I believe the translate attribute for textblob library has been cahnged. What would be the correct syntax. my error mesasage is that there is no translate attribute.
# Shared_Folders/pyqt5_Codemy/Cod_38_Translator/Translator.py
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QComboBox,QMessageBox
import sys
from PyQt5 import uic
import googletrans
# import textblob
from googletrans import Translator
import pyttsx3
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
        
        self.languages = googletrans.LANGUAGES  # dictionary
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
                if value == self.comboBox_1.currentText():## find the value in the self.languages.items() that is equal fo the comboBOx1
                    from_language_key = key ## this alllows us to get the right key out of all the possible options in the dictionary
                if value == self.comboBox_2.currentText():
                    to_language_key = key

            if not from_language_key or not to_language_key:
                raise Exception("Could not determine language keys.")

            # Perform the translation
            translator = Translator()
            text = self.textEdit_1.toPlainText()
            translated = translator.translate(text, src=from_language_key, dest=to_language_key)
            # print(translated,'   ',translated.src,'   ',translated.extra_data)
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

## Codem39 add text to speech
'''
Pywin32 is specifically designed for Windows and does not have a version for macOS. For speech functionality on macOS, consider using libraries like PyObjC or other speech synthesis libraries compatible with macOS
PyWin32 and Speech on macOS
Overview of PyWin32
PyWin32 is a set of Python extensions that provide access to many Windows APIs, including support for COM (Component Object Model). However, PyWin32 is specifically designed for Windows environments and does not have a version for macOS.
Speech Functionality on macOS
For text-to-speech functionality on macOS, you can use the built-in say command in Python. Here’s how to implement it:
Install Python: Ensure you have Python installed on your macOS.
Using the os Module: You can use the os module to call the say command directly from Python.
Example Code
Here’s a simple example to convert text to speech:
python
Copy Code
import os

text = "Hello, this is a text to speech example."
os.system(f'say "{text}"')
Alternative Libraries
If you prefer a library approach, consider using pyttsx3, which is a text-to-speech conversion library that works across platforms, including macOS.
Install pyttsx3:
bash
Copy Code
pip install pyttsx3
Example Code:
python
Copy Code
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is a text to speech example.")
engine.runAndWait()
Conclusion
While PyWin32 is not available for macOS, you can easily implement text-to-speech functionality using the built-in say command or libraries like pyttsx3.
#JBelmont72: i am using the pyttsx3 library to add speech. the text in self.textEdit_1 speaks but not in textEdit_2.  

# GitHub.copilot-chat.github.copilot.editor: To fix the issue so that both the original and translated text are spoken, ensure that the translated text is not empty before calling the speech engine and move the speech code after setting the translated text.
   

'''
# from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QComboBox,QMessageBox
# import sys
# from PyQt5 import uic
# import googletrans
# # import textblob
# from googletrans import Translator
# import pyttsx3

# # engine = pyttsx3.init()
# # engine.say("Hello, this is a text to speech example.")
# # engine.runAndWait()

# class MainWindow(QMainWindow):

#     # engine = pyttsx3.init()
#     # engine.say("Hello, this is a text to speech example.")
#     # engine.runAndWait()

#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator.ui',self)
#         self.textEdit_1 =self.findChild(QTextEdit,'textEdit_1')
#         self.textEdit_2 =self.findChild(QTextEdit,'textEdit_2')
#         self.comboBox_1 = self.findChild(QComboBox,'comboBox_1')
#         self.comboBox_2 = self.findChild(QComboBox,'comboBox_2')
#         self.translate=self.findChild(QPushButton,'translate')
#         self.Close= self.findChild(QPushButton,'close')
        
#         self.translate.clicked.connect(lambda : self.Translate(self))
#         self.Close.clicked.connect(lambda : self.clear())
        
#         self.languages = googletrans.LANGUAGES  # dictionary
#         # print(self.languages)#'es' is spanish 'la': 'latin' 'ja': 'japanese''eo': 'esperanto''en': 'english'
#         # ## list of languages , the values
#         self.languages_list=list(self.languages.values())
#         # print(self.languages_list)
        
#         ## add items to combo boxes
#         self.comboBox_1.addItems(self.languages_list)
#         self.comboBox_2.addItems(self.languages_list)
        
#         # set default comboitems
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')
#         # self.comboBox_2.setCurrentText('english')

#         engine=pyttsx3.init()
#         self.engine=engine
#     def Translate(self, s):
#         print('translate')
#         s.translate.setStyleSheet('color:red;')
#         try:
#             from_language_key = None
#             to_language_key = None

#             # Get language codes from combobox selections
#             for key, value in self.languages.items():
#                 if value == self.comboBox_1.currentText():## find the value in the self.languages.items() that is equal fo the comboBOx1
#                     from_language_key = key ## this alllows us to get the right key out of all the possible options in the dictionary
#                 if value == self.comboBox_2.currentText():
#                     to_language_key = key

#             if not from_language_key or not to_language_key:
#                 raise Exception("Could not determine language keys.")

#             # Perform the translation
#             translator = Translator()
#             text = self.textEdit_1.toPlainText()
#             self.engine.say(text)
#             self.engine.runAndWait()
#             translated = translator.translate(text, src=from_language_key, dest=to_language_key)
#             # print(translated,'   ',translated.src,'   ',translated.extra_data)
#             # Output translated text
#             self.textEdit_2.setText(translated.text)
#             if translated.text:
#                 self.engine.say(translated.text)
#                 self.engine.runAndWait()
      

#         except Exception as e:
#             QMessageBox.about(self, 'Translator', str(e))


#     def clear(self):
#         print('close')
#         self.textEdit_1.setText('')   # clear the textEdit boxes 
#         self.textEdit_2.setText('')    
#             #Re-set default comboitems
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')

# if __name__ =='__main__':
#     app =QApplication(sys.argv)
#     window=MainWindow()
#     window.show()
#     sys.exit(app.exec_())
    
    
# import sys
# from PyQt5 import uic, QtWidgets
# import googletrans as gt  # pip install googletrans==4.0.0-rc1 to avoid some errors with version 3+. If using a newer version of PyQT then use 'pip install googletrans==4.0' instead
# from gtts import gTTS     # pip install gTTs for text-to-speech function
# import os                 # This is used to play the converted audio in wav format
# import playsound          # pip install playsound==1.2.2 so that it works with Python 3, newer versions cause issues on some systems
# from googletrans import LANGUAGES

# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator.ui',self)
#         # uic.loadUi('Translator.ui', self)  # Load the UI File created with Qt Designer and named 'Translator'
#         self.setFixedSize(800, 650)         # Fix window size to prevent resizing issues
#         self.translate_button =self.findChild(QtWidgets.QPushButton,'translate')
#         self.clear_button= self.findChild(QtWidgets.QPushButton,'close')
#         self.source_textedit =self.findChild(QtWidgets.QTextEdit,'textEdit_1')
#         self.translated_textedit =self.findChild(QtWidgets.QTextEdit,'textEdit_2')
#         self.fromlangComboBox=self.findChild(QtWidgets.QComboBox, 'comboBox_1')
#         self.tolangComboBox=self.findChild(QtWidgets.QComboBox, 'comboBox_2')

#         # Fill the comboboxes with language options from googletrans LANGUAGES dictionary
#         for lang in list(LANGUAGES.values()):
#             self.fromlangComboBox.addItem(lang)   # add item to fromLang Combo Box
#             self.tolangComboBox.addItem(lang)     # add item to ToLang Combo Box
#         indexFrom = self.fromlangComboBox.findText(LANGUAGES['en'])  # Find the index of 'english' in the combo box
#         self.fromlangComboBox.setCurrentIndex(indexFrom)  # Set English to be current selection for FromLang Combo Box
#         indexTo = LANGUAGES['es']      # get the index of Spanish in the dictionary and store it for later usage, as we want spanish set by default
#         self.tolangComboBox.setCurrentIndex(int(indexTo)-1)  # Set English to be current selection for ToLang Combo Box

#         self.translate_button.clicked.connect(self.Translate)   # call Translate function when translate button is clicked
#         self.clear_button.clicked.connect(self.Clear)            # call Clear function when clear button is clicked

#     def TextToSpeech(self, text):  # Function to convert text to speech using gTTS
#         tts = gTTS(text=text, lang='en')   # Create a new instance of the gTTS class with English as default language for now
#         filename = "voice.mp3"             # Define output file name and format
#         tts.save(filename)                  # Save speech to an audio file (will be saved in same folder where Python script is located)
#         playsound.playsound("voice.mp3")    # Play the audio file that was just created using the playsound module
#         os.remove(filename)                # Delete the audio file as it is no longer needed to free up space, or comment this line if you want to keep them for future use

#     def Translate(self):  # Function called when translate button is clicked
#         try:
#             text = self.source_textedit.toPlainText()     # Get source language from the TextEdit box and store it in a variable named 'text'
#             translator = gt.Translator()                   # Create new instance of Translator class from googletrans module
#             translation1=translator.translate(text, src='en', dest=self.tolangComboBox.currentText())  # Use translate method to convert 'text' variable contents from English to language selected in ToLang Combo Box and store result in a variable named 'translation1'. The src parameter is not necessary if the source language can be detected by googletrans, but it may cause errors sometimes so its better to specify
#             self.translated_textedit.setText(str(translation1.text))   # Display translation1 contents in Translated TextEdit box
#             self.TextToSpeech(translation1.text)                       # Call TextToSpeech function with 'translation' variable content as argument to convert it into speech and play the audio file generated by that function
#         except Exception as e:
#             print("An error occurred:", str(e))  # Print any errors if they occur during execution of above try block code lines. This is useful for debugging purposes. You can remove this line or comment out '#' symbol at beginning of it to disable printing errors in the console window while running script normally without causing issues on some systems
#             self.translated_textedit.setText("An error occurred: " + str(e))  # Display error message within Translated TextEdit box instead if one occurs during execution of above try block code lines so that user can see what went wrong easily rather than checking console window for it which might be confusing to some users who are not familiar with how programming works.
#     def Clear(self):   # Function called when clear button is clicked
#         self.source_textedit.clear()           # Delete any text in the source language TextEdit box using clear method of QTextEdit class from PyQt5 module which was imported at beginning of script line by line starting with first import statement
#         self.translated_textedit.clear()       # Delete any text in translated language TextEdit box using same way as above for it too (with different variable name since they are separate boxes) so that both boxes will end up empty after clear button clicked once
# if __name__ == "__main__":    # This is the entry point of our script. If this file was imported instead of running directly then the following code inside if block would not be executed automatically, thus preventing any errors caused by it from happening when importing module into another script or interactive shell session like Jupyter Notebook for example
#     app = QtWidgets.QApplication(sys.argv)   # Create new instance of QApplication class which will handle GUI-related tasks such as event loop, widget management etc (without this line no GUIs can be created using PyQt5 since it relies on a running application object to do so). sys module provides access to some variables used or maintained by the Python interpreter and argv is one of them which contains list of command-line arguments passed in when script was run from terminal window/command prompt etc.
#     mainWindow = MainWindow()  # Create new instance of our MainWindow class (defined above) which inherits QMainWindow class so that we can use all its methods and properties too (since inheritance allows us to extend functionality without modifying original code). This will create an empty window with just title bar at this point since no widgets have been added yet.
#     mainWindow.show()         # Display our Main Window on screen by calling show method inherited from QWidget class via MainWindow -> QMainWindow (since Qt5 does not have a standalone TopLevel Widget like Tkinter does) so that user can see and interact with it as desired.
#     sys.exit(app.exec_())     # Start event loop of our application object which handles events such as mouse clicks, keyboard presses etc by calling exec_ method inherited from QCoreApplication class via QtWidgets -> QMainWindow since all GUIs require an event loop running continuously to function properly and allow user input/output interactions with widgets within window. This line makes sure that script does not terminate prematurely before any events occur or are handled which could cause errors in some cases such as trying to access non-existing objects/widgets after they have been deleted from memory already due to application closing immediately without waiting for user input first






 ## MISTY  
# from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QTextEdit, QComboBox, QPushButton, QMessageBox
# import sys
# from PyQt5 import uic
# import googletrans as trans  # Fixed 't' in Translator

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         # uic.loadUi('Translator.ui', self)
#         uic.loadUi('Cod_38_Translator/Translator.ui',self)
        
#         self.textEdit_1 = self.findChild(QTextEdit, 'textEdit_1')
#         self.textEdit_2 = self.findChild(QTextEdit, 'textEdit_2')
#         self.comboBox_1 = self.findChild(QComboBox, 'comboBox_1')
#         self.comboBox_2 = self.findChild(QComboBox, 'comboBox_2')
        
#         # Initialize engine once
#         try:
#             fromLanguageKey = None
#             toLanguageKey = None

#             if not hasattr(trans, 'Translator'):
#                 QMessageBox.critical(self, "Error", "Speech synthesis is temporarily unavailable")
#                 return
            
#             self.engine = trans.Translator()
            
#         except Exception as e:
#             QMessageBox.critical(self, "Translation Error", str(e))
#             return
        
#         # Populate combo boxes
#         languages = list(trans.LANGUAGES.values())
#         for text in languages:  # Use 'text' instead of the language name key
#             self.comboBox_1.addItems(languages)
        
#     def Translate(self):
#         print('Translate')
#         try:
#             s = self.textEdit_1.toPlainText()
            
#             # Get selected from and to languages
#             if not hasattr(trans, 'Translator'):
#                 QMessageBox.critical(self, "Translation Error", "Speech synthesis is temporarily unavailable")
#                 return
            
#             languagePairs = [(self.comboBox_1.currentText(), 
#                              self.comboBox_2.currentText())]
            
#             for pair in languagePairs:
#                 fromLang, toLang = pair
                
#                 if not fromLang or not toLang:
#                     continue
                    
#                 try:
#                     translated = trans.Translator().translate(s, from_lang=fromLang,
#                                                              to_lang=toLang)
                    
#                     # Move speech synthesis outside
#                     self.textEdit_2.clear()
#                     self.textEdit_2.append(translated)
                    
#                     if 'translation missing' in str(translated):
#                         QMessageBox.information(self, "Translation Info", 
#                                              f'Translation: {fromLang} → {toLang}')
#                 except Exception as e:
#                     QMessageBox.information(self, "Translation Error",
#                                          f'Error translating text: {str(e)}')
#                     break
            
#             if 'translation missing' in self.textEdit_2.toPlainText():
#                 QMessageBox.information(self, "Translation Info", 
#                                      self.textEdit_2.toPlainText())
            
#         except Exception as e:
#             QMessageBox.critical(self, "Critical Error", str(e))

#     def OpenFile(self):
#         pass  # Simplified version without actual file handling

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()