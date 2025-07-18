'''
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is a text to speech example.")
engine.runAndWait()

need a Translator_speech.ui and add two buttons


added pip install pyobjc


'''

# from PyQt5.QtCore import QTimer
# from PyQt5.QtCore import QThread, pyqtSignal

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QComboBox, QMessageBox
# import sys
# from PyQt5 import uic
# import googletrans
# from googletrans import Translator
# import pyttsx3

# class SpeechThread(QThread):
#     def __init__(self, text, engine):
#         super().__init__()
#         self.text = text
#         self.engine = engine

#     def run(self):
#         self.engine.stop()  # Prevent overlapping
#         self.engine.say(self.text)
#         self.engine.runAndWait()



# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator_speech.ui', self)

#         # Init TTS engine
#         self.engine = pyttsx3.init()

#         # UI Elements
#         self.textEdit_1 = self.findChild(QTextEdit, 'textEdit_1')
#         self.textEdit_2 = self.findChild(QTextEdit, 'textEdit_2')
#         self.comboBox_1 = self.findChild(QComboBox, 'comboBox_1')
#         self.comboBox_2 = self.findChild(QComboBox, 'comboBox_2')
#         self.translate = self.findChild(QPushButton, 'translate')
#         self.Close = self.findChild(QPushButton, 'close')
#         self.speakOriginal = self.findChild(QPushButton, 'pushButton')  # Added to UI
#         self.speakTranslated = self.findChild(QPushButton, 'pushButton_2')  # Added to UI
        
#         # Populate languages
#         self.languages = googletrans.LANGUAGES
#         self.languages_list = list(self.languages.values())
#         self.comboBox_1.addItems(self.languages_list)
#         self.comboBox_2.addItems(self.languages_list)
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')

#         # Connect buttons
#         self.translate.clicked.connect(lambda: self.Translate(self))
#         self.Close.clicked.connect(self.clear)
#         self.speakOriginal.clicked.connect(lambda: self.speak(self.textEdit_1.toPlainText()))
#         self.speakTranslated.clicked.connect(lambda: self.speak(self.textEdit_2.toPlainText()))
#         # self.speakOriginal.clicked.connect(lambda text=self.textEdit_1.toPlainText(): self.speak(text))
#         # self.speakTranslated.clicked.connect(lambda: self.speak(self.textEdit_2.toPlainText()))

#     # from PyQt5.QtCore import QTimer

#     def speak(self, text):
#         if text.strip():
#             print(f"Speaking: {text}")
#             self.thread = SpeechThread(text, self.engine)
#             self.thread.start()
#         else:
#             print("No text to speak.")

    
    
    
#     # def speak(self, text):
#     #     if text.strip():
#     #         print(f"Speaking: {text}")
#     #         self.engine.say(text)
            
#     #         # Let Qt finish button event, then run speech
#     #         QTimer.singleShot(100, self.engine.runAndWait)
#     #     else:
#     #         print("No text to speak.")

#     # def speak(self, text):
#     #     if text.strip():
#     #         print(f"Speaking: {text}")  # debug feedback
#     #         self.engine.say(text)
#     #         self.engine.runAndWait()
#     #     else:
#     #         print("No text to speak.")  # debug feedback

#     def Translate(self, s):
#         print('translate')
#         s.translate.setStyleSheet('color:red;')
#         try:
#             from_language_key = to_language_key = None
#             for key, value in self.languages.items():
#                 if value == self.comboBox_1.currentText():
#                     from_language_key = key
#                 if value == self.comboBox_2.currentText():
#                     to_language_key = key

#             if not from_language_key or not to_language_key:
#                 raise Exception("Could not determine language keys.")

#             translator = Translator()
#             text = self.textEdit_1.toPlainText()
#             if text:
#                 translated = translator.translate(text, src=from_language_key, dest=to_language_key)
#                 self.textEdit_2.setText(translated.text)
#                 print("Original:", text)
#                 print("Translated:", translated.text)
#                 # Speak both
#                 self.speak(text)
#                 self.speak(translated.text)

#         except Exception as e:
#             QMessageBox.about(self, 'Translator', str(e))

#     def clear(self):
#         print('clear')
#         self.textEdit_1.clear()
#         self.textEdit_2.clear()
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())



# ## my original attempt
# # /Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_38_Translator/Translator_speech.py
# from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QTextEdit,QComboBox,QMessageBox
# import sys
# from PyQt5 import uic
# import googletrans
# # import textblob
# from googletrans import Translator
# import pyttsx3
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow,self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator.ui',self)
#         engine = pyttsx3.init()
#         self.engine=engine
#         self.engine.say("Hello, this is a text to speech example.")
#         self.engine.runAndWait()
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
#             if text != None:
#                 self.engine.say(text)
#                 print(text)
#                 self.engine.runAndWait()
#             translated = translator.translate(text, src=from_language_key, dest=to_language_key)
#             # print(translated,'   ',translated.src,'   ',translated.extra_data)
#             # Output translated text
            
