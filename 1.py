import csv

#открываем файл и создаем новый
with open('game.csv', encoding='utf-8') as f, open('game_new.csv', 'w', encoding='utf-8', newline='') as nf:
    data = list(csv.reader(f, delimiter=';'))
    res = csv.writer(nf, delimiter=';')

    error = '55'
    a = []
    #ищем людей с ошибкой 55
    for stroka in data[1:]:
        if error in stroka[2]:
            print(f'У персонажа {stroka[1]} в игре {stroka[0]} нашлась ошибка с кодом: {stroka[2]}. Дата фиксации: {stroka[3]}.')

    #заменяем ошибку 55 на Done
    res.writerow(data[0])
    for stroka in data[1:]:
        if error in stroka[2]:
            stroka[2] = stroka[2][:5]+'Done'
        res.writerow(stroka)
