import unittest

from calculator.model import Model


class TestModelClass(unittest.TestCase):
    """Tests for model class."""

    def setUp(self):
        self.model = Model()
        self.model._stack = [4.0]

    def test_get_stack(self):
        stack = self.model.get_stack()
        self.assertEqual(stack, [4.0])

    def test_clear_stack(self):
        self.model.clear_stack()
        self.assertEqual(self.model._stack, [])

    def test_push_on_to_stack(self):
        self.model.push_on_to_stack(1.0)
        self.assertEqual(self.model._stack, [4.0, 1.0])

    def test_pop_from_stack(self):
        number = self.model.pop_from_stack()
        self.assertEqual(number, 4.0)

    def test_add(self):
        number = self.model.add(1.0)
        self.assertEqual(number, 5.0)

    def test_subtract(self):
        number = self.model.subtract(1.0)
        self.assertEqual(number, 3.0)

    def test_multiply(self):
        number = self.model.multiply(2.0)
        self.assertEqual(number, 8.0)

    def test_divide(self):
        number = self.model.divide(2.0)
        self.assertEqual(number, 2.0)
        result = self.model.divide(0.0)
        self.assertEqual(result, "ERROR (ready for entry)")
        self.assertEqual(self.model._stack, [2.0])
        self.model._stack = []
        result = self.model.divide(2.0)
        self.assertEqual(result, "ERROR (ready for entry)")

    def test_push_and_return(self):
        number = self.model.push_and_return(1.0)
        self.assertEqual(number, 1.0)
