import operator

europe = []
germany = {"name": "Germany", "population": 81000000, "price":1000}
europe.append(germany)
luxembourg = {"name": "Luxembourg", "population": 512000, "price":2000}
europe.append(luxembourg)
europe.append({"name": "Francia", "population": 23000000, "price":3000})
europe.append({"name": "Andorra", "population": 175000, "price":4000})
europe.append({"name": "Italia", "population": 10000000, "price":5000})

europe2 = europe[:]

europe2.sort(key=operator.itemgetter("name"))

for lista in europe2:
    print(lista)