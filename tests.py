import unittest
from loan_calculator import loan_calculator

class LoanCalculator(unittest.TestCase):
    def test_loan_calculator_returns_correct_repayment_value(self):
        self.assertEqual(loan_calculator(100000, 12, 12), 112000, 'The formula does not work')

if __name__ == '__main__':
    unittest.main()
