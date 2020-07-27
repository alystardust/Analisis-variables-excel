import pandas as pd

def isNaN(num):
    return num != num

df = pd.read_csv("data/obs.csv", sep=";", skip_blank_lines=False)

print(df)

conjunto = [];

#emepiza en fila 0 columna 0
for fila, columna in df.iterrows():



    if not (isNaN(columna[0])):

        str = columna[0].replace(' ', '').split(',')

        for i in str:
            if not (i in conjunto):
                conjunto.append(i)




print(conjunto)


listageneral = []

for fila, columna in df.iterrows():

    listabool = []

    if not (isNaN(columna[0])):
        str = columna[0].replace(' ', '').split(',')

        for i in conjunto:
            if i in str:
                listabool.append(1)
            else:
                listabool.append(0)
    else:
        for i in conjunto:
            listabool.append(0)





    listageneral.append(listabool)


import csv

with open('obs_.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(conjunto)

    for i in listageneral:
        writer.writerow(i)

#end
