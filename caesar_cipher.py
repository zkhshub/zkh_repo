code_list = ['A','B','C','D',
            'E','F','G','H',
            'I','J','K','L',
            'M','N','O','P',
            'Q','R','S','T',
            'U','V','W','X',
            'Y','Z']
plain = input('text: ').upper()
cipher = ''
for c in plain:
    if c in code_list:
        cipher += code_list[(code_list.index(c)+23) % 26]
    else:
        cipher += ' '
print(cipher)
