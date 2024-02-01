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

def questionsForAnimal(goAgain):
    while(goAgain == "y"):
        print("Answer the questions with y/n \nAnything else may cause an error\n\n")
        
        questionAns = ""
        questionAns = input("Do you like exotic pets? (y/n)")
        
