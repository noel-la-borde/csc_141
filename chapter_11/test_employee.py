import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class without using a fixture."""

    def test_give_default_raise(self):
        """Test the default raise of $5,000."""
        employee = Employee('John', 'Doe', 50000)
        employee.give_raise()
        self.assertEqual(employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        employee = Employee('Jane', 'Doe', 60000)
        employee.give_raise(10000)
        self.assertEqual(employee.annual_salary, 70000)

if __name__ == '__main__':
    unittest.main()

# This one became very tricky because for some reason pytest didn't work and I had to use unittest instead. 