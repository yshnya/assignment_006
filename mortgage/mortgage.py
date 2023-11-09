"""
Description: A class meant to manage Mortgage options.
Author: Czanel Siscar
Date: 2023/11/08
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount, rate, frequency, amortization):
        if loan_amount < 0:
            self.loan_amount = loan_amount
        else:
            raise ValueError("Loan Amount must be a positive.")
        
        if not isinstance(rate,MortgageRate):
            raise ValueError("Rate provided is invalid.")
        else:
            self.rate = rate
        
        if not isinstance(frequency,MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        else:
            self.frequency = frequency

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self.amortization = amortization