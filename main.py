""" 
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Leoš Leitgeb

email: leitgebl@seznam.cz
"""

# Program >
# 1. Vyžádání a kontrola jména a hesla, ukončení při chybě

jmena_hesla = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

jmeno = input("username: ")
heslo = input("password: ")
print("-" * 50)
if jmena_hesla.get(jmeno) == heslo:
    print("welcome to the app,",jmeno, "\nWe have 3 texts to be analyzed.")
else:
  print("unregistered user, terminating the program..")
  exit()
print("-" * 50)

# 2. Výběr 1 ze 3 textů k analýze, ukončení při chybné volbě

text_to_analyze = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# 2a. Dotaz na typ textu s kontrolou na číslo (typ/hodnotu)

while True:
  try:
    no_text = int(input("Enter a number btw. 1 and 3 to select texts: "))
    break
  except ValueError:
    print("invalid choice, terminating the program..")
    exit()
print("-" * 50)
no_text = int(no_text)
if no_text > 3 or no_text <= 0:
  print("invalid choice, terminating the program..")
  exit()
else:
  selected_text = text_to_analyze[no_text -1]

# 2b. Očištění textu o čárky a tečky
final_text_to_analyze = selected_text.replace(",", "").replace(".", "")

# 3. Statistiky
# 3a. Počet slov¨
# >> rozdělení řetězce na seznam slov a pomocí len() spočítání

slova = final_text_to_analyze.split()
pocet_slov = len(slova)
print("There are",pocet_slov, "words in the selected text.")

# 3b. Počet slov začínajících velkým písmenem
# >> rozdělení řetězce viz 3a a spočítání znaků s v.pismenem na indexu 0

pocet_slov_upper = 0

for slovo in slova:
  if slovo[0].isupper():
    pocet_slov_upper = pocet_slov_upper + 1
print("There are", pocet_slov_upper, "titlecase words.")

# 3c. Počet slov psaných velkými písmeny
# >> rozdělení řetězce viz 3a a spočítá počet s malým pismenem

pocet_slov_upper = 0

for slovo in slova:
  if slovo.isupper():
    pocet_slov_upper = pocet_slov_upper + 1
print("There are", pocet_slov_upper, "uppercase words.")

# 3d. Počet slov psaných malými písmeny
# >> rozdělení řetězce viz 3a a spočítá počet s velkým pismenem

pocet_slov_lower = 0

for slovo in slova:
    if slovo.islower():
        pocet_slov_lower = pocet_slov_lower + 1
print("There are", pocet_slov_lower, "lowercase words.")

# 3e. Počet a sumu čísel (ne cifer)
# >> rozdělení řetězce viz 3a a spočítá počet a sumu čísel

pocet_cislic = 0
suma_cislic = 0

for retezec in slova:
  if retezec.isdigit():
    pocet_cislic = pocet_cislic + 1
    suma_cislic = suma_cislic + int(retezec)
print("There are", pocet_cislic, "numeric strings.")
print("The sum of all the numbers",suma_cislic)

# 4. Vizualizace výsledků
# >> rozdělení řetězce viz 3a a pomocí while a len spočítá četnost

# 4a Spočítáme délky slov pomocí komprehence a vložíme do listu - delky_slov
delky_slov = [len(slovo) for slovo in slova]

# 4b. Získáme největší délku slova - nejvetsi_delka - pro získání rozsahu hodnot
delky_slov.sort()  # seřazení od nejmenšího k nevyššímu
nejvetsi_delka = delky_slov[-1]  # získá poslední znak = největší délku slova

# 4c. Získáme největší výskyt slov určité délky - nejvetsi_vyskyt - pro odsazení
# >> smyčka, která půjde tolikrát, kolik je největší délka slova

opakovani = 1
nejvetsi_vyskyt = 1

while opakovani <= nejvetsi_delka:
  cetnost_slov = delky_slov.count(opakovani)
  if cetnost_slov > nejvetsi_vyskyt:
    nejvetsi_vyskyt = cetnost_slov  # uložení nejvyšší hodnoty
  opakovani = opakovani + 1

# 4d. Vyhodnotíme četnost výskytů v grafu - finální zobrazení
# >> smyčka, která půjde tolikrát, kolik je největší délka slova
opakovani_n = 1

print("-" * 50)
print("LEN","\t| OCCURENCES", " " * (nejvetsi_vyskyt -10), "| NR.") # nadpis
print("-" * 50)

while opakovani_n <= nejvetsi_delka:
  cetnost_slov_n = delky_slov.count(opakovani_n)

  print(
      opakovani_n, "\t|" , "*" * cetnost_slov_n,
      " " * (nejvetsi_vyskyt - cetnost_slov_n), "|",cetnost_slov_n
  )
  opakovani_n = opakovani_n + 1
print("-" * 50)