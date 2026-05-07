import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login import LoginWindow
from store import StoreWindow
from library import LibraryWindow
from support import SupportWindow

class SteamCloneApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        # QStackedWidget nos permite apilar ventanas y mostrar una a la vez
        self.stack = QStackedWidget()
        self.stack.setWindowTitle('Steam Clone App')
        self.stack.resize(800, 600)
        self.stack.move(300, 100)
        
        # Instanciar las ventanas
        self.login_win = LoginWindow()
        self.store_win = StoreWindow()
        self.library_win = LibraryWindow()
        self.support_win = SupportWindow()
        
        # Añadir ventanas al stack
        self.stack.addWidget(self.login_win)   # Índice 0
        self.stack.addWidget(self.store_win)   # Índice 1
        self.stack.addWidget(self.library_win) # Índice 2
        self.stack.addWidget(self.support_win) # Índice 3
        
        # Conectar las señales (cambios de ventana)
        self.login_win.login_successful.connect(lambda: self.stack.setCurrentIndex(1))
        
        self.store_win.go_library.connect(lambda: self.stack.setCurrentIndex(2))
        self.store_win.go_support.connect(lambda: self.stack.setCurrentIndex(3))
        
        self.library_win.go_store.connect(lambda: self.stack.setCurrentIndex(1))
        self.support_win.go_store.connect(lambda: self.stack.setCurrentIndex(1))
        
        self.stack.show()

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = SteamCloneApp()
    app.run()