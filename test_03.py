# Testy vložení mezery a odřádkování
print("Leoš", "Leitgeb", sep="\n")  # odřádkování
print("Leoš", "Leitgeb", sep="")    # separátor žádný !!
print("Leoš", "Leitgeb")            # separátor default mezera
print("Leoš", "Leitgeb", sep="_")   # separátor podtržítko
print("konec", "-----------------------------------------", sep="\n")  # odřádkování

# Test přičítání hodnoty ze slovníku - DICT
hodnota_celkem = 0
baze = {"Leoš": 100, "Jarka": 200, "Ondra": 400,}
for zakaznik, hodnota in baze.items():              # pro dict nutno použít metodu pro vrácení klíče a hodnoty
    hodnota_celkem = hodnota_celkem + hodnota       # přičítání hodnoty
    print(hodnota_celkem)
print("konec", "-----------------------------------------", sep="\n")  # odřádkování


# Test na ukončení při hodnotě 300
hodnota_celkem = 0
baze = {"Leoš": 100, "Jarka": 200, "Ondra": 400,}
for zakaznik, hodnota in baze.items():              # pro dict nutno použít metodu pro vrácení klíče a hodnoty
    hodnota_celkem = hodnota_celkem + hodnota       # přičítání hodnoty
    if hodnota_celkem == 300:                       # test na součet 300       
        print("požadovaná hodnota:", hodnota_celkem)
    else:
        print(hodnota_celkem)
print("konec", "-----------------------------------------", sep="\n")  # odřádkování

# Test z lekce 4

obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]

for radek in obsah:
    print(radek)
    for bunka in radek[0].split(";"):
      print(bunka)