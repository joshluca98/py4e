def computegrade(user_score):
    if user_score>=0.0 and user_score<1.0:
        if user_score>=0.9:
            grade="A"
        elif user_score>=0.8:
            grade="B"
        elif user_score>=0.7:
            grade="C"
        elif user_score>=0.6:
            grade="D"
        elif user_score<0.6:
            grade="F"
    return grade

try:
    print(computegrade(float(input("Enter a score between 0.0 and 1.0: "))))
except:
    print("Invalid Score")
    quit()
