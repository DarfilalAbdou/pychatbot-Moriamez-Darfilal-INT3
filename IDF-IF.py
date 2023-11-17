txt = "Monsieur le President du Conseil Constitutionnel Monsieur le Premier ministre Mesdames Messieurs Les Françaises et les Français m ont renouvelé leur confiance Les devoirs que j ai envers chacun d eux seront constamment présents à mon esprit aujourd hui et pour les cinq années du mandat qu ils m ont donné."
txt = txt.lower()
occurence = {}

motparmot = txt.split(" ")
for i in motparmot:
    if i not in occurence.keys():
        occurence[i] = 1
    else:
        occurence[i] += 1

print (occurence)