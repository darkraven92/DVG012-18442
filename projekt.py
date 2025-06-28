import random

def choose_tabel():
    while True:
        try:
            tabel = int(input("Ange vilken gångertabell du vill öva (2–12): "))
            if 2 <= tabel <= 12:
                return tabel
            else:
                print("Du måste välja ett tal mellan 2 och 12.")
        except ValueError:
            print("Du fick bara ange ett heltal.")

def ask_math_question(tabel, used_factors):
    while True:
        factor = random.randint(2, 12)
        if factor not in used_factors:
            used_factors.append(factor)
            correct_answer = tabel * factor
            try:
                answer = int(input(f"{tabel} * {factor} = "))
                if answer == correct_answer:
                    print("Rätt svar!")
                    return True
                else:
                    print("Fel svar! Försök igen.")
                    return False
            except ValueError:
                print("Du fick bara ange ett heltal.")
                return False

def choose_zombie_door(doors_left):
    zombie_door = random.randint(1, doors_left)
    while True:
        try:
            chosen_door = int(input(f"Välj en dörr (1–{doors_left}): "))
            if 1 <= chosen_door <= doors_left:
                if chosen_door == zombie_door:
                    print("ZOMBIES! De var bakom dörren!\nSpelet avslutas.")
                    print(f"(Zombien gömde sig bakom dörr {zombie_door})")
                    return False
                else:
                    print("Ingen zombie bakom dörren.")
                    print(f"(Zombien var bakom dörr {zombie_door})")
                    return True
            else:
                print(f"Du måste välja en dörr mellan 1 och {doors_left}.")
        except ValueError:
            print("Du fick bara ange ett heltal.")

def start_game():
    print("Välkommen till Zombiemattespelet!")
    tabel = choose_tabel()
    used_factors = []  # lista istället för set
    total_questions = 11
    doors_left = 12

    while len(used_factors) < total_questions and doors_left > 1:
        if ask_math_question(tabel, used_factors):
            doors_left -= 1
            print(f"Antal dörrar kvar: {doors_left}")
            if not choose_zombie_door(doors_left):
                break
        else:
            print("Du måste svara rätt för att gå vidare!")

    if doors_left == 1:
        print("\nGrattis! Du klarade alla frågor och undvek zombierna!")
    else:
        print("\nSpelet är slut. Försök igen!")

# Starta spelet
start_game()
