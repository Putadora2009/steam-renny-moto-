from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QRadioButton, QButtonGroup

class SupportWindow(QWidget):
    go_store = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es'
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()

        # --- Header: Solo Idioma ---
        self.lang_layout = QHBoxLayout()
        self.lang_layout.addStretch()
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.lang_layout.addWidget(self.btn_lang)
        self.main_layout.addLayout(self.lang_layout)

        # --- Contenido de Soporte ---
        self.lbl_title = QLabel('--- AYUDA AL CLIENTE ---')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        # Título más grande y destacado
        self.lbl_title.setStyleSheet("font-size: 22px; font-weight: bold; margin-top: 10px; margin-bottom: 20px;")
        
        self.lbl_problem = QLabel('Seleccione el tipo de problema:')
        
        self.radio_button_1 = QRadioButton('1. Problema de Compra')
        self.radio_button_1.setChecked(True)
        self.radio_button_2 = QRadioButton('2. Bug en un Juego')
        self.radio_button_3 = QRadioButton('3. Acceso a la Cuenta')
        
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1, 1)
        self.button_group.addButton(self.radio_button_2, 2)
        self.button_group.addButton(self.radio_button_3, 3)

        self.btn_send = QPushButton('Enviar Reporte')
        self.btn_send.clicked.connect(self.handle_send_click)
        
        self.lbl_status = QLabel('')
        self.lbl_status.setAlignment(Qt.AlignCenter)

        self.btn_back = QPushButton('Volver a la Tienda')
        self.btn_back.clicked.connect(self.go_store.emit)

        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_problem)
        self.main_layout.addWidget(self.radio_button_1)
        self.main_layout.addWidget(self.radio_button_2)
        self.main_layout.addWidget(self.radio_button_3)
        self.main_layout.addWidget(self.btn_send)
        self.main_layout.addWidget(self.lbl_status)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.btn_back, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

    def handle_send_click(self):
        selected_id = self.button_group.checkedId()
        if self.lang == 'es':
            self.lbl_status.setText("Enviado. Seleccionado: número de problema " + str(selected_id))
        else:
            self.lbl_status.setText("Sent. Selected: problem number " + str(selected_id))

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.lbl_title.setText('--- CUSTOMER SUPPORT ---')
            self.lbl_problem.setText('Select the type of problem:')
            self.radio_button_1.setText('1. Purchase Issue')
            self.radio_button_2.setText('2. In-game Bug')
            self.radio_button_3.setText('3. Account Recovery')
            self.btn_send.setText('Send Report')
            self.btn_back.setText('Back to Store')
            self.lbl_status.setText('')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.lbl_title.setText('--- AYUDA AL CLIENTE ---')
            self.lbl_problem.setText('Seleccione el tipo de problema:')
            self.radio_button_1.setText('1. Problema de Compra')
            self.radio_button_2.setText('2. Bug en un Juego')
            self.radio_button_3.setText('3. Acceso a la Cuenta')
            self.btn_send.setText('Enviar Reporte')
            self.btn_back.setText('Volver a la Tienda')
            self.lbl_status.setText('')