#             self.textEdit_2.setText(translated.text)
#             if translated.text!= None:
                
#                 self.engine.say(translated.text)
#                 print(translated.text)
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
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QPushButton,
#     QTextEdit, QComboBox, QMessageBox
# )
# from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5 import uic
# import googletrans
# from googletrans import Translator
# import pyttsx3


# # Worker thread for speech
# class SpeechThread(QThread):
#     def __init__(self, text, engine):
#         super().__init__()
#         self.text = text
#         self.engine = engine

#     def run(self):
#         self.engine.stop()  # cancel any ongoing speech
#         self.engine.say(self.text)
#         self.engine.runAndWait()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator_speech.ui', self)

#         # Init TTS engine
#         self.engine = pyttsx3.init()
#         self.speech_threads = []  # keep running threads alive

#         # UI Elements
#         self.textEdit_1 = self.findChild(QTextEdit, 'textEdit_1')
#         self.textEdit_2 = self.findChild(QTextEdit, 'textEdit_2')
#         self.comboBox_1 = self.findChild(QComboBox, 'comboBox_1')
#         self.comboBox_2 = self.findChild(QComboBox, 'comboBox_2')
#         self.translate = self.findChild(QPushButton, 'translate')
#         self.Close = self.findChild(QPushButton, 'close')
#         self.speakOriginal = self.findChild(QPushButton, 'pushButton')      # Speak Original
#         self.speakTranslated = self.findChild(QPushButton, 'pushButton_2')  # Speak Translation

#         # Language list
#         self.languages = googletrans.LANGUAGES
#         self.languages_list = list(self.languages.values())
#         self.comboBox_1.addItems(self.languages_list)
#         self.comboBox_2.addItems(self.languages_list)
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')

#         # Button connections
#         self.translate.clicked.connect(lambda: self.Translate(self))
#         self.Close.clicked.connect(self.clear)
#         self.speakOriginal.clicked.connect(
#             lambda: self.speak(self.textEdit_1.toPlainText()))
#         self.speakTranslated.clicked.connect(
#             lambda: self.speak(self.textEdit_2.toPlainText()))

#     def speak(self, text):
#         if text.strip():
#             print(f"Speaking: {text}")
#             thread = SpeechThread(text, self.engine)
#             thread.finished.connect(lambda: self.cleanup_thread(thread))
#             self.speech_threads.append(thread)
#             thread.start()
#         else:
#             print("No text to speak.")

#     def cleanup_thread(self, thread):
#         try:
#             self.speech_threads.remove(thread)
#         except ValueError:
#             pass

#     def Translate(self, s):
#         print('translate')
#         s.translate.setStyleSheet('color:red;')
#         try:
#             from_language_key = to_language_key = None
#             for key, value in self.languages.items():
#                 if value == self.comboBox_1.currentText():
#                     from_language_key = key
#                 if value == self.comboBox_2.currentText():
#                     to_language_key = key

#             if not from_language_key or not to_language_key:
#                 raise Exception("Could not determine language keys.")

#             translator = Translator()
#             text = self.textEdit_1.toPlainText()
#             if text:
#                 translated = translator.translate(text, src=from_language_key, dest=to_language_key)
#                 self.textEdit_2.setText(translated.text)
#                 print("Original:", text)
#                 print("Translated:", translated.text)
#                 self.speak(text)
#                 self.speak(translated.text)

#         except Exception as e:
#             QMessageBox.about(self, 'Translator', str(e))

#     def clear(self):
#         print('clear')
#         self.textEdit_1.clear()
#         self.textEdit_2.clear()
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

## !!this is the final working copy /Users/judsonbelmont/Documents/Shared_Folders/pyqt5_Codemy/Cod_38_Translator
import sys
import platform
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTextEdit, QComboBox, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import uic
import googletrans
from googletrans import Translator

# macOS native speech
if platform.system() == "Darwin":
    from AppKit import NSSpeechSynthesizer
else:
    import pyttsx3


