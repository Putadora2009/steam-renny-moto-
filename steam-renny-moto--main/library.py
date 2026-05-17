from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
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
        # Título más grande y destacado
        self.lbl_title.setStyleSheet("font-size: 22px; font-weight: bold; margin-top: 10px; margin-bottom: 20px;")
        self.main_layout.addWidget(self.lbl_title)

        # Layout horizontal para los juegos adquiridos
        self.games_layout = QHBoxLayout()
        
        self.library_games = [
            {"title_es": "Red Dead Redemption 2\n(Instalado)", "title_en": "Red Dead Redemption 2\n(Installed)", "img": "reddead2.jpg"},
            {"title_es": "Grand Theft Auto V\n(Instalado)", "title_en": "Grand Theft Auto V\n(Installed)", "img": "gta5.jpg"}
        ]
        
        self.game_widgets = [] 

        for game in self.library_games:
            game_vbox = QVBoxLayout()
            
            # Label de imagen
            img_label = QLabel()
            pixmap = QPixmap(game["img"])
            if not pixmap.isNull():
                pixmap = pixmap.scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label.setPixmap(pixmap)
            else:
                img_label.setText("[Imagen no encontrada]")
            img_label.setAlignment(Qt.AlignCenter)
            
            # Label de texto descriptivo (Nombre del juego más grande y en negrita)
            text_label = QLabel(game["title_es"] if self.lang == 'es' else game["title_en"])
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 8px;")
            
            game_vbox.addWidget(img_label)
            game_vbox.addWidget(text_label)
            self.games_layout.addLayout(game_vbox)
            
            self.game_widgets.append((text_label, game))

        self.main_layout.addLayout(self.games_layout)

        # Botón volver
        self.btn_back = QPushButton('Volver a la Tienda')
        self.btn_back.clicked.connect(self.go_store.emit)

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
            self.btn_back.setText('Back to Store')
            for label, data in self.game_widgets:
                label.setText(data["title_en"])
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.input_search.setPlaceholderText('Buscar en tu biblioteca...')
            self.btn_search.setText('Buscar')
            self.lbl_title.setText('--- MI BIBLIOTECA ---')
            self.btn_back.setText('Volver a la Tienda')
            for label, data in self.game_widgets:
                label.setText(data["title_es"])