# Magic 8 Ball
# Mark Garcia
# 8/30/2019
#------------------------------------------------------------------------------------------------

import sys
import random


question = input("Ask the magic 8 ball a question: (press Y for answer or any key to quit) ")
    
#Here we are telling the script to pick a random number from 1 through 20, and based on the result is what the answer displayed will be.
answers = ['It is certain', 'Outlook good', 'You may rely on it', 'Ask again later', 'Concentrate and ask again', 'Reply hazy, try again',
               'My reply is no', 'My sources say no', 'It is decidedly so', 'Outlook not so good', 'Very doubtful', 'Dont count on it',
               'Cannot predict now', 'Better not tell you now', 'Signs point to yes', 'Yes', 'Most likely', 'As I see it, yes', 'Yes - definitely',
               'Without a doubt']
    
#If the user presses ENTER, then the script will exit.
if question == "Y":
    
    print(random.choice(answers))

else:

    sys.exit()

#This will allow the script to stay displayed if the script is launched from within a command prompt.
twonk=input("Press Enter to continue...")
