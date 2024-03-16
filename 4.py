import csv


def search(name, data):
    k = 0
    for stroka in data:
        if name == stroka[1]:
            k += 1
            return k


with open('game.csv', encoding='utf-8') as f, open('game_counter.csv', 'w', encoding='utf-8', newline='') as nf:
    data = list(csv.reader(f, delimiter=';'))
    res = csv.writer(nf, delimiter=';')

    data[0].append('Errors count')
    res.writerow(data[0])
    for stroka in data[1:]:
        game_name = stroka[0]
        h = search(game_name,data)
        stroka.append(h)
        res.writerow(stroka)
