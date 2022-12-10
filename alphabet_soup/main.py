def alphabetSoup(string):
    li = sorted(list(string))
    new_string = ''
    for char in li:
        new_string += char
    return new_string

def alphabetSoup_2(string):
    li = sorted(list(string))
    lowerLi = sorted(list(string.lower()))
    caps = []
    new_string = ''
    for char in li:
        if char.isupper():
            caps.append(char)
    for letter in lowerLi:
        if caps.count(letter.upper())!= 0:
            new_string += letter.upper()
            caps.pop(caps.index(letter.upper()))
        else:
            new_string += letter
    return new_string


word = input('Enter a string ')
print(alphabetSoup(word))