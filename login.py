from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
import random

class LoginWindow(QWidget):
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es' # Idioma por defecto
        self.setup_ui()
        self.generate_captcha()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        
        # --- Botón de Idioma (Esquina superior derecha) ---
        self.top_layout = QHBoxLayout()
        self.top_layout.addStretch() # Empuja el botón a la derecha
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.top_layout.addWidget(self.btn_lang)
        self.main_layout.addLayout(self.top_layout)

        # --- Formulario de Login ---
        self.lbl_title = QLabel('Iniciar Sesión')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        
        self.lbl_user = QLabel('Usuario:')
        self.input_user = QLineEdit()
        
        self.lbl_pass = QLabel('Contraseña:')
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        
        # Captcha
        self.lbl_captcha_q = QLabel('Captcha: ¿Cuánto es X + Y?')
        self.input_captcha = QLineEdit()
        
        self.btn_login = QPushButton('Entrar')
        self.btn_login.clicked.connect(self.check_login)

        # Añadir al layout principal (centrado)
        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_user)
        self.main_layout.addWidget(self.input_user)
        self.main_layout.addWidget(self.lbl_pass)
        self.main_layout.addWidget(self.input_pass)
        self.main_layout.addWidget(self.lbl_captcha_q)
        self.main_layout.addWidget(self.input_captcha)
        self.main_layout.addWidget(self.btn_login, alignment=Qt.AlignCenter)
        
        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

    def generate_captcha(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.correct_answer = str(self.num1 + self.num2)
        if self.lang == 'es':
            self.lbl_captcha_q.setText(f'Captcha: ¿Cuánto es {self.num1} + {self.num2}?')
        else:
            self.lbl_captcha_q.setText(f'Captcha: How much is {self.num1} + {self.num2}?')

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.lbl_title.setText('Login')
            self.lbl_user.setText('User:')
            self.lbl_pass.setText('Password:')
            self.btn_login.setText('Enter')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.lbl_title.setText('Iniciar Sesión')
            self.lbl_user.setText('Usuario:')
            self.lbl_pass.setText('Contraseña:')
            self.btn_login.setText('Entrar')
        self.generate_captcha() # Actualizar texto del captcha

    def check_login(self):
        if self.input_captcha.text() == self.correct_answer:
            self.login_successful.emit()
        else:
            msg = 'Captcha incorrecto' if self.lang == 'es' else 'Incorrect Captcha'
            QMessageBox.warning(self, 'Error', msg)
            self.generate_captcha()