# Lucky Lotto Picker
# Written by: Mark Garcia
# Date: 8/27/2019
# -------------------------------------------------------------------

import random
import datetime

# Declare Variables--------------------------------------------------
lottoNumbers = random.sample(range(54), 6)
now = datetime.datetime.now()

# Output--------------------------------------------------------------
print(lottoNumbers)

print("Current date and time:")
print(now.strftime("%m-%d-%Y %I:%M%p"))
print('\nYour lucky lotto numbers are: ')

# Sort the list from lowest to highest number-------------------------
lottoNumbers.sort()
print(lottoNumbers)

# Save to a file
print("Current date and time:", now.strftime("\n%m-%d-%Y %I:%M%p"), '\nYour lucky lotto numbers are: ', lottoNumbers, '\n', file=open("todayslottonumbers.txt", "a"))

# Pause---------------------------------------------------------------
twonk = input('Press any key to continue...')

