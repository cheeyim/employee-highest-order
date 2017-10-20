"""
This is a test module to test highest_management_order function.
"""

import unittest
from employee_highest_order import highest_management_order

class HighestManagementOrderTest(unittest.TestCase):
    """
    Highest Management Order Test Class
    """
    def test_sample1(self):
        """
        Test Sample - Different employees level with 4 levels.
        """
        test_sample = ["Hilary", "James", "Sarah Fred", "Sarah Paul",
                       "Fred Hilary", "Fred Jenny", "Jenny James"]
        self.assertTrue(highest_management_order(test_sample) == "Fred")

    def test_sample2(self):
        """
        Test Sample - Employee1 is manager of Employee2.
        """
        test_sample = ["Claudia", "Simon", "Sarah Claudia", "Sarah Paul", "Claudia Simon"]
        self.assertTrue(highest_management_order(test_sample) == "Claudia")

    def test_sample3(self):
        """
        Test Sample - Different employees level with 3 levels.
        """
        test_sample = ["Alex", "Gareth", "June Alex", "June Qing", "Qing Paul", "Qing Gareth"]
        self.assertTrue(highest_management_order(test_sample) == "June")

    def test_sample4(self):
        """
        Test Sample - Different employees level with 3 levels, with similar managers at the root.
        """
        test_sample = ["Mary", "Gareth", "June Alex", "June Qing",
                       "Alex Mary", "Qing Paul", "Qing Gareth"]
        self.assertTrue(highest_management_order(test_sample) == "June")

if __name__ == '__main__':
    unittest.main()
