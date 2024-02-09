score = 0
goAgain = "y"

petscore = []

#max amount of points is 400, min is 132, prob rn is getting middle group as a result
def scoreAdder(currentScore, questionStrength):
    if(questionStrength == "str"):
        currentScore += 100
        petscore.append(currentScore)
        return currentScore
    elif(questionStrength == "med"):
        currentScore += 75
        petscore.append(currentScore)
        return currentScore
        
    elif(questionStrength == "weak"):
        currentScore += 33
        petscore.append(currentScore)
        return currentScore
    else:
        print("Wat")

def questionsForAnimal(goAgain,score):
    while(goAgain == "y"):
        print("Answer the questions with y/n \nAnything else may cause an error\n\n")

        questionAns = input("Do you have a very busy schedule? Answer y or n.")
        if questionAns == "n":
            scoreAdder(score, "weak")
        if questionAns == "y":
            scoreAdder(score, "str")
        
        questionAns = input("Do you like exotic pets? Answer y or n")
        if questionAns == "n":
            scoreAdder(score, "str")
        if questionAns == "y":
            scoreAdder(score, "weak")

        questionAns = input("Are you willing and able to care for a high maintenance pet? y/n")
        if questionAns == "n":
            scoreAdder(score, "str")
        if questionAns == "y":
            scoreAdder(score, "weak")

        questionAns = input("Do you live in an average weather climate? y/n")
        if questionAns == "n":
            scoreAdder(score, "str")
        if questionAns == "y":
            scoreAdder(score, "weak")
            
        if sum(petscore) >= 300:
            print("The pet that is best for you is a: goldfish, hamster, guinea pig")
        elif sum(petscore) <= 132:
            print("The best pets for you are: parrot, snake, ferret") 
        else:
            print("The best pets for you are: dog, cat, turtle")   
        
        goAgain = input("Go again? y/n")  
