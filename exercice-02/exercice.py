temperatures= [-3,0,15,31]
for temperature in temperatures:
    if temperature<0:
        print(f"{temperature} °C : gel")
    elif temperature<15:
        print(f"{temperature} °C : froid")
    elif temperature<25:
        print(f"{temperature} °C : doux")
    else:
        print(f"{temperature} °C : chaud")
    print()
annee=[2024, 1900, 2000]
for annee in annee:
    if annee%4==0 and annee %100!=0:
        print(f"{annee} : bissextile")
    elif annee%400==0 :
        print(f"{annee} : bissextile")
    else:
        print(f"{annee} : non bissextile")
        