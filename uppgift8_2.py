"""
Koden på https://repl.it/@MatteMedPython/Finn-Fem-Fel Links to an external site.

Finn-Fem-Fel
Run Python code live in your browser. Write and run code in 50+ languages online with Replit, a powerful IDE, compiler, & interpreter.
repl.it
har ett antal fel, s.k. buggar.
Kopiera koden till din repl.it och rätta buggarna.
När du försöker exekvera (köra) programmet kommer du i turordning få följande fel. Åtgärda dem en i taget. Lämna sedan in länken till den rättade koden i repl.it
Fel 1 - syntaxfel
Fel 2 - syntaxfel
Fel 3 - syntaxfel
Fel 4 - logiskt fel. Inget felmeddelande, men antalet 6:or skrivs inte ut.
Fel 5 - logiskt fel. Ibland stämmer inte antalet önskade kast överens med antal summerade kast. 
 
När allting fungerar kan utskriften se ut som nedan. Alla tärningskast visas 1 - 6 och de summerade tärningskasten är lika många tärningskast som användaren vill göra. Kontrollera genom att ange minst 1000 kast.
Hur många tärningskast vill du göra? 1000   
Medelvärdet av tärningskasten är: 3.40      
Antal 1:or = 193                            
Antal 2:or = 166                            
Antal 3:or = 149                            
Antal 4:or = 176                            
Antal 5:or = 173                            
Antal 6:or = 143                            
Totalt antal summerade tärningskast är 1000 
 
Här kommer koden till Finn Fem Fel
from random import randint


# Funktion som slumpar fram ett antal kast till en lista
def slumpa_tärningskast_till_lista(antal_kast, lista):
    for i in range(antal_kast):
        tärningskast = randint(1, 7)
        lista.append(tärningskast)

        
# Funktion som beräknar medelvärdet på tal i en lista
def beräkna_medelvärde(lista)
    summa = 0
    for element in lista:
        summa = summa + element
    medelvärde = summa / len(lista)
    return medelvärde


# Fråga användaren om indata
antal_kast = int(input('Hur många tärningskast vill du göra? '))

# Skapa en tom lista
lista = lista.clear()

# Anropa funktionen som slumpar fram tärningskast till en lista
slumpa_tärningskast_till_lista(antal_kast, lista)

# Anropa funktionen som beräknar medelvärdet för elementen i en lista
medel_värde = beräkna_medelvärde(lista)
# Skriv ut medelvärdet
print(f'Medelvärdet av tärningskasten är: {medelvärde:.2f}')

# Skriv ut en frekvenstabell
summa_tärningskast = 0
for i in range(1, 6):
    antal = lista.count(i)
    summa_tärningskast += antal
    print(f'Antal {i}:or = {antal}')  

print(f'Totalt antal summerade tärningskast är {summa_tärningskast}')
"""


from random import randint

# Funktion som slumpar fram ett antal kast till en lista
def slumpa_tärningskast_till_lista(antal_kast, lista):
    for i in range(antal_kast):
        tärningskast = randint(1, 6)
        lista.append(tärningskast)


# Funktion som beräknar medelvärdet på tal i en lista
def beräkna_medelvärde(lista):
    summa = 0
    for element in lista:
        summa = summa + element
    medelvärde = summa / len(lista)
    return medelvärde


# Fråga användaren om indata
antal_kast = int(input('Hur många tärningskast vill du göra? '))


# Skapa en tom lista
lista = []

# Anropa funktionen som slumpar fram tärningskast till en lista
slumpa_tärningskast_till_lista(antal_kast, lista)

# Anropa funktionen som beräknar medelvärdet för elementen i en lista
medel_värde = beräkna_medelvärde(lista)
# Skriv ut medelvärdet
print(f'Medelvärdet av tärningskasten är: {medel_värde:.2f}')

# Skriv ut en frekvenstabell
summa_tärningskast = 0
for i in range(1, 7):
    antal = lista.count(i)
    summa_tärningskast += antal
    print(f'Antal {i}:or = {antal}')  

print(f'Totalt antal summerade tärningskast är {summa_tärningskast}')