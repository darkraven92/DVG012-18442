"""
Skriv ett program där användaren skriver in ett antal heltal på en rad.
Heltalen ska sparas i en lista och skrivas ut.
Använd sedan funktioner och metoder på en lista för att skriva ut:
listan i omvänd ordning
listan i storleksordning
antalet element i listan
minsta och största elementet i listan

Skriv ut summan och medelvärdet av heltalen i listan. Medelvärdet ska skrivas ut med 2 decimaler.

Krav: Använd f-strängar vid utskrifterna.

Tänk på att använda en och samma lista i hela programmet, dvs skapa inte flera listor.


Exempel på en körning

Ange heltal: 7 3 1 10                             
Inmatade tal som lista: [7, 3, 1, 10]             
Listan i omvänd ordning: [10, 1, 3, 7]            
Sorterad lista: [1, 3, 7, 10]                     
Listan har 4 element                              
Minsta talet i lista är 1 och största talet är 10 
Summan av talen är 21 och medelvärdet är 5.25     


Exempel på en annan körning

Skriv in tal: 7 9 8 3 14 2                        
Inmatade tal som lista: [7, 9, 8, 3, 14, 2]       
Listan i omvänd ordning: [2, 14, 3, 8, 9, 7]      
Sorterad lista: [2, 3, 7, 8, 9, 14]               
Listan har 6 element                              
Minsta talet i lista är 2 och största talet är 14 
Summan av talen är 43 och medelvärdet är 7.17
"""



heltal = input('Ange heltal: ')
lista = heltal.split()

for i in range(0, len(lista)):
    lista[i] = int(lista[i])
    
print(f'Inmatade tal som lista: {lista}')

lista.reverse()
print(f'Lista i omvänd ordning: {lista}')

lista.sort()
print(f'Sorterad lista: {lista}')

print(f'Listan har {len(lista)} element')

print(f'Minsta talet i listan är {min(lista)} och största talet är {max(lista)}')

summa = sum(lista)
medel = summa / len(lista)

print(f'Summan av talen är {summa} och medelvärdet är {medel:.2f}')