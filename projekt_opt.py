import random

def get_int(prompt, min_v, max_v):
    while True:
        try:
            v = int(input(prompt))
            if min_v <= v <= max_v: return v
            print(f"Ange ett tal mellan {min_v} och {max_v}.")
        except: print("Felaktig inmatning.")

def start_game():
    print("Zombiematte!")
    t = get_int("Välj tabell (2–12): ", 2, 12)
    faktorer = random.sample(range(2, 13), 11)
    doors = 12

    for f in faktorer:
        if get_int(f"{t} * {f} = ", 0, 9999) != t * f:
            print("Fel svar.\n")
            continue
        doors -= 1
        z = random.randint(1, doors)
        d = get_int(f"Välj en dörr (1–{doors}): ", 1, doors)
        if d == z:
            print(f"ZOMBIES! Bakom dörr {z}. Game over.")
            return
        print(f"Du klarade dig! Zombien var bakom dörr {z}.\n")

    print("Grattis! Du klarade alla frågor och överlevde!")

start_game()
