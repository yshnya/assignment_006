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

    @property
    def loan_amount(self) -> float:
        """
        accessor for the _loan_amount attribute
        """
        return self._loan_amount
    
    # Mutator for loan_amount
    @loan_amount.setter
    def loan_amount(self, value: float):
        if value <= 0:
            raise ValueError("Loan Amount must be positive.")
        else:
            self._loan_amount = value
    
    @property
    def rate(self) -> MortgageRate:
        """
        accessor for the _rate attribute
        """
        return self._rate
    
    # Mutator for rate
    @rate.setter
    def rate(self, value: MortgageRate):
        if not isinstance(value,MortgageRate):
            raise ValueError("Rate provided is invalid.")
        else:
            self._rate = value
    
    @property
    def frequency(self) -> MortgageFrequency:
        """
        accessor for the _frequency attribute
        """
        return self._frequency
    
    # Mutator for frequency
    @frequency.setter
    def frequency(self, value: MortgageFrequency):
        if not isinstance(value,MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        else:
            self._frequency = value

    @property
    def amortization(self) -> int:
        """
        accessor for the _amortization attribute
        """
        return self._amortization
    
    # Mutator for amortization
    @amortization.setter
    def amortization(self, value: int):
        if value not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        else:
            self._amortization = value

    def calculate_payment(self) -> float:
        """
        Calculates the mortgage payment amount
        Returns:
            float: the mortgage payment amount
        """
        interest_rate = self._rate.value / self._frequency.value
        payment_amount = self._amortization * self._frequency.value
        interest_numerator = interest_rate * (1 + interest_rate) ** payment_amount
        interest_denominator = ((1 + interest_rate) ** payment_amount) - 1
        principal_loan = self._loan_amount
        calculated_payment = principal_loan * (interest_numerator / interest_denominator)

        return calculated_payment
    
    def __str__(self) -> str:
        """

        Returns:
            str: All the values used in the calculation.
        """
        return f"Mortgage Amount: ${self.loan_amount:,.2f}\n" \
               f"Rate: {self.rate.value:.2%}\n" \
               f"Amortization: {self.amortization}\n" \
               f"Frequency: {self.frequency.name} -- Calculated Payment: ${self.calculate_payment():,.2f}"
    
    def __repr__(self) -> str:
        """
        Returns the values of each valid input on its own
        Returns:
            str: All the values in string format on its own
        """
        return f"[{self.loan_amount}, {self.rate.value}, {self.amortization}, {self.frequency.value}]"
               
    
    