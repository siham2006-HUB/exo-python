
T = [12.5, 14, 9.5, 17, 21, 19.5, 11]

moyenne = sum(T) / len(T)
print("Moyenne :", round(moyenne, 2))
print("Minimum :", min(T))
print("Maximum :", max(T))

compter = 0
for t in T:
    if t > 15:
        compter += 1
print("Jours au-dessus de 15 °C :", compter)

F = []
for c in T:
    F.append(c * 9 / 5 + 32)
print("Températures en Fahrenheit :", F)

for i, t in enumerate(T):
    print(f"Jour {i+1} : {t} °C")