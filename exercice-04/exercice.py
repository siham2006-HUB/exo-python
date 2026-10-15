ventes=[
    {"produit": "cafe", "prix": 2.5, "quantite": 120},
    {"produit": "the", "prix": 2.880, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]
ca_par_produit={}
for v in ventes:
    ca_par_produit[v["produit"]]=v["prix"]*v["quantite"]
print(ca_par_produit)
total_ca=sum(ca_par_produit.values())
print(f"Chiffre d'affaire total: {total_ca:.2f}€")
meilleur_produit=max(ca_par_produit, key=ca_par_produit.get)
print(f"Meilleur produit: {meilleur_produit} 
      