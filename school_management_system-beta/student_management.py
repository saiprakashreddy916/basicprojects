



from desktop_gui.dashboard import dashboard
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    _try = dashboard()
    _try.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing windown..')
