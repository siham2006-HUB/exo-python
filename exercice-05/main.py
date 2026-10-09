from outils import convertir_note ,moyenne, mention
notes_brutes=["a2,5","15","abc","9","18.25"]
notes=[]
ignorees=[]
for texte in notes_brutes:
    note=convertir_note(texte)
    if note is None:
        ignorees+=1
    else:
        notes.append(note)
m=moyenne(notes)
print ("Notes ignorees:",ignorees)
print("Moyenne:", round(m, 2))
print("Mention:",mention(m))
      