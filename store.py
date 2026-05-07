from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class StoreWindow(QWidget):
    go_library = pyqtSignal()
    go_support = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.lang = 'es'
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()

        # --- Header: Idioma y Buscador (Arriba a la derecha) ---
        self.header_layout = QVBoxLayout()
        
        # Botón de idioma
        self.lang_layout = QHBoxLayout()
        self.lang_layout.addStretch()
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        self.lang_layout.addWidget(self.btn_lang)
        
        # Buscador
        self.search_layout = QHBoxLayout()
        self.search_layout.addStretch()
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText('Buscar juegos...')
        self.btn_search = QPushButton('Buscar')
        self.search_layout.addWidget(self.input_search)
        self.search_layout.addWidget(self.btn_search)

        self.header_layout.addLayout(self.lang_layout)
        self.header_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.header_layout)

        # --- Contenido de la Tienda ---
        self.lbl_title = QLabel('--- TIENDA DE JUEGOS ---')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        
        self.lbl_games = QLabel('1. Cyberpunk 2077\n2. The Witcher 3\n3. Red Dead Redemption 2')
        self.lbl_games.setAlignment(Qt.AlignCenter)

        # --- Botones de Navegación ---
        self.nav_layout = QHBoxLayout()
        self.btn_nav_lib = QPushButton('Ir a Biblioteca')
        self.btn_nav_sup = QPushButton('Ayuda al Cliente')
        self.btn_nav_lib.clicked.connect(self.go_library.emit)
        self.btn_nav_sup.clicked.connect(self.go_support.emit)
        self.nav_layout.addWidget(self.btn_nav_lib)
        self.nav_layout.addWidget(self.btn_nav_sup)

        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addWidget(self.lbl_games)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.nav_layout)
        self.setLayout(self.main_layout)

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.input_search.setPlaceholderText('Search games...')
            self.btn_search.setText('Search')
            self.lbl_title.setText('--- GAME STORE ---')
            self.btn_nav_lib.setText('Go to Library')
            self.btn_nav_sup.setText('Customer Support')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.input_search.setPlaceholderText('Buscar juegos...')
            self.btn_search.setText('Buscar')
            self.lbl_title.setText('--- TIENDA DE JUEGOS ---')
            self.btn_nav_lib.setText('Ir a Biblioteca')
            self.btn_nav_sup.setText('Ayuda al Cliente')