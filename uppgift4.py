"""Skriv ett program som läser in positiva heltal tills 0 läses in
Ange ett positivt heltal:              

Beräkna summan av alla inmatade heltal.
Skriv ut summan.
Summan av de inmatade heltalen är:              

Efter summan skrivits ut, fråga användaren om de vill beräkna en summa till och om användaren svarar j ska inmatningen av positiva heltal börja om.
Vill du beräkna en summa till (j/n)?  

När användaren svarar n ska programmet avslutas med utskriften
Programmet avslutas!

Om användaren skriver in negativa tal ska de inte tas med i summan och en felutskrift skrivs ut (se den andra exempelkörningen).

Negativa tal inkluderas inte i summan! 

-Sista raden i utskriften är Programmet avslutas! och koden som utför den utskriften ska ligga sist i programmet 
och inte i någon repetitionssats eller if-sats.
-Använd inte listor/arrayer och inte break/continue/pass/exit (du som inte programmerat tidigare vet ännu inte vad det är).
-Använd inte AI-genererad kod (ofta inte så bra) med try-except och funktioner (vi lär oss om båda senare, hur de används på 
korrekt sätt).
-Använd beskrivande variabelnamn.
-Använd 4 mellanslag som indentering, vilket rekommenderas i Python.
-Tänk på att uppgiften ska lösas utan att samma/liknande kod upprepas flera gånger. 
Repetitionssatser används ju för att slippa upprepa samma kod flera gånger.


Extra utmaning, inte obligatorisk:
Beräkna medelvärdet också och skriv ut det tillsammans med summan. Nollan inte skulle räknas med i beräkningen av medelvärdet, 
utan ska bara som en markör för att avsluta. Fundera/testa vad som händer om användaren skriver in en nolla som första tal.

"""





summa = 0
active = True
while active:
    heltal = int(input('Ange ett positivt heltal: '))
    if heltal < 0:
        print('Negativa tal inkluderas inte i summan')
    elif heltal == 0:
        print(f'Summan av de inmatade heltalen: {summa}')
        avsluta_program = input('Vill du beräklna en summa till (j/n): ')
        if avsluta_program == "n":
            active = False
        elif avsluta_program == "j":
            summa = 0
    elif heltal > 0:
        summa = summa + heltal
print('Programmet avslutas!')