# Worker thread for pyttsx3 (Windows/Linux)
class SpeechThread(QThread):
    def __init__(self, text, engine):
        super().__init__()
        self.text = text
        self.engine = engine

    def run(self):
        self.engine.stop()
        self.engine.say(self.text)
        self.engine.runAndWait()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Cod_38_Translator/Translator_speech.ui', self)

        # Set up speech engine based on platform
        self.is_mac = platform.system() == "Darwin"
        if self.is_mac:
            self.engine = NSSpeechSynthesizer.alloc().init()
            for voice in NSSpeechSynthesizer.availableVoices():
                print(voice)

        else:
            self.engine = pyttsx3.init()
            self.speech_threads = []
       
        self.language_to_voice = {
    "spanish": "com.apple.voice.compact.es-ES.Monica",
    "german": "com.apple.voice.compact.de-DE.Anna",
    # "french": "com.apple.voice.compact.fr-FR.Thomas",
    "french": "com.apple.eloquence.fr-FR.Grandma",
    "hebrew": "com.apple.speech.synthesis.voice.Carmit",
    "latin": "com.apple.voice.compact.it-IT.Luca",  # fallback to Italian
    "polish": "com.apple.voice.compact.pl-PL.Zosia",
    # 'english':'com.apple.eloquence.en-US.Rocko',
    'english':'com.apple.voice.compact.en-AU.Karen',
}

    


        # UI Elements
        self.textEdit_1 = self.findChild(QTextEdit, 'textEdit_1')
        self.textEdit_2 = self.findChild(QTextEdit, 'textEdit_2')
        self.comboBox_1 = self.findChild(QComboBox, 'comboBox_1')
        self.comboBox_2 = self.findChild(QComboBox, 'comboBox_2')
        self.translate = self.findChild(QPushButton, 'translate')
        self.Close = self.findChild(QPushButton, 'close')
        self.speakOriginal = self.findChild(QPushButton, 'pushButton')
        self.speakTranslated = self.findChild(QPushButton, 'pushButton_2')
 

        # Populate languages
        self.languages = googletrans.LANGUAGES
        self.languages_list = list(self.languages.values())
        self.comboBox_1.addItems(self.languages_list)
        self.comboBox_2.addItems(self.languages_list)
        self.comboBox_1.setCurrentText('english')
        self.comboBox_2.setCurrentText('spanish')

        # Connect buttons
        self.translate.clicked.connect(lambda: self.Translate(self))
        self.Close.clicked.connect(self.clear)
        # self.speakOriginal.clicked.connect(
        #     lambda: self.speak(self.textEdit_1.toPlainText()))
        # self.speakTranslated.clicked.connect(
        #     lambda: self.speak(self.textEdit_2.toPlainText())) ## need to reset the 'lang' see below

        self.speakOriginal.clicked.connect(
            lambda: self.speak(self.textEdit_1.toPlainText(), lang=self.comboBox_1.currentText())
        )
        self.speakTranslated.clicked.connect(
            lambda: self.speak(self.textEdit_2.toPlainText(), lang=self.comboBox_2.currentText())
        )

        
        
    def speak(self, text, lang=None):
        if text.strip():
            print(f"Speaking: {text}")
            if self.is_mac:
                self.engine.stopSpeaking()

                # Set language-specific voice if available
                if lang:
                    voice_id = self.language_to_voice.get(lang.lower())
                    if voice_id:
                        self.engine.setVoice_(voice_id)
                        print(f"Set macOS voice to: {voice_id}")

                self.engine.startSpeakingString_(text)
            else:
                thread = SpeechThread(text, self.engine)
                thread.finished.connect(lambda: self.cleanup_thread(thread))
                self.speech_threads.append(thread)
                thread.start()
        else:
            print("No text to speak.")

    
    
    # def speak(self, text):
    #     if text.strip():
    #         print(f"Speaking: {text}")
    #         if self.is_mac:
    #             self.engine.stopSpeaking()
    #             self.engine.startSpeakingString_(text)
    #         else:
    #             thread = SpeechThread(text, self.engine)
    #             thread.finished.connect(lambda: self.cleanup_thread(thread))
    #             self.speech_threads.append(thread)
    #             thread.start()
    #     else:
    #         print("No text to speak.")

    def cleanup_thread(self, thread):
        try:
            self.speech_threads.remove(thread)
        except ValueError:
            pass

    def Translate(self, s):
        print('translate')
        s.translate.setStyleSheet('color:red;')
        try:
            from_language_key = to_language_key = None
            for key, value in self.languages.items():
                if value == self.comboBox_1.currentText():
                    from_language_key = key
                if value == self.comboBox_2.currentText():
                    to_language_key = key

            if not from_language_key or not to_language_key:
                raise Exception("Could not determine language keys.")

            translator = Translator()
            text = self.textEdit_1.toPlainText()
            if text:
                translated = translator.translate(text, src=from_language_key, dest=to_language_key)
                self.textEdit_2.setText(translated.text)
                print("Original:", text)
                print("Translated:", translated.text)
                # self.speak(text)
                # self.speak(translated.text)
                self.speak(text, lang=self.comboBox_1.currentText())
                self.speak(translated.text, lang=self.comboBox_2.currentText())

        except Exception as e:
            QMessageBox.about(self, 'Translator', str(e))

    def clear(self):
        print('clear')
        self.textEdit_1.clear()
        self.textEdit_2.clear()
        self.comboBox_1.setCurrentText('english')
        self.comboBox_2.setCurrentText('spanish')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# import sys        ## great working version without autoselect of voices
