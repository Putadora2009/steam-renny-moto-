import os
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QGridLayout

# --- AÑADIDO PARA HACER LAS IMÁGENES CLICKEABLES ---
class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)
# ---------------------------------------------------

class StoreWindow(QWidget):
    go_library = pyqtSignal()
    go_support = pyqtSignal()
    logout_successful = pyqtSignal() # Señal para cerrar sesión
    
    # CAMBIADO A "object" PARA MAYOR COMPATIBILIDAD (Acepta diccionarios sin problema en cualquier versión de PyQt5)
    go_purchase = pyqtSignal(object) 

    def __init__(self):
        super().__init__()
        self.lang = 'es'
        self.setup_ui()

    def setup_ui(self):
        self.main_layout = QVBoxLayout()

        # --- Header: Cerrar sesión, Idioma y Buscador ---
        self.header_layout = QVBoxLayout()
        
        # 3. Layout superior para Cerrar Sesión e Idioma
        self.top_bar_layout = QHBoxLayout()
        
        # Botón de Cerrar Sesión 
        self.btn_logout = QPushButton('Cerrar Sesión')
        self.btn_logout.clicked.connect(self.logout_successful.emit)
        
        # Botón de Idioma 
        self.btn_lang = QPushButton('Change to English')
        self.btn_lang.clicked.connect(self.toggle_language)
        
        self.top_bar_layout.addWidget(self.btn_logout)
        self.top_bar_layout.addStretch() # Empuja el botón de idioma a la derecha
        self.top_bar_layout.addWidget(self.btn_lang)
        
        self.search_layout = QHBoxLayout()
        self.search_layout.addStretch()
        self.input_search = QLineEdit()
        self.input_search.setPlaceholderText('Buscar juegos...')
        self.btn_search = QPushButton('Buscar')
        self.search_layout.addWidget(self.input_search)
        self.search_layout.addWidget(self.btn_search)

        self.header_layout.addLayout(self.top_bar_layout)
        self.header_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.header_layout)

        # --- Contenido de la Tienda ---
        self.lbl_title = QLabel('--- TIENDA DE JUEGOS ---')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setStyleSheet("font-size: 22px; font-weight: bold; margin-top: 10px; margin-bottom: 20px;")

        # Cuadrícula de juegos
        self.games_layout = QGridLayout()
        
        self.games_data = [
            {"title": "Cyberpunk 2077", "img": "cyberpunk2077.jpg"},
            {"title": "Elden Ring", "img": "eldenring.jpg"},
            {"title": "The Witcher 3", "img": "thewitcher.webp"},
            {"title": "GTA 5", "img": "gta5.jpg"},
            {"title": "Red Dead Redemption 2", "img": "reddead2.jpg"},
            {"title": "Baldurs Gate 3", "img": "baldurs.jpg"},
            {"title": "Hollow Night", "img": "hollow.webp"},
            {"title": "Batman Arkham", "img": "batman.jpg"}, 
            {"title": "Bully", "img": "bully.jpg"}           
        ]

        # Obtener el directorio absoluto donde se encuentra este script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        for i, game in enumerate(self.games_data):
            game_vbox = QVBoxLayout()
            
            # CLAVE: Nos aseguramos de usar la nueva clase ClickableLabel y no el QLabel normal
            img_label = ClickableLabel() 
            
            # Usamos *args en el lambda para absorber de forma segura cualquier argumento por defecto que PyQt envíe
            img_label.clicked.connect(lambda *args, g=game: self.go_purchase.emit(g))
            
            # 2. Generar ruta absoluta para la imagen
            img_path = os.path.join(base_dir, game["img"])
            pixmap = QPixmap(img_path)
            
            if not pixmap.isNull():
                pixmap = pixmap.scaled(120, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label.setPixmap(pixmap)
            else:
                img_label.setText("[Imagen]")
                
            img_label.setAlignment(Qt.AlignCenter)
            img_label.setCursor(Qt.PointingHandCursor) 
            
            text_label = QLabel(game["title"])
            text_label.setAlignment(Qt.AlignCenter)
            text_label.setStyleSheet("font-size: 15px; font-weight: bold;")
            
            game_vbox.addWidget(img_label)
            game_vbox.addWidget(text_label)
            
            row = i // 2
            col = i % 2
            self.games_layout.addLayout(game_vbox, row, col)

        # Barra de Navegación Inferior
        self.nav_layout = QHBoxLayout()
        self.btn_nav_lib = QPushButton('Ir a Biblioteca')
        self.btn_nav_sup = QPushButton('Ayuda al Cliente')
        self.btn_nav_lib.clicked.connect(self.go_library.emit)
        self.btn_nav_sup.clicked.connect(self.go_support.emit)
        self.nav_layout.addWidget(self.btn_nav_lib)
        self.nav_layout.addWidget(self.btn_nav_sup)

        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addLayout(self.games_layout)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.nav_layout)
        self.setLayout(self.main_layout)

    def toggle_language(self):
        if self.lang == 'es':
            self.lang = 'en'
            self.btn_lang.setText('Cambiar a Español')
            self.btn_logout.setText('Log Out') 
            self.input_search.setPlaceholderText('Search games...')
            self.btn_search.setText('Search')
            self.lbl_title.setText('--- GAME STORE ---')
            self.btn_nav_lib.setText('Go to Library')
            self.btn_nav_sup.setText('Customer Support')
        else:
            self.lang = 'es'
            self.btn_lang.setText('Change to English')
            self.btn_logout.setText('Cerrar Sesión')
            self.input_search.setPlaceholderText('Buscar juegos...')
            self.btn_search.setText('Buscar')
            self.lbl_title.setText('--- TIENDA DE JUEGOS ---')
            self.btn_nav_lib.setText('Ir a Biblioteca')
            self.btn_nav_sup.setText('Ayuda al Cliente')