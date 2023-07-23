def main():
    print("This is monthly payment loan calculator ")
    print("")

    principal=float(input("The loan amount:   "))
    apr=float(input("Input the annual interest rate:  "))
    years=int(input("Input amount of years:   "))

    monthlu_interest_rate=apr/1200
    amount_of_months=years*12
    monthly_payment=principal*monthlu_interest_rate/(1-(1+monthlu_interest_rate)**(-amount_of_months))

    print("Monthly payment for this loan is:  %.2f  " % monthly_payment)
    
main()