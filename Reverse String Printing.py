def ReverseString(Text):
    Reverse = list(Text)
    Reverse.reverse()
    Reverse_Text = ''.join(Reverse)
    return Reverse_Text
    
while True:
    print(ReverseString(input('Plz Enter Text :')))