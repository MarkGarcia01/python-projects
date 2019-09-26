#!/usr/bin/env python3
# Yearly Salary Raise
# Mark Garcia
# 9/25/2019
# -----------------------------------------------------------------------


def main():

    # Define function to calculate pay raise per year
    def calSalaryIncrease(userSalary, percentIncrease, totalYears, year):

        while year < totalYears:
            userSalary = (userSalary * percentIncrease) + userSalary
            year += 1
            print(f'On year {year}, your salary will be:')
            print('  ${:,.2f}'.format(userSalary))

    # Gather User Input
    userSalary = int(input('Enter salary:'))
    percentIncrease = float(input('Enter percent:'))
    totalYears = int(input('Enter total years:'))

    year = 0

    # Call the function and pass the variables
    calSalaryIncrease(userSalary, percentIncrease, totalYears, year)


# main call
if __name__ == '__main__':
    main()
