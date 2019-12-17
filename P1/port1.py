#============================================
# Opgave 1 - Se på indholdet af datafilen
#============================================
"""
A: Datafilen indeholder følgende datatyper:
    - Integers: prisklassen, søskende/hustruer ombord, børn/forældre ombord og alderen
    - Floats: Billetprisen (nogle af aldrene er også angivet som floats)
    - Booleans: Overlevede angivet ved 0/1 og køn angivet ved male/female.
    - Strings: Navnene
    
B: Datasættet indeholder ikke data om alle passagerer fra Titatnic,
   men om 887 passagerer.
   15 af passagererne har en fare på 0, hvilket enten er manglende data,
   eller også var passagererne muligvis medarbejdere eler lign.
   således at de ikke skulle betale for en billet.
"""

#============================================
# Opgave 2 - Import af data til dataframe
#============================================

#Importerer pandas og gemmer datafilen i en dataframe
import pandas as pd
df_titan = pd.read_csv("data/titanic.csv")

#Ændrer antal kolonner og bredde så dataframen nemmere kan læses.
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', 150)

print(df_titan, "\n")

# Opgave 2a: Beskrivelse af datasæt med pandas funktioner

# Antallet af rækker i datasættet
print("Antal rækker i datasættet: ",len(df_titan), "\n")

# Antallet af rækker og kolonner i datasættet
print("Antal rækker og kolonner i datasættet: ",df_titan.shape, "\n")

# Antallet af celler i tabellen
print("Antal celler i datasættet: ",df_titan.size, "\n")

# Kolonnernes navne
print("Kolonnernes navne:\n",df_titan.columns, "\n")

# Kolonnernes datatyper
print("Kolonnernes datatyper:\n",df_titan.dtypes, "\n")

#============================================
# Opgave 3: Deskriptiv statistik af datasættet
#============================================

# Antal der overlevede
print("Antal der overlevede:","\n",df_titan['Survived'].sum(),"\n")

# Gennemsnitsalder
print("Gennemsnitsalderen:","\n",df_titan['Age'].mean(),"\n")

# Alders medianen
print("Alders medianen:","\n",df_titan['Age'].median(),"\n")

# Antal mænd og kvinder
print("Antal mænd og kvinder:","\n",df_titan.groupby('Sex')['Sex'].count(),"\n")

# For deskriptiv statistik kan .describe() metoden bruges. Eksempelvis:
df_titan['Age'].describe()
df_titan['Fare'].describe()
df_titan['Pclass'].describe()

#============================================
# Opgave 4: Personer med samme efternavn
#============================================

namelist = df_titan['Name'] # Gemmer datafilens navne i en liste
lastnames = [] # Tom liste til at indeholde efternavne

for lastname in namelist:
    name = lastname.split(" ")[-1:] # Deler alle navnene ved mellemrum, gemmer kun efternavnet
    lastnames.append(name[0]) # Indsætter efternavnet i min liste til efternavne
    
# Jeg gemmer listen med navne i en dataframe, for at kunne bruge en pandas funktion
df_lastnames = pd.DataFrame(lastnames)

# Antal forekomster af hvert enkelt efternavn
print("De 10 mest hyppige efternavne:\n",df_lastnames[0].value_counts().head(10),"\n") 

# Alternativt kan Counter funktionen fra 'collections' bruges
from collections import Counter

# Printer de 10 mest brugte efternavne
print("De 10 mest hyppige efternavne (med Counter-funktionen):\n",Counter(lastnames).most_common(10),"\n")

#============================================
# Opgave 5: Rejsende pr. prisklasse
#============================================

# Antal personer i hver prisklasse
antal = df_titan['Pclass'].value_counts()
print("Antal personer i hver prisklasse:\n",antal,"\n")

# Antal overlevende i hver prisklasse
print("Antal overlevende i hverprisklasse:\n",df_titan.groupby('Pclass')['Survived'].sum(),"\n")

# Antal overlevende og døde i hver prisklasse
print("Antal overlevende og døde i hver prisklasse:\n (0 = døde, 1 = overlevende) \n",df_titan.groupby('Pclass')['Survived'].value_counts())

procent = df_titan.groupby('Pclass')['Survived'].value_counts()
# Procentdelen for døde og overlevende i hver prisklasse:
print('Procentdel døde og overlevende i prisklasse 1: \n',procent[1]/antal[1]*100)
print('Procentdel døde og overlevende i prisklasse 2: \n',procent[2]/antal[2]*100)
print('Procentdel døde og overlevende i prisklasse 3: \n',procent[3]/antal[3]*100)
