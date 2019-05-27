# Random guessing game, terminal user interface game
# Created by Adrian Patterson, May 2019

import random       # importing random for generating random number, time to keep track of time, and numpy/math for math stuff
import time 
import numpy
import math 





def guessevaluator(userinput):          # function to evaluate user guesses

    if int(userinput) not in range(1,100):              # checks if userinput in range of randomly generated number
        print("Error: Number not in range of 0-100.")
        return False

    if int(userinput)==randomint:           # returns true if guess correct
        return True

    if abs(int(userinput)-randomint)<5:     # notifies user if they're close
        print("Very Warm!")
        return False
        
    if int(userinput)<randomint:            # notifies user if too low
        print("Too low.")
        return False

    if int(userinput)>randomint:            # notifies user if too high
        print("Too High.")
        return False




def highscoredisplay(userscore):        # function to display high scores when game is over

    highscores = open(r"C:\Users\patte\Documents\My Projects\python fun\Random\Random\HighScores.txt","r")  # using filestream to open txt with scores
    scores = []                 # temporary array declared, will be used to display scores
         # temp integer which will be used to track which spot the user is at 
    
    for i in highscores:                # i.e. for each line in txt file, add the float to our array, "scores"
        scores.append(float(i))

    scores.sort()                       # sort the scores in ascending order
    print("\n\n\n\tHIGH SCORES: \n")        # display of scores

    scorecount=1                        # when the scorecount is equal to user's guess, their according placing is set.
    highscore_placing = 0 

    for i in scores:                    # for loop to display all high scores
        
        if(userscore==float(i)):            # little if function that'll set the user's placing, if the value in high scores == the user score
            highscore_placing = scorecount      # userscore is passed to the function to determine the placing. Then their placing is set acordingly

        print("\t\t", end='')           
        print(scorecount,end=')\t')     # two tabs, and then the placing number (scorecount)
        print(i)                        # prints the array element (for i in array)
        scorecount+=1                   # scorecount++
    
    print("\n\t\t\tYou placed number",highscore_placing,"on the leader-boards!")    # once the highscore placing is set, then it is displayed after

    if(highscore_placing==1):
        print("\t\t\tCONGRADULATIONS!!!! NEW HIGH SCORE\a")             # just a little if /elseif (elif) block that will give a user a judgement depending on their placing.
    elif(highscore_placing<=10):
        print("\t\t\tTop Ten. Not bad! Almost top dog.")
    elif(highscore_placing>10):
        print("\t\t\tMeh... Pretty weak.")
    elif(highscore_placing>20):
        print("\t\t\tYikes... work on it bud.")
    elif(highscore_placing>40):
        print("\t\t\tYeah, I'd get ahead and just quit now. Thanks for playing though!")
    

    
    highscores.close()          # closes the txt file with the scores

    











while True:             # while block to loop until user wants to stop playing


        guesscounter = 0        # counter for guesses
        randomint= numpy.random.randint(0,100)          # our randomly generated int between 0 and 100

        print("\n\t\t\tWelcome to the Guessing Game!\n\t\t\tA random value has been chosen from 1-100.\
            \n\t\t\tEnter your guesses! \n\t\t\tTimer will begin once first guess is entered. Good luck.")

        input("\n\t\t\tPress enter to begin.\n")        # just intro shiz

        start = time.time()     # start time declared after user presses enter

        while True:     # second while block for successive guesses from user

            

            guess = input("Guess: ")     # little tab and then the user inputs their guess.
            print()                         # newline

            if guess.lower() == "exit":         # if user enters exit, then 
                break   
  
            try:        # try/except block to see if value is integer

                value = int(guess)     # tries to take integer value of guess. If not possible, then go to except

            except ValueError:          # catches the value conversion error, and executes except block
                print("Sorry! Not a valid integer. Try again.\n")       # error message, then continue back to start of while block
                continue

            if guessevaluator(str(guess)) == False:     # sends guess to evaluator function, if false then print incorrect and increment guesscount
                print("Incorrect! Try again.\n")
                guesscounter+=1
                continue    # continue back to start of while
                
            else:           # if it returns true, then this statement will execute
                end = time.time()           # end time is marked, and total time taken is calculated
                totaltime = end - start
                guesscounter+=1             # final increment
                print("\n\n\t\t    Solved! you finally got it. \
                    \n\n\t\t\tCongradulations! \
                    \n\n\tSTATS: \n\n\t\t",                                 # basically displays a bunch of fun facts about the user's score
                    u'\u2022',"Time taken to solve:",totaltime,
                    "\n\t\t",u'\u2022',"Total attemps:",guesscounter,
                    "\n\n\t\tIn the time you played this game:\n\n\t\t\t",u'\u2022', int(4*totaltime),
                        "people were born.\n\t\t\t", u'\u2022',int(2*totaltime),
                        "people have died.",
                        "\n\n\t\t\t", u'\u2022',"The Earth has traveled", round((30*totaltime),3),"meters, or ",round(((30*totaltime)/1000),3), "kilometers around the sun."
                            "\n\t\t\t",u'\u2022',"Our Solar System has traveled",int(200*totaltime),"kilometers around the Milky Way."
                                "\n\t\t\t",u'\u2022',"The Milky Way has traveled",int(630*totaltime),"kilometers, into the dark unknown of our unexplored universe.",
                            "\n\n\t\t\tNow that's a long distance to travel... rest up traveler, and try to beat your high score!"
                        )
                
                highscores = open(r"C:\Users\patte\Documents\My Projects\python fun\Random\Random\HighScores.txt","a+") # opens file in "a+" mode, which means appending it
                highscores.write("\n"+str(round(totaltime,2)))      # writes to file the user's total time, rounded to two decimal places
                highscores.close()      #closes file

                highscoredisplay(round(totaltime,2))        # then, function is called to display the high score


                break           # and we're done


       
            
        command = input("\n\tEnter 'exit' if done. Enter 'again' to play again.\n\t")       # is user done playing?
        if(command=="exit"):
            break


print("""\n\n\t\t\t\tThank you for playing the guessing game!       
                \n\t\t\t\tCreated by: Adrian Patterson\n\n
            """)            # if done, then we print a final statement

            # The End!

