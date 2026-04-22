import io
import unittest
from contextlib import redirect_stdout

from main import build_multiplication_message, is_equal, multiply, run


class TestMain(unittest.TestCase):
    def test_multiply_returns_product(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 10), 0)

    def test_is_equal_true(self):
        self.assertTrue(is_equal(25, 25))

    def test_is_equal_false(self):
        self.assertFalse(is_equal(24, 25))

    def test_build_multiplication_message(self):
        message = build_multiplication_message(5, 5, 25)
        self.assertEqual(message, "5 * 5 is equal to 25")

    def test_run_prints_expected_message(self):
        output = io.StringIO()
        with redirect_stdout(output):
            run()
        self.assertEqual(output.getvalue().strip(), "5 * 5 is equal to 25")


if __name__ == "__main__":
    unittest.main()
