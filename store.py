from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QGridLayout

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
        
        # Se reemplaza el QLabel de texto simple por un QGridLayout para organizar las portadas
        self.games_layout = QGridLayout()
        
        # Lista con los nombres y los archivos de imagen exactos que subiste
        self.games_data = [
            ("1. Cyberpunk 2077", "cyberpunk2077.jpg"),
            ("2. The Witcher 3", "thewitcher.webp"),
            ("3. Red Dead Redemption 2", "reddead2.jpg"),
            ("4. Elden Ring", "eldenring.jpg"),
            ("5. Grand Theft Auto V", "gta5.jpg"),
            ("6. Baldur's Gate 3", "baldurs.jpg"),
            ("7. Stardew Valley", "stardewvalley.png"),
            ("8. Hollow Knight", "hollow.webp")
        ]

        # Generar las portadas y los textos dinámicamente
        row = 0
        col = 0
        for name, img_path in self.games_data:
            # Etiqueta para la imagen
            img_label = QLabel()
            pixmap = QPixmap(img_path)
            
            # Escalar la imagen para que todas tengan el mismo tamaño (puedes ajustar estos números)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(150, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                img_label.setPixmap(pixmap)
            else:
                img_label.setText("[Imagen no encontrada]")
            
            img_label.setAlignment(Qt.AlignCenter)

            # Etiqueta para el título del juego
            text_label = QLabel(name)
            text_label.setAlignment(Qt.AlignCenter)

            # Unir la imagen y el texto en un pequeño layout vertical
            game_vbox = QVBoxLayout()
            game_vbox.addWidget(img_label)
            game_vbox.addWidget(text_label)

            # Añadir ese juego a la cuadrícula principal (4 juegos por fila)
            self.games_layout.addLayout(game_vbox, row, col)
            col += 1
            if col > 3:  # Al llegar a 4 columnas, salta a la siguiente fila
                col = 0
                row += 1

        # --- Botones de Navegación ---
        self.nav_layout = QHBoxLayout()
        self.btn_nav_lib = QPushButton('Ir a Biblioteca')
        self.btn_nav_sup = QPushButton('Ayuda al Cliente')
        self.btn_nav_lib.clicked.connect(self.go_library.emit)
        self.btn_nav_sup.clicked.connect(self.go_support.emit)
        self.nav_layout.addWidget(self.btn_nav_lib)
        self.nav_layout.addWidget(self.btn_nav_sup)

        # Ensamblar el layout principal
        self.main_layout.addWidget(self.lbl_title)
        self.main_layout.addLayout(self.games_layout) # Agregamos la cuadrícula de imágenes aquí
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