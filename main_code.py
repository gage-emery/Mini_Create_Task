score = 0
goAgain = "y"

def scoreAdder(currentScore, questionStrength):
    if(questionStrength == "str"):
        currentScore += 200
        return currentScore
    elif(questionStrength == "med"):
        currentScore += 100
        return currentScore
    elif(questionStrength == "weak"):
        currentScore += 50
        return currentScore
    else:
        print("Wat")

def questionsForAnimal(goAgain,score):
    while(goAgain == "y"):
        print("Answer the questions with y/n \nAnything else may cause an error\n\n")
        
        questionAns = ""
        questionAns = input("Do you like exotic pets? (y/n)")

        questionAns = input("Do you have a very busy schedule? Answer y or n.")
        
        questionAns = input("Do you like exotic pets? Answer y ot n")
        if questionAns == "y":
            scoreAdder(score,"weak")

        if questionAns == "n":
            scoreAdder(score,"med")

        questionAns = input("if you would like a high maitnence pet answer y, if you would like a low maitnence pet answer n.")
        if questionAns == "y":
            scoreAdder(score,"weak")

        if questionAns == "n":
            scoreAdder(score,"str")

        questionAns = input("Do you live in a warmer climate? answer y. Do you live in a colder climate? answer n")
        if questionAns == "y":
            scoreAdder(score,"weak")

        if questionAns == "n": 
            scoreAdder(score,"str")
