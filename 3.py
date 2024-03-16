import csv

#ищем, есть ли имя в строке, если есть, возвращаем строку
def search(name, data):
    for stroka in data:
        if name == stroka[1]:
            return stroka
    return None

#открываем файл
with open('game.csv', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=';'))

    m = 1
    name = input()
    #проверяем, сть ли такой персонаж
    while name != 'game':
        res = search(name, data)
        if res is None:
            print('Этого персонажа не существует')
        else:
            print(f'Персонаж {res[1]} встречается в играх:')
            #если есть выводим 5 первых игр, где он встречается
            for stroka in data[1:]:
                if stroka[1] == name:
                    print(stroka[0])
                    m += 1
                    if m == 6:
                        break
        name = input()
