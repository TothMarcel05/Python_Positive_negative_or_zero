"""
Production code - This is the application code that we are testing.
This module contains the business logic for determining if a number 
is positive, negative, or zero.
"""

def categorize_number(number):
    """
    Kategorizálja a számot pozitív, negatív vagy nulla kategóriába.
    
    Args:
        number (int vagy float): A kategorizálandó szám
        
    Returns:
        str: "Pozitív" ha a szám > 0, "Negatív" ha < 0, "Nulla" ha = 0
    """
    number = float(number) 
    if number > 0:
        return "Pozitív"
    elif number < 0:
        return "Negatív"
    else:
        return "Nulla"