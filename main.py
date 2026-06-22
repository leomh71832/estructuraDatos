import sys
from PyQt5.QtWidgets import QApplication
from load.menuui import LoadMenu



def main():
    app = QApplication(sys.argv)
    
    principal = LoadMenu()
    principal.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
