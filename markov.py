import string,math,itertools,time
from collections import Counter
##OBTENEMOS Y LIMPIAMOS TEXTO
start_time = time.time()
file = open(r"C:\Users\PC\Documents\Markov\DCfrances.txt","r")
fLow="aaaæçeeeeiioœuuuaaaæçeeeeiioœuuu"
fUp="ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçèéêëîïôœùûü"
texto_general=file.read()
ftranslator = str.maketrans(fUp,fLow)
x=texto_general.translate(ftranslator)
texto_minusculas=x.lower()
translator = str.maketrans('', '', string.punctuation)
texto_puntuacion=texto_minusculas.translate(translator)
texto = ''.join([i for i in texto_puntuacion if not i.isdigit()])
##DEFINIMOS ABECEDARIO
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z' ,'ç', 'æ' ,'œ',' ']
##DEFINIMOS PAREJAS,TERCIAS Y CUARTETO
parejas = [''.join(i) for i in itertools.product(ABC, repeat = 2)]
tercias= [''.join(i) for i in itertools.product(ABC, repeat = 3)]
cuarteto = [''.join(i) for i in itertools.product(ABC, repeat = 4)]
##OBTENER REPETICIONES Y PROBABILIDAD EN FUENTE SIN MEMORIA:
probabilidades=[]
repeticiones=[]
entropias=[]
#FUENTE SIN MEMORIA:
for letra in ABC:
    repeticiones.append(texto.count(letra))
    index=ABC.index(letra)
    probabilidades.append(repeticiones[index]/len(texto))
    try:
        entropias.append(math.log((1/probabilidades[index]),2)*probabilidades[index])
    except ZeroDivisionError:
        entropias.append(0)
##PRIMERA DE MARKOV:
rep_mark_1=[]
prob_mark_1=[]
entro_mark_1=[]
for pareja in parejas:
    letra=pareja[0]
    rep_mark_1.append(texto.count(pareja))
    index2=parejas.index(pareja)
    index=ABC.index(letra)
    try:
        prob_mark_1.append(rep_mark_1[index2]/repeticiones[index])
    except ZeroDivisionError:
        prob_mark_1.append(0)
    try:
        pr=probabilidades[index]*prob_mark_1[index2]
        proba=pr*math.log((1/prob_mark_1[index2]),2)
    except ZeroDivisionError:
        proba=0
    entro_mark_1.append(proba)
##SEGUNDA DE MARK0V
rep_mark_2=[]
prob_mark_2=[]
entro_mark_2=[]
for tercia in tercias:
    letras=tercia[0]+tercia[1]
    rep_mark_2.append(texto.count(tercia))
    index3=tercias.index(tercia)
    index=ABC.index(tercia[0])
    index2=parejas.index(letras)
    try:
        prob_mark_2.append(rep_mark_2[index3]/rep_mark_1[index2])
    except ZeroDivisionError:
        prob_mark_2.append(0)
    try:
        proba=probabilidades[index]*prob_mark_1[index2]*prob_mark_2[index3]*math.log((1/prob_mark_2[index3]),2)
    except ZeroDivisionError:
        proba=0
    entro_mark_2.append(proba)
##TERCERA DE MARKOV
rep_mark_3 =[]
prob_mark_3=[]
entro_mark_3=[]
cua=[w for w, c in Counter(cuarteto).items() if w in texto]

for cuatro in cua:
    rep_mark_3.append(texto.count(cuatro))
    letras=cuatro[0]+cuatro[1]+cuatro[2]
    index4=cua.index(cuatro)
    index=ABC.index(cuatro[0])
    index2=parejas.index(cuatro[0]+cuatro[1])
    index3=tercias.index(letras)
    try:
        prob_mark_3.append(rep_mark_3[index4]/rep_mark_2[index3])
    except ZeroDivisionError:
        prob_mark_3.append(0)
    try:
        proba=probabilidades[index]*prob_mark_1[index2]*prob_mark_2[index3]*prob_mark_3[index4]*math.log((1/prob_mark_3[index4]),2)
        #print(math.log((1/prob_mark_3[index4]),2))
    except ZeroDivisionError:
        proba=0
    entro_mark_3.append(proba)
    #print(cuatro)

print("Entropia de una fuente sin memoria : {} bytes".format(sum(entropias)))
print("Primera de Markov : {} bytes".format(sum(entro_mark_1)))
print("Segunda de Markov : {} bytes".format(sum(entro_mark_2)))#ENTROPIA  SEGUNDA DE MARKOV
print("Tercera de Markov : {} bytes".format(sum(entro_mark_3)))#ENTROPIA  TERCERA DE MARKOV
print("--- %s seconds ---" % (time.time() - start_time))
