def ReverseString(text):
    text_list = list(text)
    text_list.reverse()
    reverse_text = ''.join(text_list)
    return reverse_text
    
while True:
    print(ReverseString(input('Plz Enter Text :')))