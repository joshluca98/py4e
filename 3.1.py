hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
if hours > 40:
    print('Total Pay:', round((rate*hours)+((rate*0.5)*(hours-40)),2))
else:
    print('Total Pay:', round(rate*hours,2))





