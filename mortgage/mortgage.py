"""
Description: A class meant to manage Mortgage options.
Author: Czanel Siscar
Date: 2023/11/08
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount: float, rate: MortgageRate, 
                 frequency: MortgageFrequency, amortization: int):
        """
        Initializes new __init__ method
        Args:
            loan_amount(float): The amount of the mortgage loan.
            rate(MortgageRate): The annual interest rate.
            Frequency(int): The number of payments per year.
            Amortization(int): The number of years to repay the mortgage loan.
        Returns:
            None
        """
        if loan_amount >= 0:
            self._loan_amount = loan_amount
        else:
            raise ValueError("Loan Amount must be a positive.")
        
        if not isinstance(rate,MortgageRate):
            raise ValueError("Rate provided is invalid.")
        else:
            self._rate = rate
        
        if not isinstance(frequency,MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        else:
            self._frequency = frequency

        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self._amortization = amortization