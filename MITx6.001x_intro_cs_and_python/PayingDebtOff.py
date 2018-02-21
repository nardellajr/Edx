"""
For each month:
    Compute the monthly payment, based on the previous month’s balance.

    Update the outstanding balance by removing the payment, then charging interest on the result.

    Output the month, the minimum monthly payment and the remaining balance.

    Keep track of the total amount of paid over all the past months so far.

Print out the result statement with the total amount paid and the remaining balance.
"""


def creditcardbalance(balance, annualInterestRate, monthlyPaymentRate):
    """

    :param balance:
    :param annualInterestRate:
    :param monthlyPaymentRate:
    :return:
    """

    # Test Case 1
    # Month 1 Remaining balance: 40.90
    # Month 2 Remaining balance: 40.01
    # Month 3 Remaining balance: 39.05



    # Test Case 1
    # print("Remaining balance: 31.38



if __name__ == '__main__':
    assert creditcardbalance(42, 0.2, 0.04) == 31.38, "Should return 31.38"
    assert creditcardbalance(484, 0.2, 0.04) == 361.61, "Should return 361.61"

