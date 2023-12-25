list_id = []

while True:
    flagAlpha = False
    flagDigit = False
    ID = input('задайте идентификатор')
    if ID == 'stop':
        break
    elif ID == 'getIdn':
        print(list_id)
    else:
        if len(ID) < 10:
            print('Идентификатор должен быть не менее 10 символов!')
        elif ID[0] != "$":
            print('Идентификатор должен начинаться с символа $')
        for i in ID:
            if i.isalpha():
                flagAlpha = True
            elif i.isdigit():
                flagDigit = True
        if flagAlpha == False:
            print('в идентификаторе должна быть хотя бы одна буква!')
        elif flagDigit == False:
            print('в идентификаторе должна быть хотя бы одна цифра!')
        elif list_id.count(ID):
            print('идентификатор должен быть уникальным!')
        else:
            list_id.append(ID)









