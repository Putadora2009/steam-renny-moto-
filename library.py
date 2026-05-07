from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class LibraryWindow(QWidget):
    go_store = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es'
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()

        # --- Header: Idioma y Buscador ---
        self.header_layout = QVBoxLayout()
        
        self.lang_layout = QHBoxLayout()
        self.lang_layout.addStretch()
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.lang_layout.addWidget(self.btn_lang)
        
        self.search_layout = QHBoxLayout()
        self.search_layout.addStretch()
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText('Buscar en tu biblioteca...')
        self.btn_search = QPushButton('Buscar')
        self.search_layout.addWidget(self.input_search)
        self.search_layout.addWidget(self.btn_search)

        self.header_layout.addLayout(self.lang_layout)
        self.header_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.header_layout)

        # --- Contenido de la Biblioteca ---
        self.lbl_title = QLabel('--- MI BIBLIOTECA ---')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        
        self.lbl_games = QLabel('- Terraria (Instalado)\n- Stardew Valley (No Instalado)')
        self.lbl_games.setAlignment(Qt.AlignCenter)

        # Botón volver
        self.btn_back = QPushButton('Volver a la Tienda')
        self.btn_back.clicked.connect(self.go_store.emit)

        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_games)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.btn_back, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.input_search.setPlaceholderText('Search in your library...')
            self.btn_search.setText('Search')
            self.lbl_title.setText('--- MY LIBRARY ---')
            self.lbl_games.setText('- Terraria (Installed)\n- Stardew Valley (Not Installed)')
            self.btn_back.setText('Back to Store')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.input_search.setPlaceholderText('Buscar en tu biblioteca...')
            self.btn_search.setText('Buscar')
            self.lbl_title.setText('--- MI BIBLIOTECA ---')
            self.lbl_games.setText('- Terraria (Instalado)\n- Stardew Valley (No Instalado)')
            self.btn_back.setText('Volver a la Tienda')