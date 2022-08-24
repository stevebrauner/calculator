class Model:
    """
    Model class for the Calculator App -- A simple RPN style calculator.

    The model includes methods for addition, subtraction, division,
    and multiplication, along with methods to manipulate the stack and check
    for division by zero.
    """

    def __init__(self):
        self._stack = []
        self.ERROR_TEXT = "ERROR (ready for entry)"

    def get_stack(self):
        return self._stack

    def clear_stack(self):
        self._stack = []

    def push_on_to_stack(self, number):
        self._stack.append(number)

    def pop_from_stack(self):
        try:
            result = self._stack.pop()
        except IndexError:
            result = None
        finally:
            return result

    def add(self, number):
        number_from_stack = self.pop_from_stack()
        if number_from_stack:
            result = number_from_stack + number
            return self.push_and_return(result)
        else:
            return self.ERROR_TEXT

    def subtract(self, number):
        number_from_stack = self.pop_from_stack()
        if number_from_stack:
            result = number_from_stack - number
            return self.push_and_return(result)
        else:
            return self.ERROR_TEXT

    def multiply(self, number):
        number_from_stack = self.pop_from_stack()
        if number_from_stack:
            result = number_from_stack * number
            return self.push_and_return(result)
        else:
            return self.ERROR_TEXT

    def divide(self, denominator):
        nominator = self.pop_from_stack()
        if denominator != 0.0 and nominator:
            result = nominator / denominator
            return self.push_and_return(result)
        elif nominator:
            self.push_on_to_stack(nominator)
            return self.ERROR_TEXT
        else:
            return self.ERROR_TEXT

    def push_and_return(self, result):
        self.push_on_to_stack(result)
        return result