# import platform
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QPushButton,
#     QTextEdit, QComboBox, QMessageBox
# )
# from PyQt5.QtCore import QThread, pyqtSignal
# from PyQt5 import uic
# import googletrans
# from googletrans import Translator

# # macOS native speech
# if platform.system() == "Darwin":
#     from AppKit import NSSpeechSynthesizer
# else:
#     import pyttsx3


# # Worker thread for pyttsx3 (Windows/Linux)
# class SpeechThread(QThread):
#     def __init__(self, text, engine):
#         super().__init__()
#         self.text = text
#         self.engine = engine

#     def run(self):
#         self.engine.stop()
#         self.engine.say(self.text)
#         self.engine.runAndWait()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         uic.loadUi('Cod_38_Translator/Translator_speech.ui', self)

#         # Set up speech engine based on platform
#         self.is_mac = platform.system() == "Darwin"
#         if self.is_mac:
#             self.engine = NSSpeechSynthesizer.alloc().init()
#         else:
#             self.engine = pyttsx3.init()
#             self.speech_threads = []

#         # UI Elements
#         self.textEdit_1 = self.findChild(QTextEdit, 'textEdit_1')
#         self.textEdit_2 = self.findChild(QTextEdit, 'textEdit_2')
#         self.comboBox_1 = self.findChild(QComboBox, 'comboBox_1')
#         self.comboBox_2 = self.findChild(QComboBox, 'comboBox_2')
#         self.translate = self.findChild(QPushButton, 'translate')
#         self.Close = self.findChild(QPushButton, 'close')
#         self.speakOriginal = self.findChild(QPushButton, 'pushButton')
#         self.speakTranslated = self.findChild(QPushButton, 'pushButton_2')

#         # Populate languages
#         self.languages = googletrans.LANGUAGES
#         self.languages_list = list(self.languages.values())
#         self.comboBox_1.addItems(self.languages_list)
#         self.comboBox_2.addItems(self.languages_list)
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')

#         # Connect buttons
#         self.translate.clicked.connect(lambda: self.Translate(self))
#         self.Close.clicked.connect(self.clear)
#         self.speakOriginal.clicked.connect(
#             lambda: self.speak(self.textEdit_1.toPlainText()))
#         self.speakTranslated.clicked.connect(
#             lambda: self.speak(self.textEdit_2.toPlainText()))

#     def speak(self, text):
#         if text.strip():
#             print(f"Speaking: {text}")
#             if self.is_mac:
#                 self.engine.stopSpeaking()
#                 self.engine.startSpeakingString_(text)
#             else:
#                 thread = SpeechThread(text, self.engine)
#                 thread.finished.connect(lambda: self.cleanup_thread(thread))
#                 self.speech_threads.append(thread)
#                 thread.start()
#         else:
#             print("No text to speak.")

#     def cleanup_thread(self, thread):
#         try:
#             self.speech_threads.remove(thread)
#         except ValueError:
#             pass

#     def Translate(self, s):
#         print('translate')
#         s.translate.setStyleSheet('color:red;')
#         try:
#             from_language_key = to_language_key = None
#             for key, value in self.languages.items():
#                 if value == self.comboBox_1.currentText():
#                     from_language_key = key
#                 if value == self.comboBox_2.currentText():
#                     to_language_key = key

#             if not from_language_key or not to_language_key:
#                 raise Exception("Could not determine language keys.")

#             translator = Translator()
#             text = self.textEdit_1.toPlainText()
#             if text:
#                 translated = translator.translate(text, src=from_language_key, dest=to_language_key)
#                 self.textEdit_2.setText(translated.text)
#                 print("Original:", text)
#                 print("Translated:", translated.text)
#                 self.speak(text)
#                 self.speak(translated.text)

#         except Exception as e:
#             QMessageBox.about(self, 'Translator', str(e))

#     def clear(self):
#         print('clear')
#         self.textEdit_1.clear()
#         self.textEdit_2.clear()
#         self.comboBox_1.setCurrentText('english')
#         self.comboBox_2.setCurrentText('spanish')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
