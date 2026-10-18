def convertir_note(texte):
    try:
        return float(texte.strip().replace(",", "."))
    except ValueError:
        return None

def moyenne(valeurs):
    if not valeurs:
        return None
    return sum(valeurs) / len(valeurs)

def mention(note):
    if note >= 16:
        return "Très bien"
    if note >= 14:
        return "Bien"
    if note >= 12:
        return "Assez bien"
    if note >= 10:
        return "Passable"
    return "Insuffisant"
