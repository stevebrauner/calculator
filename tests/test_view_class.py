import pytest

from calculator.view import View


class TestViewClass:
    """Tests for View class."""

    @pytest.fixture
    def test_view(self, qtbot):
        qview = View()
        qview.create_view()
        qtbot.addWidget(qview)
        return qview

    def test_buttons(self, test_view):
        button_keys = {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            ".",
            "POP",
            "DRP",
            "C",
            "AC",
            "SWP",
            "+/-",
            "/",
            "*",
            "-",
            "+",
        }
        view_button_keys = test_view.button.keys()
        assert view_button_keys == button_keys

    def test_enter(self, test_view):
        view_enter_text = test_view.enter.text()
        assert view_enter_text == "RET"

    def test_entry(self, test_view):
        view_entry_text = test_view.entry.text()
        assert view_entry_text == ""

    def test_stack(self, test_view):
        view_stack_text = test_view.stack.text()
        assert view_stack_text == ""
