
# Funktion som hanterar användarfel. 
def fel_hantering(operand2, operator):
    # Hantering av division med 0
    if operand2 == 0 and operator in ['/','%', '//']:
        return f'Fel: Division med 0'
    # Hantering om använder skriver in en annan operator än en giltig
    if operator not in ['+', '-', '*', '/', '%', '//']:
        return f'Felaktig operator'

# Utför uträkningar baserat på operander och operator 
def beräkna(operand1, operator, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1*operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '%':
        return operand1 % operand2
    elif operator == '//':
        return operand1 // operand2

aktiv = True
while aktiv:
    uträckning = input('Vad vill du räkna: ')
    
    # Delar upp uträckning
    operand1, operator, operand2 = uträckning.split()
    
    # Konverterar operand1 och operand2 till float
    operand1 = float(operand1)
    operand2 = float(operand2)

    # Eventuellt fel tilldelas i variabel fel_meddelande
    fel_meddelande = fel_hantering(operand2, operator)

    # Om fel har tilldelas i fel_medddelande skrivs det ut
    if fel_meddelande:
        print(f'{fel_meddelande}')
    else:
        # Anropar funktionen beräkna
        beräkna(operand1, operator, operand2)
        # Skriver ut uträkningen
        print(f'{operand1} {operator} {operand2} = {beräkna(operand1, operator, operand2)}')   