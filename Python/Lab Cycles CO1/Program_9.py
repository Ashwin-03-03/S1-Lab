# WAP to check whether an entered year is a leap year or not.
def leapYearChecker():
    year = int(input("Enter a year: "))
    if (year%4==0 and year%100==0):
        print("The entered year is not a leap year")
    elif (year%4==0 or year%400==0):
        print("The enetered year is a leap year")
    else:
        print("The year is not a leap year")
        
leapYearChecker()
