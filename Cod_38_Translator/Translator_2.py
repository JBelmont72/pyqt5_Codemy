'''


'''
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
from PyQt5.QtWidgets import QVBoxLayout, QWidget


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
    # 'english':'com.apple.eloquence.en-GB.Eddy',
    # 'english':'com.apple.speech.synthesis.voice.Hysterical',
    'english':'com.apple.voice.compact.en-AU.Karen',
}

        self.en_voices = {
    "Karen (AU)": "com.apple.voice.compact.en-AU.Karen",
    "Daniel (UK)": "com.apple.voice.compact.en-GB.Daniel",
    "Eddy UK": "com.apple.eloquence.en-GB.Eddy",
    "Flo UK": "com.apple.eloquence.en-GB.Flo",
    "Grandma UK": "com.apple.eloquence.en-GB.Grandma",
    "Grandpa UK": "com.apple.eloquence.en-GB.Grandpa",
    "Reed UK": "com.apple.eloquence.en-GB.Reed",
    "Rocko UK": "com.apple.eloquence.en-GB.Rocko",
    "Sandy UK": "com.apple.eloquence.en-GB.Sandy",
    "Shelley UK": "com.apple.eloquence.en-GB.Shelley",
    "Moira (IE)": "com.apple.voice.compact.en-IE.Moira",
    "Rishi (IN)": "com.apple.voice.compact.en-IN.Rishi",
    "Albert": "com.apple.speech.synthesis.voice.Albert",
    "Bad News": "com.apple.speech.synthesis.voice.BadNews",
    "Eddy US": "com.apple.eloquence.en-US.Eddy",
    "Flo US": "com.apple.eloquence.en-US.Flo",
    "Grandma US": "com.apple.eloquence.en-US.Grandma",
    "Grandpa US": "com.apple.eloquence.en-US.Grandpa",
    "Fred": "com.apple.speech.synthesis.voice.Fred",
    "Good News": "com.apple.speech.synthesis.voice.GoodNews",
    "Jester": "com.apple.speech.synthesis.voice.Hysterical",
    "Kathy": "com.apple.speech.synthesis.voice.Kathy",
    "Princess": "com.apple.speech.synthesis.voice.Princess",
    "Ralph": "com.apple.speech.synthesis.voice.Ralph",
    "Reed US": "com.apple.eloquence.en-US.Reed",
    "Rocko US": "com.apple.eloquence.en-US.Rocko",
    "Samantha": "com.apple.voice.compact.en-US.Samantha",
    "Sandy US": "com.apple.eloquence.en-US.Sandy",
    "Shelley US": "com.apple.eloquence.en-US.Shelley",
    "Tessa (ZA)": "com.apple.voice.compact.en-ZA.Tessa",
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
        # Add a combobox for English voices (for demonstration)
##############
#         # If using Qt Designer .ui, centralwidget is already present
#         self.comboBox_en_voice = QComboBox(self)
#         self.comboBox_en_voice.setObjectName("comboBox_en_voice")

#         # Populate with available English voices (macOS only)
#         if self.is_mac:
#             en_voices = [
#             v for v in NSSpeechSynthesizer.availableVoices()
#             if ".en-" in v or ".en_" in v or "english" in v.lower()
#             ]
#             self.comboBox_en_voice.addItems(en_voices)
#         else:
#             # For pyttsx3, list voices with 'en' in id or name
#             voices = self.engine.getProperty('voices')
#             en_voices = [v.id for v in voices if 'en' in v.id or 'English' in v.name]
#             self.comboBox_en_voice.addItems(en_voices)

#         # Add to layout if possible, else just show as a child widget
#         # If using Qt Designer, you may need to add it to a layout manually
#         self.comboBox_en_voice.move(10, 220)  # Adjust position as needed
#         self.comboBox_en_voice.resize(350, 30)
#         self.comboBox_en_voice.show()
# ####################### if use QT Designer
#         self.comboBox_en_voice = self.findChild(QComboBox, 'comboBox_en_voice')
#         self.comboBox_en_voice.addItems(self.en_voices.keys())
#         self.comboBox_en_voice.setCurrentText("Samantha")  # or your default

        ########
        self.comboBox_en_voice = QComboBox(self)
        self.comboBox_en_voice.setObjectName("comboBox_en_voice")
        self.comboBox_en_voice.move(10, 220)  # Adjust position as needed
        self.comboBox_en_voice.resize(350, 30)
        self.comboBox_en_voice.show()
        self.comboBox_en_voice.addItems(self.en_voices.keys())
        self.comboBox_en_voice.setCurrentText("Samantha")  # or your default


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

        
        
    # def speak(self, text, lang=None):   ## without the language combobox
    #     if text.strip():
    #         print(f"Speaking: {text}")
    #         if self.is_mac:
    #             self.engine.stopSpeaking()

    #             # Set language-specific voice if available
    #             if lang:
    #                 voice_id = self.language_to_voice.get(lang.lower())
    #                 if voice_id:
    #                     self.engine.setVoice_(voice_id)
    #                     print(f"Set macOS voice to: {voice_id}")

    #             self.engine.startSpeakingString_(text)
    #         else:
    #             thread = SpeechThread(text, self.engine)
    #             thread.finished.connect(lambda: self.cleanup_thread(thread))
    #             self.speech_threads.append(thread)
    #             thread.start()
    #     else:
    #         print("No text to speak.")
        
    def speak(self, text, lang=None):   ## with the language combobox
        if text.strip():
            print(f"Speaking: {text}")
            if self.is_mac:
                self.engine.stopSpeaking()

                # Set language-specific voice if available
                if lang:  ### the new language select
                    if lang.lower() == 'english':
                        selected_label = self.comboBox_en_voice.currentText()
                        voice_id = self.en_voices.get(selected_label)
                        if voice_id:
                            self.engine.setVoice_(voice_id)
                            print(f"🔊 Using selected English voice: {selected_label} → {voice_id}")
                    else:
                        voice_id = self.language_to_voice.get(lang.lower())
                        if voice_id:
                            self.engine.setVoice_(voice_id)
                            print(f"Set macOS voice to: {voice_id}")

                # if lang:      ## the old language select
                #     voice_id = self.language_to_voice.get(lang.lower())
                #     if voice_id:
                #         self.engine.setVoice_(voice_id)
                #         print(f"Set macOS voice to: {voice_id}")

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
