import sys

try:
    f = open("meses.txt")
except IOError as e:
    print(e)
    print ("IOError {0}  {1}".format(e.errno, e.strerror))
    
print(f.read())
f.close()

f = open("meses.txt")
next = f.read(1)
a = 1
while next != "":
    print(next)
    next = f.read(1)
    a = a + 1
print "Numero de caracteres: ", a
f.close()
    
f = open("meses.txt")
for month in f.readlines():
    valor = len(month.strip())
    print("Month " + month.strip() + "  Caracteres: " + str(valor))
f.close()