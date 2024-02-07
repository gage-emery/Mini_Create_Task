score = 0
goAgain = "y"

petscore = []

def scoreAdder(currentScore, questionStrength):
    if(questionStrength == "str"):
        currentScore += 200
        return currentScore
    elif(questionStrength == "med"):
        currentScore += 100
        return currentScore
    elif(questionStrength == "weak"):
        currentScore += 50
        petscore.append(currentScore)
        return petscore
        
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

        questionAns = input("If you live in a warmer climate, answer y. If you live in a colder climate, answer n.")
        if questionAns == "n":
            scoreAdder(score, "str")
        if questionAns == "y":
            scoreAdder(score, "weak")
            
        if sum(petscore) >= 700:
            print("The pet that is best for you is a: goldfish, hamster, guinea pig")
        elif sum(petscore) <= 450:
            print("The best pets for you are: parrot, snake, ferret") 
        else:
            print("The best pets for you are: dog, cat, turtle")   
        
        goAgain = input("Go again? y/n")  
