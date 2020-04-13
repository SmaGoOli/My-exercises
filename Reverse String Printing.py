def ReverseString(text):
    text_list = list(text)
    text_list.reverse()
    text_reverse = ''.join(text_list)
    return text_reverse
    
while True:
    print(ReverseString(input('Plz Enter Text :')))
