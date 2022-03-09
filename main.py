from ui import UI
from ui_MEZ import UI_MEZ
from PyQt5 import QtWidgets

if __name__ == "__main__":
    from translater import TRANSLATE

    # TRANSLATE.into_str = "с.ектор газа"
    # TRANSLATE.rus_in_eng()
    # TRANSLATE.into_str = TRANSLATE.out_str
    # TRANSLATE.out_str = ""
    # TRANSLATE.eng_in_rus()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())