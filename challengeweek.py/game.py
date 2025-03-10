import random

word = [
    "appel", "boter", "cactus", "droom", "eeuws", "fiets", "grote", "haven", "ijsje", "jacht",
    "kassa", "lachen", "mango", "nacht", "oranje", "piano", "quick", "regen", "schep", "tafel",
    "uniek", "vogel", "water", "xenon", "yoghurt", "zomer", "azijn", "beker", "champ", "datum",
    "einde", "flesj", "groep", "houten", "inktp", "joker", "kaasj", "lucht", "meter", "niets",
    "ovenk", "prijs", "quote", "radio", "sjaal", "takje", "urgent", "vader", "wezen", "xerox",
    "yaren", "zandp", "boekt", "charme", "dansp", "echoo", "flits", "grapj", "hoofd", "inlog",
    "juist", "klank", "licht", "muziek", "nooit", "openl", "puntj", "qatar", "ritme", "storm",
    "titel", "uitje", "visje", "wapen", "zonne", "angst", "beeld", "caren", "exact", "focus",
    "gooit", "hobby", "input", "jaren", "kracht", "lijst", "moment", "optie", "passie", "quizj",
    "ruimt", "stoer", "troep", "vrouw"
]
antwoord = random.choice(word)
print(f'Je woord is {antwoord[0]}')
while True:
    guess = input()
    for letter in guess:
        for char in antwoord:
            if guess == antwoord:
                print("Correct Je hebt het woordt geraden")
                exit()
            elif letter == char:
                print(f"{letter} is de correcte letter")
                exit()
