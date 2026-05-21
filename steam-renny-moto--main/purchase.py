import os
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMessageBox

class PurchaseWindow(QWidget):
    go_store = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es'
        self.current_game = None
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()

        # Header - Language
        self.lang_layout = QHBoxLayout()
        self.lang_layout.addStretch()
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.lang_layout.addWidget(self.btn_lang)
        self.main_layout.addLayout(self.lang_layout)

        # Title
        self.lbl_title = QLabel('--- COMPRAR JUEGO ---')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 20px;")
        self.main_layout.addWidget(self.lbl_title)

        # Game Info (Image + Title)
        self.img_label = QLabel()
        self.img_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.img_label)

        self.lbl_game_title = QLabel('Nombre del Juego')
        self.lbl_game_title.setAlignment(Qt.AlignCenter)
        self.lbl_game_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.main_layout.addWidget(self.lbl_game_title)

        self.lbl_price = QLabel('Precio: $59.99')
        self.lbl_price.setAlignment(Qt.AlignCenter)
        self.lbl_price.setStyleSheet("font-size: 18px; color: #66c0f4; margin-bottom: 20px;")
        self.main_layout.addWidget(self.lbl_price)

        # Action Buttons
        self.buttons_layout = QHBoxLayout()
        self.btn_buy = QPushButton('Confirmar Compra')
        self.btn_buy.clicked.connect(self.handle_purchase)
        
        self.btn_cancel = QPushButton('Cancelar')
        self.btn_cancel.clicked.connect(self.go_store.emit)

        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.btn_buy)
        self.buttons_layout.addWidget(self.btn_cancel)
        self.buttons_layout.addStretch()
        self.main_layout.addLayout(self.buttons_layout)

        self.main_layout.addStretch()
        self.setLayout(self.main_layout)

    def load_game(self, game_data):
        self.current_game = game_data
        self.lbl_game_title.setText(game_data["title"])
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(base_dir, game_data["img"])
        pixmap = QPixmap(img_path)
        
        if not pixmap.isNull():
            pixmap = pixmap.scaled(200, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.img_label.setPixmap(pixmap)
        else:
            self.img_label.setText("[Imagen no encontrada]")
            
    def handle_purchase(self):
        msg = f'¡Felicidades! Has comprado {self.current_game["title"]} con éxito.' if self.lang == 'es' else f'Congratulations! You successfully bought {self.current_game["title"]}.'
        QMessageBox.information(self, 'Éxito' if self.lang == 'es' else 'Success', msg)
        self.go_store.emit()

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.lbl_title.setText('--- BUY GAME ---')
            self.lbl_price.setText('Price: $59.99')
            self.btn_buy.setText('Confirm Purchase')
            self.btn_cancel.setText('Cancel')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.lbl_title.setText('--- COMPRAR JUEGO ---')
            self.lbl_price.setText('Precio: $59.99')
            self.btn_buy.setText('Confirmar Compra')
            self.btn_cancel.setText('Cancelar')