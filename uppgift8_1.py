

tal1 = int(input('Skriv in tal 1: '))
tal2 = int(input('Skriv in tal 2: '))
tal3 = int(input('Skriv in tal 3: '))

def print_max(tal1, tal2, tal3):
    if tal1 >= tal2 and tal1 >= tal3:
        print(f'Det största talet är {tal1}')
    elif tal2 >= tal1 and tal2 >= tal3:
        print(f'Det största talet är {tal2}')
    elif tal3 >= tal2 and tal3 >= tal1:
        print(f'Det största talet är {tal3}')
print_max(tal1,tal2,tal3)
        