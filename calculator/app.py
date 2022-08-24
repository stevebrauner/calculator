"""
Main file for running the Calculator App -- a simple RPN style calculator.

The App class instantiates the Model, View, and Controller classes, and
provides a run method.
This file also provides a main class to instantiate the App class and to
provide the if __name__ == "__main__" statement for running with
"python app.py".
"""
import sys

from controller import Controller
from model import Model
from PySide6 import QtWidgets
from view import View


class App:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)

    def run(self):
        self.view.create_view()
        self.controller.connect_view_controller()
        self.view.show()
        sys.exit(self.app.exec())


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()
