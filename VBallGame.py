#volleyball game. This program detemines the final winner according to the given current points. 

def game():

    summ = 0.0
    sumj = 0.0

    while not ( ((summ >= 10 or sumj >= 10) and abs (summ - sumj) > 2) or (summ ==7 and sumj == 0) or (sumj ==7 and summ == 0)):

        #This is below line return non-cummulative score as requested by the instructor.


        summ = float(input("what is Mary's point?\n"))
        sumj = float(input("what is Jake's point?\n"))
        print ("Mary's point is",summ,"and Jake's point is", sumj)

        
        ####Comment out### if you want to get the final score of the Winner consistent of all given scores.

        #m = float(input("what is Mary's point?\n"))
        #j = float(input("what is Jake's point?\n"))
        #print ("Mary's point is",m,"and Jake's point is", j)
        #summ += m
        #sumj += j
 
        if summ > sumj and (not (((summ >= 10 or sumj >= 10) and abs (summ - sumj) > 2) or (summ ==7 and sumj == 0) or (sumj ==7 and summ == 0))):
           print ("For now, Mary is ahead with a sum points of", summ, "\n")
        elif sumj > summ and (not (((summ >= 10 or sumj >= 10) and abs (summ - sumj) > 2) or (summ ==7 and sumj == 0) or (sumj ==7 and summ == 0))):
           print ("For now, Jake is ahead with a sum points of", sumj, "\n")
        
    if summ > sumj:
        print ("The final Winner is 'Mary' with the final point of beating Jake ", summ, "to ", sumj)
    elif summ < sumj:
        print ("The final Winner is 'Jake' with the final point of beating Mary ", sumj, "to ", summ)

game()
