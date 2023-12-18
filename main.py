import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_items = self.menuBar().addMenu("&File")
        help_menu_items = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        file_menu_items.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_items.addAction(about_action)
        # For Mac
        # about_action.setMenuRole(QAction.MenuRole.NoRole)


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
sys.exit(app.exec())
