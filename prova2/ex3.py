emoji = input()
frase = input()

while frase != "":
    print(frase.replace(emoji,"").replace(emoji[::-1],""))
    frase = input()