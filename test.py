
f = open("cleaned/Nomination_Chirac1.txt", "r", encoding="utf-8")
#f2 = open("cleaned/cleaned.txt", "w", encoding="utf-8")

exeption = "çàéèêëï0123456789"
lines = f.readline()
lines = lines.lower()
lines = lines.replace(chr(10)," ")
lines = lines.replace(" ", "/")
lines = [x if (x>="a" and x<="z") or x in exeption else " " for x in lines]
lines = "".join(lines)
lines = lines.split(" ")
print(lines)
st= ''
print(len(st))