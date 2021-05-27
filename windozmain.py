
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
import string
from PySide6.QtUiTools import QUiLoader


class windozmain(QMainWindow):
    def __init__(self):
        super(windozmain, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.bt_1.clicked.connect(self.generate)
        self.password = string.ascii_letters + string.digits + string.printable + string.ascii_uppercase

    def generate(self):
        if self.ui.rb_1.isChecked():
            password = ''.join(random.choice(self.password) for i in range(8))
            self.ui.tb_1.setText(password)

        if self.ui.rb_2.isChecked():
            password = ''.join(random.choice(self.password) for i in range(12))
            self.ui.tb_1.setText(password)

        if self.ui.rb_3.isChecked():
            password = ''.join(random.choice(self.password) for i in range(16))
            self.ui.tb_1.setText(password)


if __name__ == "__main__":
    app = QApplication([])
    window = windozmain()
    sys.exit(app.exec_())
