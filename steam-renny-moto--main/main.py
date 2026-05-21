import sys
import os
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5.QtGui import QFontDatabase, QFont
from login import LoginWindow
from store import StoreWindow
from library import LibraryWindow
from support import SupportWindow
from purchase import PurchaseWindow

class SteamCloneApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        # --- 1. CARGAR FUENTE EXTERNA (Roboto) ---
       
        fuente_path = "Roboto-VariableFont_wdth,wght.ttf" 
        if os.path.exists(fuente_path):
            QFontDatabase.addApplicationFont(fuente_path)
            self.app.setFont(QFont("Roboto", 11))
        else:
            print("Advertencia: No se encontró 'Roboto-Regular.ttf'. Se usará la fuente Roboto del sistema si está instalada.")
            self.app.setFont(QFont("Roboto", 11))

        # --- DISEÑO Y ESTILO GLOBAL (Actualizado a Roboto) ---
        self.app.setStyleSheet("""
            QWidget {
                background-color: #1b2838;
                color: #ffffff;
                font-family: 'Roboto', sans-serif;
            }
            QLabel {
                background-color: transparent;
                font-size: 15px;
            }
            QLineEdit {
                background-color: #2a475e;
                color: #ffffff;
                border: 1px solid #101822;
                border-radius: 3px;
                padding: 5px;
                font-size: 14px;
                font-family: 'Roboto', sans-serif;
            }
            QLineEdit:focus {
                border: 1px solid #66c0f4;
            }
            QPushButton {
                background-color: #214b6b;
                color: #66c0f4;
                border: 1px solid #66c0f4;
                border-radius: 4px;
                padding: 6px 15px;
                font-weight: bold;
                font-size: 14px;
                font-family: 'Roboto', sans-serif;
            }
            QPushButton:hover {
                background-color: #66c0f4;
                color: #1b2838;
            }
            QPushButton:pressed {
                background-color: #17364f;
            }
            QRadioButton {
                background-color: transparent;
                font-size: 14px;
                padding: 3px;
            }
        """)

        self.stack = QStackedWidget()
        self.stack.setWindowTitle('Steam (Renny, Moto)')
        self.stack.resize(800, 600)
        self.stack.move(300, 100)
        
        # Instanciar las ventanas
        self.login_win = LoginWindow()
        self.store_win = StoreWindow()
        self.library_win = LibraryWindow()
        self.support_win = SupportWindow()
        self.purchase_win = PurchaseWindow() # <-- AÑADIDO
        
        # Añadir ventanas al stack
        self.stack.addWidget(self.login_win)   # Índice 0
        self.stack.addWidget(self.store_win)   # Índice 1
        self.stack.addWidget(self.library_win) # Índice 2
        self.stack.addWidget(self.support_win) # Índice 3
        self.stack.addWidget(self.purchase_win)# Índice 4 <-- AÑADIDO
        
        # Conectar las señales (cambios de ventana)
        self.login_win.login_successful.connect(lambda: self.stack.setCurrentIndex(1))
        
        # --- 3. CONEXIÓN PARA CERRAR SESIÓN ---
        self.store_win.logout_successful.connect(lambda: self.stack.setCurrentIndex(0))
        
        self.store_win.go_library.connect(lambda: self.stack.setCurrentIndex(2))
        self.store_win.go_support.connect(lambda: self.stack.setCurrentIndex(3))
        
        # <-- CONEXIÓN PARA IR A COMPRAR -->
        self.store_win.go_purchase.connect(self.open_purchase_window)
        
        self.library_win.go_store.connect(lambda: self.stack.setCurrentIndex(1))
        self.support_win.go_store.connect(lambda: self.stack.setCurrentIndex(1))
        self.purchase_win.go_store.connect(lambda: self.stack.setCurrentIndex(1)) # <-- AÑADIDO
        
        self.stack.show()

    def open_purchase_window(self, game_data):
        self.purchase_win.load_game(game_data)
        self.stack.setCurrentIndex(4)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = SteamCloneApp()
    app.run()