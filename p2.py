import operator
foods={}

foods["yogur"] = 8

#print(foods)
#print(foods["yogur"])

ingredients = {}
ingredients["sandwich"] = "bread", "lettuce", "tomato", "bacon"

#print (ingredients)

sandwich=[]

if "sandwich" in ingredients:
    sandwich.append(ingredients["sandwich"])
else:
    print ("Mierda. Esto no va asi")

#print (sandwich)

logs = []

linea1={"response": "280", "date":"2010/10/20", "weigth":216}
logs.append(linea1)
linea2={"response": "200", "date":"2011/03/30", "weigth":128}
logs.append(linea2)

#linea1={"response": "280", "date":"2010/10/20", "weigth":216}
logs.append({"response": "280", "date":"2010/10/20", "weigth":216})
#linea2={"response": "200", "date":"2011/03/30", "weigth":128}
logs.append({"response": "200", "date":"2011/03/30", "weigth":128})

for lista in logs:
    print("Respuesta", lista["response"] , "Fecha", lista["date"], "Peso", lista["weigth"])

mi_tupla=(28,1,87,12,9,89,54,43,21,9,23)

a = 0
for i in mi_tupla:
    if i > 50:
	a = a + 1
	print(i)
print ("Numero de registros: ", a)

mi_lista=list(mi_tupla)
mi_lista.sort()
a = 0
for i in mi_lista:
    a = a + 1
    print(i)
print ("Numero de registros: ", a)

europe = []
germany = {"name": "Germany", "population": 81000000, "price":1000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000, "price":2000}
europe.append(luxembourg)
europe.append({"name": "Francia", "population": 23000000, "price":3000})
europe.append({"name": "Andorra", "population": 175000, "price":4000})
europe.append({"name": "Italia", "population": 10000000, "price":5000})

europe2 = europe[:]
for lista in europe2:
    if lista["population"] < 200000 and lista["name"].find("A")==0:
	print ("Pais:", lista["name"], "Población:", lista["population"])
    else:
	europe.remove(lista)

for lista in europe:
    print(lista)

for lista in europe2:
    lista["price"] = lista["price"]*1.25

for lista in europe2:
    print(lista)
