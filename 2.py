import csv


with open('game.csv', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=';'))[1:]

    for i in range(len(data)):
        temp=data[i]
        j=i-1
        temp[2]=temp[2] if temp[2]!='None' else 0
        while j>=0 and int(data[j+1][4])>int(data[j][4]):
            data[j+1],data[j]=data[j],data[j+1]
            j-=1

    for stroka in data[1:]:
        print(f'{stroka[0]} - количесво багов: {})
