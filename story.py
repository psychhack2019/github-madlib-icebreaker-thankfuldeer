"""
@author: annabel wing-yan fan 2019

INSTRUCTIONS
Using a python IDE (i.e. Spyder) open and run both the madlib and story script

1) Run your madlib script
2) Run this script

credits: adapted from PhD Comics: https://tapas.io/episode/37261
"""


import madlib

story = ("This paper presents a " + synonymForNew + " method for " +
         sciencyVerb + "\nthe " + nounFewPeopleHaveHeardOf + ". Using " +
         somethingYouDidntInvent + ", the \n" + dependentVariable + " was measured to be " +
         number + " +/- " + number2 + "\n" + units + ". " +
         "Results show " + sexyAdjective + " agreement with \ntheoretical predictions and significant improvement over \nprevious efforts by " +
         scientistThatScoopsYourLabConstantly + " et al. The work presented \nhere has profound implications for future studies of \n" +
         buzzword + " and may one day help solve the problem of \n" + supremeSocialogicalConcern + ". \n\n\n"

         "Keywords: " + buzzword2 + ", " +  buzzword3 + ", " +  buzzword4
        )

print (story)

madlib = open(teamName + "_madlib.txt", "w")
madlib.write(story)
madlib.close()
