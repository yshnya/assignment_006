"""
Description: A class used to test the Mortgage class.
Author: Czanel Siscar
Date: 2023/11/08
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(unittest.TestCase):
    def test_init_invalid_loan(self):   
        # Arrange
        loan_amount = -10
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = VALID_AMORTIZATION

        expected = "Loan Amount must be a positive."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_init_invalid_rate(self):
        # Arrange
        loan_amount = 10
        rate = 10
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = VALID_AMORTIZATION

        expected = "Rate provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_init_invalid_frequency(self):
        # Arrange
        loan_amount = 10
        rate = MortgageRate.FIXED_1
        frequency = 5
        amortization = VALID_AMORTIZATION

        expected = "Frequency provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization,)
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_init_invalid_amortization(self):
        # Arrange
        loan_amount = 10
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 2

        expected = "Amortization provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            Mortgage(loan_amount, rate, frequency, amortization)
        # Assert
        self.assertEqual(str(context.exception),expected)