"""
Dette er portfolio opgave 1 i Open Data Science. 
Læg titanic.csv filen i samme sti i en mappe ved navn "data".
Kør scriptet, da print funktionen er taget i brug

- Af Mushtaba Osmani
"""

import pandas as pd
df_titanic = pd.read_csv("data/titanic.csv")

from collections import Counter # importerer Counter funktionen her, da den bliver brugbar i opgaven

#Opgave 2 - Dataframes beskrevet
 

columns = df_titanic.shape[0] # får antal kolloner 
rows = df_titanic.shape[1] # får antal rækker
print(f"Der er {rows} rækker og {columns} kolonner i datasættet, de {columns} indikerer også antallet af passagere ombord" )



print("Dermed har vi ", df_titanic.size," antal celler i datasættet\n") 

print("Her ses de forskellige 'types' af værdierne i dataæsttet:\n" + str(df_titanic.dtypes),"\n")
# Her får vi typer af de forskellige rows-værdier i enten objects, integers eller floats.

"""
Nenstående har vi udvidet hvor meget der bliver vist af dataæsttet, ifht. max rækker, max kolonner og max bredde.
Hvis man vil vise den i konsol kan man man kalde funktionen, df_options()
"""
def df_options ():
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)
    pd.set_option("display.width",150)
    print(df_titanic) 

# Opgave 3 - Deskriptiv data
print("I det nuværende datasæt var antal overlevende på :", df_titanic["Survived"].sum())

print("Gennemsnitsalderen var: ", round(df_titanic["Age"].mean()), "år")

print("Median alderen var: ", round(df_titanic["Age"].median()), "år")

print("Gennemsnitsprisen på en billet var på:", round(df_titanic["Fare"].mean()), "£\n")
pclass1 = 0
pclass2 = 0
pclass3 = 0

for answer in df_titanic["Pclass"]: # vi går igennem listen Pclass med en for loop
    if answer == 1:  # hvis vi støder på en prisklasse 1 >
        pclass1 += 1 # lægger vi den i pclass1, og det samme gøres i pclass2 og pclass 3
    elif answer == 2: 
        pclass2 += 1
    elif answer == 3:
        pclass3 += 1

print(f"Der er {pclass1} passagere i prisklasse 1, {pclass2} i prisklasse 2 og {pclass3} i prisklasse 3 \n")
        
sex_list = df_titanic["Sex"]

male_female_count = Counter(sex_list)
print("\n Her ses antallet af mænd og kvinder: \n", male_female_count)



# Opgave 4 - personer med samme efternavn

name_list = df_titanic["Name"] # Får hentet alle navne i databasen


list_surnames = []                              # Skaber en ny liste til efternavne
for names in name_list:
    extract_surname = names.split()[-1:]        #Finder efternavne ved at bruge split funktion
    for lastname in extract_surname:
        list_surnames.append(lastname)          # Sætter udeluekkende efternavnene i den nye liste
        
surname_count = Counter(list_surnames)          # Counter bliver brugt til at ligge duplicate navne i en tæller 
print("\n Disse er de mest hyppige efternavne (Navn, antal personer med samme efternavn)\n", surname_count.most_common(3))

# Opgave 5 - Pivot tabel 

# Fordeling af tre prisklasser
pclass_pivot = df_titanic["Pclass"].value_counts()
print ("\nFordeling af tre prisklasser:\n"+str(pclass_pivot),"\n")


# Antal overlevende (1) og døde (0) i hvert prisklasse
surv_dead_pivot = df_titanic.groupby("Pclass")["Survived"].value_counts()
print("Antal overlevende (1) og døde (0) i hvert prisklasse \n"+ str(surv_dead_pivot),"\n\n\n")

#Ikke nødvendigt information til opgaven men en god tabel til overblik af de forskellige prisklasser:
pclass_pivot2 = pd.pivot_table(df_titanic, columns = "Pclass")
print("Ikke nødvendigt information til opgaven men en god tabel til overblik af de forskellige prisklasser: \n" + str(pclass_pivot2))
