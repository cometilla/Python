palabraacifrar = input("Palabra a cifrar: ")
clave = int(input("Clave de cifrado: "))

palabracifrada = ""
for caracter in palabraacifrar:
    ordinal = ord(caracter)+clave
    if ordinal > 122:
        ordinal = ordinal - 122 + 64
    caracter = chr(ordinal)
    palabracifrada = palabracifrada+caracter
    
print ("Palabra cifrada: " + palabracifrada)

palabraacifrar = ""

for caracter in palabracifrada:
    ordinal = ord(caracter)-clave
    if ordinal < 65:
        ordinal = ordinal + 122 - 64
    caracter = chr(ordinal)
    palabraacifrar = palabraacifrar+caracter
        
print ("Palabra descifrada: " + palabraacifrar)
        