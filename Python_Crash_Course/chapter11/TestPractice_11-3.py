import unittest
from practice_11_3 import Employee

class TestEmployee(unittest.TestCase):
    """测试Employee类是否能正确地增加年薪"""

    def setUp(self):
        self.employee = Employee("Cavin", "Xian", 30000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 35000)

    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.salary, 38000)

unittest.main()
