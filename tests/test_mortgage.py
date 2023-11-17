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

    def test_loan_amount_negative(self):
        # Arrange
        mortgage = Mortgage(120000, MortgageRate.FIXED_1, 
                            MortgageFrequency.BI_WEEKLY, 25)
        expected = "Loan Amount must be positive."
        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = -120000
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_loan_amount_zero(self):
        # Arrange
        mortgage = Mortgage(120000, MortgageRate.FIXED_1, 
                            MortgageFrequency.BI_WEEKLY, 25)
        expected = "Loan Amount must be positive."
        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.loan_amount = 0
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_loan_amount_accessor(self):
        # Arrange and Act
        mortgage = Mortgage(120000, MortgageRate.FIXED_3, 
                            MortgageFrequency.BI_WEEKLY, 25)
        # Assert
        self.assertEqual(mortgage.loan_amount, 120000)

    def test_rate_value(self):
        # Arrange and Act
        mortgage = Mortgage(120000, MortgageRate.FIXED_1,
                           MortgageFrequency.BI_WEEKLY,25)
        # Assert
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_1)

    def test_rate_error(self):
        # Arrange
        mortgage = Mortgage(120000, MortgageRate.FIXED_1,
                            MortgageFrequency.BI_WEEKLY, 25)
        expected = "Rate provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.rate = 0.69
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_frequency_value(self):
        # Arrange and Act
        mortgage = Mortgage(120000, MortgageRate.FIXED_1,
                            MortgageFrequency.BI_WEEKLY, 25)
        # Assert
        self.assertEqual(mortgage.frequency, MortgageFrequency.BI_WEEKLY)

    def test_frequency_error(self):
        # Arrange
        mortgage = Mortgage(120000, MortgageRate.FIXED_1,
                            MortgageFrequency.BI_WEEKLY, 25)
        expected = "Frequency provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.frequency = 0.69
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_amortization_value(self):
        # Arrange and Act
        mortgage = Mortgage(120000, MortgageRate.FIXED_1, 
                            MortgageFrequency.BI_WEEKLY, 25)
        # Assert
        self.assertEqual(mortgage.amortization, 25)

    def test_amortization_error(self):
        # Arrange
        mortgage = Mortgage(120000, MortgageRate.FIXED_1, 
                            MortgageFrequency.BI_WEEKLY, 25)
        expected = "Amortization provided is invalid."
        # Act
        with self.assertRaises(ValueError) as context:
            mortgage.amortization = 69
        # Assert
        self.assertEqual(str(context.exception), expected)

    def test_init_value(self):
        # Arrange
        loan_amount = 120000
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 25
        # Act
        mortgage = Mortgage(120000, MortgageRate.FIXED_1,
                            MortgageFrequency.BI_WEEKLY, 25)
        # Assert
        self.assertEqual(mortgage._loan_amount, loan_amount)
        self.assertEqual(mortgage._rate, rate)
        self.assertEqual(mortgage._frequency, frequency)
        self.assertEqual(mortgage._amortization, amortization)

    def test_calculate_payment(self):
        # Arrange
        amount = 100000
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 25
        expected = 637.59
        # Act
        mortgage = Mortgage(amount, rate, frequency, amortization)
        actual = mortgage.calculate_payment()
        # Assert
        self.assertAlmostEqual(expected, actual, 2)

    def test_calculate_payment_two(self):
        # Arrange
        amount = 169000
        rate = MortgageRate.FIXED_3
        frequency = MortgageFrequency.MONTHLY
        amortization = 30
        expected = 990.54
        # Act
        mortgage = Mortgage(amount, rate, frequency, amortization)
        actual = mortgage.calculate_payment()
        # Assert
        self.assertAlmostEqual(expected, actual, 2)

    def test_calculate_payment_three(self):
        # Arrange
        amount = 200000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 25
        expected = 539.32
        # Act
        mortgage = Mortgage(amount, rate, frequency, amortization)
        actual = mortgage.calculate_payment()
        # Assert
        self.assertAlmostEqual(expected, actual, 2)