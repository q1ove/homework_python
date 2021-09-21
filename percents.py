import string
str_='ddd'
def percents(str_):
    uppers = 0
    lowers = 0
    for i in str_:
        if i.isalpha():
            if i.islower():
                lowers += 1
            else:
                uppers += 1
    summa = uppers + lowers
    procenty_zaglav = (100//summa) * uppers
    return {'заглавные':procenty_zaglav,'строчные':100-procenty_zaglav};
print(percents(str_))
