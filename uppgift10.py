# Funktion för att kontrollera giltig operator
def kontrollera_operator(operator):
    giltiga_operatorer = ['+','-','*','/','%','//']
    if operator not in giltiga_operatorer:
        return f'Felaktig operator'

# Funktion för att uföra uträkningen
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
    try:
        # Frågar efter ett uttryck 
        uträkning = input('Vad vill du räkna: ') 
        # Delar upp uttrycket
        operand1, operator, operand2 = uträkning.split() 
        # Konverterar till float
        operand1 = float(operand1)
        operand2 = float(operand2)

        # Eventuellt fel tilldelas i varibel
        fel_meddelande = kontrollera_operator(operator)    

        # Om fel tilldelas i variabel fel_meddelande 
        if fel_meddelande:
            print(f'{fel_meddelande}')
        else:
            print(f'{operand1} {operator} {operand2} = {beräkna(operand1, operator, operand2)}')
    # Fångar upp eventuella undantag
    except ValueError:
        print('Felaktig operand')
    except ZeroDivisionError:
        print('Fel: Division med 0')