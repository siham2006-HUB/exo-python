def convertir_note(texte):
    try:
        note = float(texte.replace(",", "."))
        except ValueError:
        return None
    df moyenne(valeurs):
    return round(sum(valeurs) / len(valeurs)
    df montion(note):
    if note >= 16:  
        return "Tres Bien"
        elif note >= 14:
            return "Bien"
        elif note >= 12:
            return "Aassez Bien"
        elif note >= 10:
            return "P"
        else:
            return "Insuffisant"