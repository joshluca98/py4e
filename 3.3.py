try:
    user_score = float(input("Enter a score between 0.0 and 1.0: "))
except:
    print("Invalid Score")
    quit()

if user_score>=0.0 and user_score<1.0:
    if user_score>=0.9:
        print("A")
    elif user_score>=0.8:
        print("B")
    elif user_score>=0.7:
        print("C")
    elif user_score>=0.6:
        print("D")
    elif user_score<0.6:
        print("F")
