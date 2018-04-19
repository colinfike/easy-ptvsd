"""Tests for easy_ptvsd module."""
import types
import unittest
from unittest.mock import Mock, patch

from easy_ptvsd import wait_and_break


class TestWaitAndBreakClass(unittest.TestCase):
    """Tests for the wait_and_break class."""

    def test_default_init_parameters(self):
        """Test that default parameters are working properly."""
        wait_and_break_obj = wait_and_break()
        self.assertEqual(wait_and_break_obj.address, ("0.0.0.0", 3000))
        self.assertEqual(wait_and_break_obj.secret, "my_secret")

    def test_custom_init_parameters(self):
        """Test that custom parameters are working properly."""
        wait_and_break_obj = wait_and_break(
            address=("1.2.3.4", 4000), secret="your_secret"
        )
        self.assertEqual(wait_and_break_obj.address, ("1.2.3.4", 4000))
        self.assertEqual(wait_and_break_obj.secret, "your_secret")

    def test_invocation_returns_function(self):
        """Test that invoking a wait_and_break object returns a function."""
        wait_and_break_obj = wait_and_break()
        result = wait_and_break_obj(None)
        self.assertTrue(isinstance(result, types.FunctionType))

    @patch("easy_ptvsd.ptvsd")
    def test_decorated_function_wrapper_functionality(self, mock_ptvsd):
        """Test that the function returned by invoking wait_and_break is functional."""
        decorated_func_mock = Mock(return_value="ret val")
        wait_and_break_obj = wait_and_break()
        result = wait_and_break_obj(decorated_func_mock)

        return_value = result("positional_arg", key_word_arg="keywordarg")

        self.assertTrue(mock_ptvsd.enable_attach.called)
        self.assertTrue(mock_ptvsd.wait_for_attach.called)
        self.assertTrue(mock_ptvsd.break_into_debugger.called)
        self.assertEqual(return_value, "ret val")
        decorated_func_mock.assert_called_once_with(
            "positional_arg", key_word_arg="keywordarg"
        )


if __name__ == "__main__":
    unittest.main()
