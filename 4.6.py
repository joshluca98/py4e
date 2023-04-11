def computepay(hours, rate):
    if hours > 40:
        return(round((rate*hours)+((rate*0.5)*(hours-40)),2))
    else:
        return(round(rate*hours,2))

try:
    print("Pay", computepay(float(input('Enter Hours: ')), float(input('Enter Rate: '))))
except:
    print("Please enter numeric values (!)")
    quit()
