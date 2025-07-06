"""
Day 25-26 – Module 6 Assignment (4.6)
Compute gross pay with overtime using a function.
"""

def computepay(hours: float, rate: float) -> float:
    """
    Return gross pay.

    Regular rate for the first 40 hours;
    1.5 × rate for any hours over 40.
    """
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    return pay


# ---- main script ----
if __name__ == "__main__":
    hrs_input = input("Enter Hours: ")
    rate_input = input("Enter Rate: ")

    hours = float(hrs_input)
    rate = float(rate_input)

    pay = computepay(hours, rate)
    print("Pay", pay)
