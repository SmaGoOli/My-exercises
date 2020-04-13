def Reverse(number):
    r_reverse = 0
    while number > 0 :
        reminder = number % 10
        r_reverse = ( r_reverse * 10 ) + reminder
        number = number//10
    return r_reverse

while True:
    print(Reverse(int(input('Plz Enter Number:'))))
