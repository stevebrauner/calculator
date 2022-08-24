from PySide6 import QtCore, QtWidgets


class View(QtWidgets.QWidget):
    """
    View for Calculator App -- a simple RPN style calculator.

    View uses PySide6 GUI framework.
    """

    def __init__(self):
        super().__init__()
        self.button = dict()

    def create_view(self):
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.layout_keys()
        self.layout_entry()
        self.layout_stack()

    def layout_keys(self):
        self.layout_button("0", 5, 1)
        self.layout_button("1", 4, 1)
        self.layout_button("2", 4, 2)
        self.layout_button("3", 4, 3)
        self.layout_button("4", 3, 1)
        self.layout_button("5", 3, 2)
        self.layout_button("6", 3, 3)
        self.layout_button("7", 2, 1)
        self.layout_button("8", 2, 2)
        self.layout_button("9", 2, 3)

        self.layout_button(".", 5, 3)

        self.layout_button("POP", 4, 0)
        self.layout_button("DRP", 3, 0)
        self.layout_button("C", 2, 0)
        self.layout_button("AC", 1, 0)
        self.layout_button("SWP", 1, 1)
        self.layout_button("+/-", 1, 2)
        self.layout_button("/", 1, 3)
        self.layout_button("*", 1, 4)
        self.layout_button("-", 2, 4)
        self.layout_button("+", 3, 4)

        self.enter = QtWidgets.QPushButton("RET")
        self.set_size_policy(self.enter)
        self.enter.setMinimumSize(50, 50)
        self.grid_layout.addWidget(self.enter, 4, 4, 2, 1)

    def layout_button(self, text, row, column):
        self.button[text] = QtWidgets.QPushButton(text)
        self.set_size_policy(self.button[text])
        self.button[text].setMinimumSize(50, 50)
        self.grid_layout.addWidget(self.button[text], row, column)

    def layout_entry(self):
        self.entry = QtWidgets.QLabel()
        self.set_size_policy(self.entry)
        self.entry.setAlignment(QtCore.Qt.AlignRight)
        self.grid_layout.addWidget(self.entry, 0, 0, 1, 5)

    def layout_stack(self):
        self.stack = QtWidgets.QLabel()
        self.set_size_policy(self.stack)
        self.stack.setAlignment(QtCore.Qt.AlignBottom)
        self.grid_layout.addWidget(self.stack, 1, 5, 5, 3)

    def set_size_policy(self, widget):
        widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding,
        )
