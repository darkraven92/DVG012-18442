"""Skriv ett program som skriver ut en snygg multiplikationstabell.
Användaren ska välja vilken tabell som ska skrivas ut och vilka mellan vilket intervall tabellen ska visa.

Använd en loop för beräkningen och f-strängar för att få en snygg tabell.

Programmets utskrifter ska se exakt ut som vid exempelkörningarna nedan, dvs raka högermarginaler på utskrifterna.

Använd for-loopen vid utskrift av tabellen.

Efter tabellen skrivits ut, fråga användaren om de vill avsluta Vill du avsluta (j/n)?
och programmet avslutas om användaren svarar j. Om användaren svarar n ska användaren användaren tillfrågas om 
tabell och intervaller.

Använd inte break, continue, pass eller exit.
Använd inte AI-genererad kod (ofta inte så bra) med try-except och funktioner (vi lär oss om båda senare, 
hur de används på korrekt sätt).
Använd beskrivande variabelnamn.
Använd 4 mellanslag som indentering, vilket rekommenderas i Python.

 

*Inte obligatoriskt, men för de som vill ha en extra utmaning:
*Om annat svar än j eller n ska texten 'felaktigt svar' skrivas och frågan Vill du avsluta (j/n)?  visas igen.
*Ska fungera även om J skrivs in istället för j och om N skrivs in istället för n. """

resultat = 0
aktiv = True
while aktiv:
    tabell = int(input('Ange tabell: '))
    start_intervall = int(input('Ange startintervall: '))
    stop_intervall = int(input('Ange stoppintervall: '))
    print('----------------------')
    print(f'{tabell}:ans tabell')
    print('----------------------')
    for i in range(start_intervall, stop_intervall + 1):
        print(f'{i:3} * {tabell:1} = {i * tabell:5}')
    avsluta_program = input('Vill du avsluta (j/n)? ')
    if avsluta_program == 'j':
        aktiv = False
print('Programmet avslutas!')
