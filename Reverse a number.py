def Reverse(number):
    r_reverse = 0
    while number > 0 :
        Reminder = number % 10
        r_reverse = ( r_reverse * 10 ) + Reminder
        number = number//10
    return r_reverse

while True:
    print(Reverse(int(input('Plz Enter Number:'))))
