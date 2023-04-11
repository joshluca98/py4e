count = 0
total = 0.0
max = None
min = None

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

    if min == None:
        min = converted_input
    if max == None:
        max = converted_input
    if converted_input < min:
        min = converted_input
    if converted_input > max:
        max = converted_input



print("Total is:",total)
print("Count is:",count)
print("Minimum is:",min)
print("Maximum is:",max)

print("All done.")
