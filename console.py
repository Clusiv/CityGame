a = input()
b = input()

def citycheck(city1, city2):
    if city1[-1] in 'ьъы':
        if city1[-2] == city2[0].lower():
            return True
        else:
            return False
    else:
        if city1[-1] == city2[0].lower():
            return True
        else:
            return False

while True:
    if citycheck(a,b):
        a = b
        b = input('Введите следующий город: ')
    else:
        b = input('Введен не правильный город, повторите: ')
