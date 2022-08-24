import unittest

from pytestqt.qt_compat import qt_api

from calculator.controller import Controller
from calculator.model import Model
from calculator.view import View


def test_basics(qtbot):
    """Basic test so QApplication instance exists for the following tests."""
    assert qt_api.QtWidgets.QApplication.instance() is not None
    widget = qt_api.QtWidgets.QWidget()
    qtbot.addWidget(widget)
    widget.setWindowTitle("W1")
    widget.show()

    assert widget.isVisible()
    assert widget.windowTitle() == "W1"


class TestControllerClass(unittest.TestCase):
    """Tests Controller class."""

    def setUp(self):
        self.model = Model()
        self.model._stack = [4.0]
        self.view = View()
        self.view.create_view()
        self.controller = Controller(self.model, self.view)
        self.controller.connect_view_controller()

    def test_drop_from_stack(self):
        self.controller.drop_from_stack()
        self.assertEqual(self.model._stack, [])

    def test_clear_entry(self):
        self.controller._entry = "1.0"
        self.controller.clear_entry()
        self.assertEqual(self.controller._entry, "")

    def test_clear_all(self):
        self.controller._entry = "1.0"
        self.controller.clear_all()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [])

    def test_swap_entry_stack_top(self):
        self.controller._entry = "1.0"
        self.controller.swap_entry_stack_top()
        self.assertEqual(self.controller._entry, "4.0")
        self.assertEqual(self.model._stack, [1.0])
        self.controller._entry = ""
        self.controller.swap_entry_stack_top()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [1.0])

    def test_enter(self):
        self.controller._entry = "1.0"
        self.controller.enter()
        self.assertEqual(self.model._stack, [4.0, 1.0])
        self.assertEqual(self.controller._entry, "")
        self.controller._entry = "0.0"
        self.controller.enter()
        self.assertEqual(self.model._stack, [4.0, 1.0, 0.0])
        self.assertEqual(self.controller._entry, "")
        self.controller.enter()
        self.assertEqual(self.model._stack, [4.0, 1.0, 0.0])
        self.assertEqual(self.controller._entry, "")

    def test_divide(self):
        self.controller._entry = "2.0"
        self.controller.divide()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [2.0])
        self.controller._entry = "0.0"
        self.controller.divide()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [2.0])
        self.controller._entry = ""
        self.controller.divide()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [2.0])

    def test_multiply(self):
        self.controller._entry = "2.0"
        self.controller.multiply()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [8.0])
        self.controller._entry = "0.0"
        self.controller.multiply()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [0.0])
        self.controller._entry = ""
        self.model._stack = [4.0]
        self.controller.multiply()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [4.0])

    def test_add(self):
        self.controller._entry = "1.0"
        self.controller.add()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [5.0])
        self.controller._entry = "0.0"
        self.controller.add()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [5.0])
        self.controller._entry = ""
        self.controller.add()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [5.0])

    def test_subtract(self):
        self.controller._entry = "1.0"
        self.controller.subtract()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [3.0])
        self.controller._entry = "0.0"
        self.controller.subtract()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [3.0])
        self.controller._entry = ""
        self.controller.subtract()
        self.assertEqual(self.controller._entry, "")
        self.assertEqual(self.model._stack, [3.0])
