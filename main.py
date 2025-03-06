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

jmeno = input("username:")
heslo = input("password:")
print("-" * 40)
if jmena_hesla.get(jmeno) == heslo:
    print("welcome to the app,",jmeno, "\nWe have 3 texts to be analyzed.")
else:
  print("unregistered user, terminating the program..")
  exit()  #
print("-" * 40)

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
# >>> oprava 2, test na číslo změnen z while na if a dáno do jednoho bloku

no_text = (input("Enter a number btw. 1 and 3 to select texts: "))
if no_text.isdigit():
  no_text = int(no_text)
  if no_text > 3 or no_text <= 0:
    print("invalid choice, terminating the program..")
    exit()
else:
  print("invalid choice, terminating the program..")
  exit()

selected_text = text_to_analyze[no_text -1]

# 2b. Očištění textu o čárky a tečky
final_text_to_analyze = selected_text.replace(",", "").replace(".", "")

# 3. Statistiky
# 3a. Rozdělení řetězce na seznam slov pro další výpočty
slova = final_text_to_analyze.split()
print("-" * 40)

# 3b. Spočítání počtu slov
pocet_slov = len(slova)
print("There are",pocet_slov, "words in the selected text.")

# 3c. Výpočty dle zadání, sjednocení do jednoho cyklu for >>> oprava 6
pocet_slov_titlecase = 0  # >>> oprava 1
pocet_slov_upper = 0
pocet_slov_lower = 0
pocet_cislic = 0
suma_cislic = 0

for slovo in slova:
  if slovo.isupper():
    pocet_slov_upper = pocet_slov_upper + 1
  elif slovo[0].isupper() and not slovo.isupper():
    pocet_slov_titlecase = pocet_slov_titlecase + 1
  elif slovo.islower():
    pocet_slov_lower = pocet_slov_lower + 1
  elif slovo.isdigit():
    pocet_cislic = pocet_cislic + 1
    suma_cislic = suma_cislic + int(slovo)

print("There are", pocet_slov_titlecase, "titlecase words.")
print("There are", pocet_slov_upper, "uppercase words.")
print("There are", pocet_slov_lower, "lowercase words.")
print("There are", pocet_cislic, "numeric strings.")
print("The sum of all the numbers",suma_cislic)

# 4. Vizualizace výsledků
# >> rozdělení řetězce viz 3a a pomocí while a len spočítá četnost

# 4a. Spočítáme délky slov pomocí komprehence a vložíme do listu - delky_slov
delky_slov = [len(slovo) for slovo in slova]

# 4b. Získáme největší délku slova - nejvetsi_delka - pro získání rozsahu hodnot
delky_slov.sort()  # seřazení od nejmenšího k nevyššímu
nejvetsi_delka = delky_slov[-1]  # získá poslední znak = největší délku slova

# 4c. Vyhodnotíme četnost výskytů v grafu - finální zobrazení
# >> smyčka, která půjde tolikrát, kolik je největší délka slova
# >>> oprava 3-5 formátování výstupu
opakovani_n = 1

print("-" * 40)
print("LEN|","  OCCURENCES  ", "|NR.", sep='') # nadpis
print("-" * 40)

while opakovani_n <= nejvetsi_delka:
  cetnost_slov_n = delky_slov.count(opakovani_n)
  print(
      str(opakovani_n).rjust(3), "|" , "*" * cetnost_slov_n,
      " " * (20 - cetnost_slov_n), "|",cetnost_slov_n, sep=''
  )
  opakovani_n = opakovani_n + 1