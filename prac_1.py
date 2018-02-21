import unidecode,string,math
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '];
file = open("dante.txt","r")
repeticiones=[]
probabilidades=[]
entropias=[]
texto_general=file.read()
texto_minusculas=texto_general.lower()
texto_acentos= unidecode.unidecode(texto_minusculas)
translator = str.maketrans('', '', string.punctuation)
texto_puntuacion=texto_acentos.translate(translator)
texto = ''.join([i for i in texto_puntuacion if not i.isdigit()])
for letra in ABC:
    repeticiones.append(texto.count(letra))
    index=ABC.index(letra)
    probabilidades.append(repeticiones[index]/len(texto))
print(repeticiones)#Repeticiones contiene ahora el num de repeticiones por caracter en el texto
print(sum(probabilidades))
for probabilidad in probabilidades:
    try:
        entropias.append(math.log((1/probabilidad),2)*probabilidad)
    except ZeroDivisionError:
        entropias.append(0)

print(sum(entropias))
