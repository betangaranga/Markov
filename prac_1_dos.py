import unidecode,string,math
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z' ,'ç', 'æ' ,'œ', ' ','\n'];
file = open("DCfrances.txt","r",encoding = "ISO-8859-1")
fLow="aaaæçeeeeiioœuuuaaaæçeeeeiioœuuu"
fUp="ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçèéêëîïôœùûü"
repeticiones=[]
probabilidades=[]
entropias=[]
rep_mark_1=[]
prob_mark_1=[]
entro_mark_1=[]
parejas=[]
texto_general=file.read()
ftranslator = str.maketrans(fUp,fLow)
x=texto_general.translate(ftranslator)
texto_minusculas=x.lower()
translator = str.maketrans('', '', string.punctuation)
texto_puntuacion=texto_minusculas.translate(translator)
texto = ''.join([i for i in texto_puntuacion if not i.isdigit()])
for letra in ABC:
    repeticiones.append(texto.count(letra))
    index=ABC.index(letra)
    probabilidades.append(repeticiones[index]/len(texto))#Repeticiones contiene ahora el num de repeticiones por caracter en el texto
for probabilidad in probabilidades:
    try:
        entropias.append(math.log((1/probabilidad),2)*probabilidad)
    except ZeroDivisionError:
        entropias.append(0)
#print(texto)
#EMPIEZA MARKOV
for letra  in ABC:
            index=ABC.index(letra)
            for letra in ABC:
                combinacion=ABC[index]+letra
                rep_mark_1.append(texto.count(combinacion))
                parejas.append(combinacion)
                index2=parejas.index(combinacion)
                try:
                    prob_mark_1.append(rep_mark_1[index2]/repeticiones[index])
                except ZeroDivisionError:
                    prob_mark_1.append(0)
                #entro=probabilidades[index]*prob_mark_1[index2]*math.log((1/prob_mark_1[index2]),2)
#print((prob_mark_1))
dicc=dict(zip(parejas,rep_mark_1))
print(dict(zip(parejas,prob_mark_1)))
#valores=dicc.values();
#print(dicc.get("za"))
#print(prob_mark_1)
