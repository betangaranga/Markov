import string
file = open("DCfrances.txt","r",encoding="ISO-8859-1")
texto_general=file.read()
ftranslator = str.maketrans("ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçèéêëîïôœùûü","aaaæçeeeeiioœuuuaaaæçeeeeiioœuuu")
x=texto_general.translate(ftranslator)
texto=[]
texto1= ''.join([i for i in x if not i.isdigit()])
texto2=texto1.replace(" ", "")
texto3=list(texto2)
for letra in x:
    texto3.append(letra)
    if len(texto)==40000:
        break
file.close()
file = open("DCfrances2.txt","w",encoding="ISO-8859-1")
file.write(''.join(texto2))
