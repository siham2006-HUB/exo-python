T=[12.5,14,9.5,17,21,19.5,11 ] 
moyenne= round(sum(T)/len(T),2)
print("Moyenne:",moyenne)
print("Min:",min(T),"Max:",max(T))
compt=0
for i in T:
    if i>15:
        compt+=1    
print("jours> à 15:", compt)
fahrenheit =[t*9/5+32 for t in T]
print("Fahrenheit:",fahrenheit)
for i,t in enumerate(T,start=1):
    print(f"jour {i}: {t}°C")
