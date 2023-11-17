def replace(text):
    f = open(text, "r", encoding="utf-8")
    f2 = open("cleaned/cleaned.txt", "w", encoding="utf-8")

    exeption = "çàéèêëï0123456789"
    lines = f.readline()
    tab = []
    while lines != "":
        lines = lines.lower()
        mots = lines.split(" ")
        for mot in range(len(mots)):
            for i in range(len(mots[mot])):
                if mots[mot][i] == "'" or mots[mot][i] == "-":
                    mots[mot] = [x for x in mots[mot]]
                    mots[mot][i] = " "
                    mots[mot] = "".join(mots[mot])
                elif (mots[mot][i] < "a" or mots[mot][i] > "z") and mots[mot][i] not in exeption:
                    mots[mot] = [x for x in mots[mot]]
                    mots[mot][i] = ""
                    mots[mot] = "".join(mots[mot])
                    lines = " ".join(mots)
        f2.write(lines)
        lines = f.readline()
    f.close()
    f2.close()