__author__ = 'Dreyke Boone'

def convert(word):
    output = ''.join(x for x in word.title() if x.isalnum())
    return output[0].lower() + output[1:]

convertString = input("Enter a string: ")
print(convert(convertString))