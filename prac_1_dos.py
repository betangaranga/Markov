import string,math
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z' ,'ç', 'æ' ,'œ', ' ','\n'];
file = open("/home/angel/Documentos/Teoria_info/Prac_1/Markov/DCfrances.txt","r",encoding = "ISO-8859-1")
fLow="aaaæçeeeeiioœuuuaaaæçeeeeiioœuuu"
fUp="ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçèéêëîïôœùûü"
repeticiones=[]
probabilidades=[]
entropias=[]
rep_mark_1=[]
prob_mark_1=[]
entro_mark_1=[]
parejas=[]
rep_mark_2=[]
prob_mark_2=[]
entro_mark_2=[]
tercias=[]
rep_mark_3=[]
prob_mark_3=[]
entro_mark_3=[]
cuarteto=[]
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

#EMPIEZA MARKOV (1 ERA)
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

dicc=dict(zip(parejas,rep_mark_1))
#print(dicc)
#CALCULO DE ENTROPIAS PRIMERA DE MARK0V
for pareja in parejas:
    letra=pareja[0]
    index=ABC.index(letra)
    index2=parejas.index(pareja)
    try:
        pr=probabilidades[index]*prob_mark_1[index2]
        proba=pr*math.log((1/prob_mark_1[index2]),2)
    except ZeroDivisionError:
        proba=0
    entro_mark_1.append(proba)

#EMPIEZA MARKOV (2DA)
for letra  in ABC:
            index=ABC.index(letra)
            for letra in ABC:
                combinacion=ABC[index]+letra
                index2=parejas.index(pareja)
                for letra in ABC:
                    tripleta=combinacion+letra
                    tercias.append(tripleta)
                    rep_mark_2.append(texto.count(tripleta))
                    index3=tercias.index(tripleta)
                    try:
                        prob_mark_2.append(rep_mark_2[index3]/rep_mark_1[index2])
                    except ZeroDivisionError:
                        prob_mark_2.append(0)
#CALCULO DE ENTROPIAS SEGUNDA DE MARKOV
for tercia in tercias:
    letras=tercia[0]+tercia[1]
    index=ABC.index(tercia[0])
    index2=parejas.index(letras)
    index3=tercias.index(tercia)
    try:
        proba=probabilidades[index]*prob_mark_1[index2]*prob_mark_2[index3]*math.log((1/prob_mark_2[index3]),2)
    except ZeroDivisionError:
        proba=0
    entro_mark_2.append(proba)
#COMIENZA MARKOV DE TERCER ORDEN






print("Entropia de una fuente sin memoria : {} bytes".format(sum(entropias)))
print("Primera de Markov : {} bytes".format(sum(entro_mark_1)))#ENTROPIA  PRIMERA DE MARKOV
print("Segunda de Markov : {} bytes".format(sum(entro_mark_2)))#ENTROPIA  SEGUNDA DE MARKOV
