from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
import random
from log_in import iniciar_sesion, registrar_usuarios

class LoginWindow(QWidget):
    login_successful = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es' 
        self.setup_ui()
        self.generate_captcha()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()
        
        # --- Botón de Idioma ---
        self.top_layout = QHBoxLayout()
        self.top_layout.addStretch() 
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.top_layout.addWidget(self.btn_lang)
        self.main_layout.addLayout(self.top_layout)

        # --- Formulario de Login ---
        self.lbl_title = QLabel('Iniciar Sesión')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        # Título más grande y en negrita
        self.lbl_title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 15px;")
        
        self.lbl_user = QLabel('Usuario:')
        self.input_user = QLineEdit()
        
        self.lbl_pass = QLabel('Contraseña:')
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        
        # Captcha
        self.lbl_captcha_q = QLabel('Captcha: ¿Cuánto es X + Y?')
        self.input_captcha = QLineEdit()
        
        # Botones de Acción
        self.buttons_layout = QHBoxLayout()
        self.btn_login = QPushButton('Entrar')
        self.btn_register = QPushButton('Registrar')
        
        self.btn_login.clicked.connect(self.check_login)
        self.btn_register.clicked.connect(self.handle_register)
        
        self.buttons_layout.addWidget(self.btn_login)
        self.buttons_layout.addWidget(self.btn_register)

        # Añadir al layout principal
        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_user)
        self.main_layout.addWidget(self.input_user)
        self.main_layout.addWidget(self.lbl_pass)
        self.main_layout.addWidget(self.input_pass)
        self.main_layout.addWidget(self.lbl_captcha_q)
        self.main_layout.addWidget(self.input_captcha)
        self.main_layout.addLayout(self.buttons_layout)
        
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
            self.btn_register.setText('Register')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.lbl_title.setText('Iniciar Sesión')
            self.lbl_user.setText('Usuario:')
            self.lbl_pass.setText('Contraseña:')
            self.btn_login.setText('Entrar')
            self.btn_register.setText('Registrar')
        self.generate_captcha()

    def check_login(self):
        usuario = self.input_user.text()
        contrasena = self.input_pass.text()

        if self.input_captcha.text() != self.correct_answer:
            msg = 'Captcha incorrecto' if self.lang == 'es' else 'Incorrect Captcha'
            QMessageBox.warning(self, 'Error', msg)
            self.generate_captcha()
            return

        if iniciar_sesion(usuario, contrasena):
            self.login_successful.emit()
        else:
            msg = 'Usuario o contraseña incorrectos, o campos vacíos.' if self.lang == 'es' else 'Invalid username/password or empty fields.'
            QMessageBox.warning(self, 'Error', msg)
            self.generate_captcha()

    def handle_register(self):
        usuario = self.input_user.text()
        contrasena = self.input_pass.text()

        if self.input_captcha.text() != self.correct_answer:
            msg = 'Captcha incorrecto' if self.lang == 'es' else 'Incorrect Captcha'
            QMessageBox.warning(self, 'Error', msg)
            self.generate_captcha()
            return

        if registrar_usuarios(usuario, contrasena):
            msg = f'Usuario "{usuario}" registrado correctamente.' if self.lang == 'es' else f'User "{usuario}" registered successfully.'
            QMessageBox.information(self, 'Éxito' if self.lang == 'es' else 'Success', msg)
            self.input_user.clear()
            self.input_pass.clear()
            self.input_captcha.clear()
        else:
            msg = 'Error: Los campos no pueden estar vacíos.' if self.lang == 'es' else 'Error: Fields cannot be empty.'
            QMessageBox.warning(self, 'Error', msg)
        
        self.generate_captcha()