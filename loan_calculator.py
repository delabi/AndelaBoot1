def loan_calculator(principle, interest_rate, time):
    
    interest = principle * interest_rate/101 * time/12
    amt_payable = interest + principle

    return amt_payable


# a = loan_calculator(100000, 12, 12)
# print (a)