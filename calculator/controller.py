from PySide6 import QtCore


class Controller:
    """
    Controller class for the Calculator App -- a simple RPN style calculator.

    The controller connects the Model and View classes.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.ERROR_TEXT = "ERROR (ready for entry)"
        self._entry = ""

    def connect_view_controller(self):
        self.view.button["9"].clicked.connect(self.nine)
        self.view.button["8"].clicked.connect(self.eight)
        self.view.button["7"].clicked.connect(self.seven)
        self.view.button["6"].clicked.connect(self.six)
        self.view.button["5"].clicked.connect(self.five)
        self.view.button["4"].clicked.connect(self.four)
        self.view.button["3"].clicked.connect(self.three)
        self.view.button["2"].clicked.connect(self.two)
        self.view.button["1"].clicked.connect(self.one)
        self.view.button["0"].clicked.connect(self.zero)
        self.view.button["."].clicked.connect(self.period)

        self.view.button["POP"].clicked.connect(self.entry_from_stack)
        self.view.button["DRP"].clicked.connect(self.drop_from_stack)
        self.view.button["C"].clicked.connect(self.clear_entry)
        self.view.button["AC"].clicked.connect(self.clear_all)
        self.view.button["SWP"].clicked.connect(self.swap_entry_stack_top)
        self.view.button["+/-"].clicked.connect(self.plus_minus)
        self.view.button["/"].clicked.connect(self.divide)
        self.view.button["*"].clicked.connect(self.multiply)
        self.view.button["-"].clicked.connect(self.subtract)
        self.view.button["+"].clicked.connect(self.add)
        self.view.enter.clicked.connect(self.enter)

    @QtCore.Slot()
    def nine(self):
        self._entry += "9"
        self.update_view_entry()

    @QtCore.Slot()
    def eight(self):
        self._entry += "8"
        self.update_view_entry()

    @QtCore.Slot()
    def seven(self):
        self._entry += "7"
        self.update_view_entry()

    @QtCore.Slot()
    def six(self):
        self._entry += "6"
        self.update_view_entry()

    @QtCore.Slot()
    def five(self):
        self._entry += "5"
        self.update_view_entry()

    @QtCore.Slot()
    def four(self):
        self._entry += "4"
        self.update_view_entry()

    @QtCore.Slot()
    def three(self):
        self._entry += "3"
        self.update_view_entry()

    @QtCore.Slot()
    def two(self):
        self._entry += "2"
        self.update_view_entry()

    @QtCore.Slot()
    def one(self):
        self._entry += "1"
        self.update_view_entry()

    @QtCore.Slot()
    def zero(self):
        self._entry += "0"
        self.update_view_entry()

    @QtCore.Slot()
    def period(self):
        if "." not in self._entry:
            self._entry += "."
            self.update_view_entry()

    @QtCore.Slot()
    def entry_from_stack(self):
        top_of_stack = self.model.pop_from_stack()
        if top_of_stack:
            self._entry = str(top_of_stack)
            self.update_view_entry()
            self.update_view_stack()
        else:
            self._entry = ""
            self.view.entry.setText(self.ERROR_TEXT)

    @QtCore.Slot()
    def drop_from_stack(self):
        result = self.model.pop_from_stack()
        if result:
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def clear_entry(self):
        self._entry = ""
        self.update_view_entry()

    @QtCore.Slot()
    def clear_all(self):
        self.clear_entry()
        self.model.clear_stack()
        self.update_view_entry()
        self.update_view_stack()

    @QtCore.Slot()
    def swap_entry_stack_top(self):
        entry_as_float = self.convert_entry_to_float()
        number_from_stack = self.model.pop_from_stack()
        if entry_as_float and number_from_stack:
            self._entry = str(number_from_stack)
            self.model.push_on_to_stack(entry_as_float)
            self.update_view_entry()
            self.update_view_stack()
        elif number_from_stack:
            self.entry_error()
            self.model.push_on_to_stack(number_from_stack)
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def plus_minus(self):
        if "-" not in self._entry:
            self._entry = "-" + self._entry
            self.update_view_entry()
        else:
            self._entry = self._entry[1:]
            self.update_view_entry()

    @QtCore.Slot()
    def enter(self):
        entry_as_float = self.convert_entry_to_float()
        if entry_as_float is not None:
            self.model.push_on_to_stack(entry_as_float)
            self._entry = ""
            self.update_view_entry()
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def divide(self):
        denominator = self.convert_entry_to_float()
        if denominator == 0.0:
            self.entry_error()
        elif denominator:
            answer = str(self.model.divide(denominator))
            self.display_entry_then_clear(answer)
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def multiply(self):
        number = self.convert_entry_to_float()
        if number is not None:
            answer = str(self.model.multiply(number))
            self.display_entry_then_clear(answer)
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def add(self):
        number = self.convert_entry_to_float()
        if number is not None:
            answer = str(self.model.add(number))
            self.display_entry_then_clear(answer)
            self.update_view_stack()
        else:
            self.entry_error()

    @QtCore.Slot()
    def subtract(self):
        number = self.convert_entry_to_float()
        if number is not None:
            answer = str(self.model.subtract(number))
            self.display_entry_then_clear(answer)
            self.update_view_stack()
        else:
            self.entry_error()

    def convert_entry_to_float(self):
        result = None
        try:
            result = float(self._entry)
        except ValueError:
            result = None
        finally:
            return result

    def entry_error(self):
        self._entry = ""
        self.view.entry.setText(self.ERROR_TEXT)

    def display_entry_then_clear(self, value):
        self.view.entry.setText(value)
        self._entry = ""

    def update_view_entry(self):
        self.view.entry.setText(self._entry)

    def update_view_stack(self):
        stack_for_view = "\n".join(map(str, self.model._stack[::-1]))
        self.view.stack.setText(stack_for_view)
