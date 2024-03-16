import csv

#пишем те символы, которые используются в названии игр
alf = sorted("'.:-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
d = {alf[i]: i + 1 for i in range(len(alf))}


#пишем функцию составления хеша
def hash(s):
    s = s.replace(' ', '')
    p = 65
    m = 10 ** 9 + 9
    hash_value = 0
    i = 0
    for c in s:
        hash_value += d[c] * p ** i
        i += 1
    return int(hash_value % m)

#ткрываем файл и создаем новый
with open('game.csv', encoding='utf-8') as f, open('game_with_hash.csv', 'w', encoding='utf-8', newline='') as nf:
    data = list(csv.reader(f, delimiter=';'))
    res = csv.writer(nf, delimiter=';')

    #добавляем столбец hash  вписываем туда хеш
    data[0].append('hash')
    res.writerow(data[0])
    for stroka in data[1:]:
        game = stroka[0]
        name = stroka[1]
        s = game + name
        h = hash(s)
        stroka.append(h)
        res.writerow(stroka)
