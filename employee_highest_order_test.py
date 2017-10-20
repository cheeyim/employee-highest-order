import unittest
from employee_highest_order import highest_management_order

class HighestManagementOrderTest(unittest.TestCase):   
    def test_sample1(self):
        test_sample = ["Hilary", "James", "Sarah Fred", "Sarah Paul", "Fred Hilary", "Fred Jenny", "Jenny James"]
        self.assertTrue(highest_management_order(test_sample) == "Fred")
    
    def test_sample2(self):
        test_sample = ["Claudia", "Simon", "Sarah Claudia", "Sarah Paul", "Claudia Simon"]
        self.assertTrue(highest_management_order(test_sample) == "Claudia")

    def test_sample3(self):
        test_sample = ["Alex", "Gareth", "June Alex", "June Qing", "Qing Paul", "Qing Gareth"]
        self.assertTrue(highest_management_order(test_sample) == "June")

    def test_sample4(self):
        test_sample = ["Mary", "Gareth", "June Alex", "June Qing", "Alex Mary", "Qing Paul", "Qing Gareth"]
        self.assertTrue(highest_management_order(test_sample) == "June")

if __name__ == '__main__':
    unittest.main()