"""Gör en enkel miniräknare där programmet frågar om första operanden, sedan operatorn och sist andra operanden.
Operanderna ska vara heltal.
Operatorn kan vara +, -, *,/ (dvs de 4 räknesätten) och  %, // (dvs modulus och heltalsdivision).

Sedan ska programmet visa resultatet och fråga om en ny beräkning ska göras.
Den frågan ska man kunna svar antingen j för Ja eller n för nej.
Exempel på en körning
Ange operand: 3                       
Ange räknesätt: +                     
Ange operand: 2                       
Svar: 3 + 2 = 5                       
                                      
Vill du göra en ny beräkning (j/n)? j 
Ange operand: 3                       
Ange räknesätt: %                     
Ange operand: 2                       
Svar: 3 % 2 = 1                       
                                      
Vill du göra en ny beräkning (j/n)? j 
Ange operand: -5                      
Ange räknesätt: +                     
Ange operand: 3                       
Svar: -5 + 3 = -2                     
                                      
Vill du göra en ny beräkning (j/n)? n 
Programmet avslutas!                  
Hantera på ett snyggt sätt, utan att avbryta programmet, om felaktigt räknesätt anges.
Hantera på ett snyggt sätt, så att programmet inte kraschar vid division/heltalsdivision/modulus med 0 
och utan att avbryta programmet.
Krav: Använd f-strängar för utskrifter. För er som programmerat tidigare, inga break, continue, pass eller exit satser får 
användas.
Använd beskrivande variabelnamn.
Använd 4 mellanslag som indentering, vilket rekommenderas i Python.
"""
aktiv = True
while aktiv:
    operand1 = int(input('Ange operand: '))
    operator = input('Ange räknesätt: ')
    operand2 = int(input('Ange operand: '))

    if operator == '+':
        resultat = operand1 + operand2
        print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
    elif operator == '-':
        resultat = operand1 - operand2
        print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
    elif operator == '*':
        resultat = operand1 * operand2
        print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
    elif operator == '/':
        if  operand2 != 0:
            resultat = operand1 / operand2
            print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
        else:
            print('Fel: Division med 0')      
    elif operator == '%':
        if  operand2 != 0:
            resultat = operand1 % operand2
            print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
        else:
            print('Fel: Modulus med 0')
    elif operator == '//':
        if  operand2 != 0:
            resultat = operand1 // operand2
            print(f'Svar: {operand1} {operator} {operand2} = {resultat}')
        else:
            print('Fel: Heltalsdivision med 0')
    else:
        print('Ogilitig operator')
    print()
    avsluta_program = input('Vill du göra en ny beräkning (j/n)? ')
    if avsluta_program == "n":
        aktiv = False
print('Programmet avslutas!')