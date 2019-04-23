# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:01:56 2019

@author: annabel wing-yan fan 2019

citation for madblib sample: 
https://www.theodysseyonline.com/mad-libs-for-college-kids

1) Git pull
2) Change your word selections
3) Git add -A 
4) Git commit -m"Type in your name"
5) Git push

Next person!    

"""

#person 1
teamName = "TeamA"
yourCollegename = "UofT"
adjective1 = "stressed"
bodyPart = "elbows"

#person 2
Object = "cellphone"
drugName = "weed"
action = "cry"
adjective2 = "loudly"

#person 3
bodyPart2 = "lower back"
placeOnCampus = "cafeteria"
animal = "wild coon"
favoriteCurseWord = "yoinks"

#person 4
favoriteCurseWord = "yoinks"
number = "42"
kitchenAppliance = "crock pot"
nameOneOfTheKardashians = "Kim Kardashian"


#person 4 or together
#run the script!


story = ("It was the one night everybody dreads, the night before hell week starts- AKA finals week- at " + yourCollegename +". \n\n" 
         
         "The library was full of " + adjective1 + " students all glued to their books and " + bodyPart + " deep in energy drink cans and empty coffee cups. \n\n" 
         "One desperate student even had the guts to sneak in a(n) " + Object + ". \n\n" 
         "As expected, I couldn't find a decent place to sit so I had to sit next to the dude who smelled like " + drugName + ". \n\n\n" 
         
         "I began to " + action + " " + adjective2 + ". \n \n\n"
         
         "Finally, at around 5 a.m. Monday morning I started wandering back to my dorm room, \nbut my " + bodyPart2 +  " was so exhausted that I decided to crash at " + placeOnCampus + ". \n\n" 
         "I was awoken 5 hours later by a not so friendly " + animal + " who was gnawing on my notes. \n\n"
         
         "\"" + favoriteCurseWord + "! I'm late for my first final!\" I yelled.\n\n" 
         
         "I ran to class as fast as I could, but when I got there and saw no one in class, \nI realized that my first final was actually a week ago and it was not Monday at all.\n\n" 
         
         "In fact, it was Friday and not only did I miss all of my finals, but I've been going to the wrong school for " + number + " years \nand am actually a(n) " + kitchenAppliance + ".\n\n"
         "\"Oh well,\" I sighed. \"At least I'll always be smarter than "+ nameOneOfTheKardashians + ".\""

        )

print (story)

madlib = open(teamName + "_madlib.txt", "w")
madlib.write(story)
madlib.close()