
import sys
import speech_recognition as sr
import pyttsx3
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QSizePolicy
from PyQt6.QtGui import QMovie, QPalette, QColor
from PyQt6.QtCore import QThread, pyqtSignal, Qt  # Import Qt here

class VoiceRecognitionThread(QThread):
    result = pyqtSignal(str)
    error = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            while True:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

                try:
                    command = recognizer.recognize_google(audio)
                    print("You said:", command)
                    self.result.emit(command)
                except sr.UnknownValueError:
                    self.error.emit("Sorry, I did not understand that.")
                except sr.RequestError as e:
                    self.error.emit(f"Could not request results; {e}")

class VoiceAssistant(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.start_listening()

    def initUI(self):
        self.setWindowTitle('Voice Assistant')
        self.setFixedSize(800, 600)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0,8,39,255))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
        palette.setColor(QPalette.ColorRole.Text, QColor(255, 255, 255))
        self.setPalette(palette)

        self.layout = QVBoxLayout()

        # Voice Bob setup
        self.voice_bob = QLabel(self)
        self.movie = QMovie("jarvis-bob-unscreen.gif")  # Ensure this is the correct path to your GIF
        self.voice_bob.setMovie(self.movie)
        self.movie.start()  # Start the animation immediately

        # Set size policy and fixed width
        self.voice_bob.setFixedWidth(400)  # Adjust width as needed
        self.voice_bob.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.voice_bob.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the image
        self.layout.addWidget(self.voice_bob, alignment=Qt.AlignmentFlag.AlignCenter)

        self.history_label = QLabel('Conversation History:')
        self.layout.addWidget(self.history_label)

        self.history_text = QTextEdit()
        self.history_text.setReadOnly(True)
        self.layout.addWidget(self.history_text)

        self.response_label = QLabel('Assistant Response:')
        self.layout.addWidget(self.response_label)

        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        self.layout.addWidget(self.response_text)

        self.setLayout(self.layout)

    def start_listening(self):
        self.history_text.append("Listening...")

        self.recognition_thread = VoiceRecognitionThread()
        self.recognition_thread.result.connect(self.handle_result)
        self.recognition_thread.error.connect(self.handle_error)
        self.recognition_thread.start()

    def handle_result(self, command):
        self.history_text.append(f"You said: {command}")
        self.respond(command)

    def handle_error(self, error_message):
        self.history_text.append(error_message)

    def respond(self, command):
        response = f"You said: {command}"
        self.history_text.append(response)

        engine = pyttsx3.init()
        engine.say(response)
        engine.runAndWait()

        self.response_text.setPlainText(response)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    assistant = VoiceAssistant()
    assistant.show()
    sys.exit(app.exec())

