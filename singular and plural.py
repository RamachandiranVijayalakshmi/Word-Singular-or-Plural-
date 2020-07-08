def word(word):
    if word[-1].lower()=='s':
        print(word,'is a plural word')
    else:
        print(word,'is a singular word')
a=str(input('Enter the word:'))
word(a)