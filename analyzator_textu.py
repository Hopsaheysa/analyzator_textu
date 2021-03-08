jmeno = input("Dobrý den. Prosím zadejte uživatelské jméno: ")
heslo = input("Dobrý den. Prosím zadejte heslo: ")
hesla = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# zadání už. jména a hesla = 3 pokusy
pokus = 0
while hesla.get(jmeno) != heslo:
    if pokus == 2:
        print("Uživatelské jméno nebo heslo byly zadány 3x chybně. Přístup byl odepřen!")
        exit()
    print("Uživatelské jméno nebo heslo byly zadány chybně.")
    jmeno = input("Prosím zadejte uživatelské jméno: ")
    heslo = input("Prosím zadejte heslo: ")
    pokus += 1


print("=" * 120)
print(f"Vítejte v analyzátoru textu, {jmeno}!")
print("=" * 120)
zobrazeni_textu = input("Pokud chceš vidět dnešní texty zadej 'T'. Pokud texty znáš a zobrazit je nechceš, "
                        "stiskni jakoukoliv jinou klávesu: ")
print("=" * 120)

text1 = '''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. 
'''
text2 = '''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.
'''
text3 = '''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
if zobrazeni_textu == "t" or zobrazeni_textu == "T":
    print("TEXT1", text1)
    print("TEXT2", text2)
    print("TEXT3", text3)
    print("=" * 50)
    print("")

# Inputujeme string abychom se vyhnuli nepříjemným errorům
TEXT_zadani = input("Zadejte číslo od 1-3 dle Vámi vybraného textu, který chete analyzovat: ")
pokus = 0
while TEXT_zadani != "1" and TEXT_zadani != "2" and TEXT_zadani != "3":
    print("Omlouváme se, ale Vámi zadaná informace není platná")
    TEXT_zadani = input("Zadejte číslo od 1-3 dle Vámi vybraného textu: ")
    pokus += 1
    if pokus == 2:
        print("Tomuto zadání neodpovídá žádný článek v databazi! Děkujeme, přijďte zas!")
        exit()

# Zintegerujeme input pro zadání článku a pak ho použijeme k indexování článků
TEXT_zadani = int(TEXT_zadani)
TEXT_list = [text1, text2, text3]
TEXT = TEXT_list[TEXT_zadani - 1]
print("=" * 120)
# rozdělení textu na list slov a vyčištění od nechtěných znaků
slova = TEXT.split()
vycistena_slova = [slovo.strip(", .!") for slovo in slova]

pomocna_title = 0
pomocna_upper = 0
pomocna_lower = 0
pomocna_num = 0
pomocna_cislo = 0

# V tomto případě můžeme použít jeden for pro více ifů protože se navzájem vylučujíbob
# pro přidávání dalších if na to dej pozor a popřípadě je rozděl do více fórů
for pomocna in vycistena_slova:
    if pomocna.istitle():
        pomocna_title += 1
    if pomocna.isupper():
        pomocna_upper += 1
    if pomocna.islower():
        pomocna_lower += 1
    if pomocna.isdigit():
        pomocna_num += 1
        pomocna_cislo += int(pomocna)
print(f"V textu {TEXT_zadani} je: \n"
      f"{len(vycistena_slova)}x slovo.\n"
      f"{pomocna_title}x slovo, které začíná velkým písmenem.\n"
      f"{pomocna_upper}x slovo, které má všechna písmena velká.\n"
      f"{pomocna_lower}x slovo, které má všechna písmena malá.\n"
      f"{pomocna_num}x 'slovo' složené jen z číslic.\n"
      f"Součet čísel v tomto textu je {pomocna_cislo}.")
print("=" * 120, "\n")

# zde hledám jaká je nejdelší délka slova a tvořím slovník délka:počet
promenna_delka = 0
slovnik_slov = {}
for delka in vycistena_slova:
    slovnik_slov[len(delka)] = slovnik_slov.setdefault(len(delka), 0) + 1
    if len(delka) > promenna_delka:
        promenna_delka = len(delka)



# tištění grafíku a přidání do slovníku nul
nejpocetnejsi = max(slovnik_slov.values())
print("DÉLKA |", "ZNÁZORNĚNÍ".center(nejpocetnejsi), "| POČET")

for item in range(1, promenna_delka + 1):
    slovnik_slov[item] = slovnik_slov.setdefault(item, 0)
    print(str(item).rjust(5), "|", str("*" * int(slovnik_slov[item])).ljust(nejpocetnejsi), "|", str(slovnik_slov.get(item)))
