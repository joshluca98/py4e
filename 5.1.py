count = 0
total = 0.0

while True:
    raw_input = input("Enter number:")
    try:
        converted_input = float(raw_input)
    except:
        if raw_input == 'done':
            break
        else:
            print('(!) Please enter a numerical value. (!)')
            continue
    count = count + 1
    total = total + converted_input
    average = total/count

print("Total is:",total)
print("Count is:",count)
try:
    print("Average is:",average)
except:
    print("Average is: 0.0")

print("All done.")
