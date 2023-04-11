numberList = []
while(True):
    number = input("Enter numbers: ")
    if number == "done":
        break;
    number = float(number)
    numberList.append(number)
print("Maximum:",max(numberList))
print("Minimum:",min(numberList))