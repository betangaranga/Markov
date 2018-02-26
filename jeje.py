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
#ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z' ,'ç', 'æ' ,'œ']
##DEFINIMOS PAREJAS,TERCIAS Y CUARTETO
parejas = [''.join(i) for i in itertools.product(ABC, repeat = 2)]
tercias= [''.join(i) for i in itertools.product(ABC, repeat = 3)]
cuarteto = [''.join(i) for i in itertools.product(ABC, repeat = 4)]
##OBTENER REPETICIONES Y PROBABILIDAD EN FUENTE SIN MEMORIA:
probabilidades=[]
repeticiones=[]
entropias=[]
#FUENTE SIN MEMORIA:
repeticiones = Counter()
for letra in ABC:
    repeticiones[letra]+=1
##PRIMERA DE MARKOV:
rep_mark_1=Counter()
prob_mark_1=[]
entro_mark_1=[]
for pareja in parejas:
    letra=pareja[0]
    rep_mark_1[pareja]+=1
rep_mark_2=Counter()
prob_mark_2=[]
entro_mark_2=[]
for tercia in tercias:
    letras=tercia[0]+tercia[1]
    rep_mark_2[tercia]+=1
##TERCERA DE MARKOV
rep_mark_3 =Counter()
prob_mark_3=[]
entro_mark_3=[]
cua=[w for w, c in Counter(cuarteto).items() if w in texto]

for cuatro in cua:
    rep_mark_3[cuatro]+=1
    #print(cuatro)+=1
print("Entropia de una fuente sin memoria : {} bytes".format(sum(entropias)))
print("Primera de Markov : {} bytes".format((rep_mark_1)))
print("Segunda de Markov : {} bytes".format((rep_mark_2)))#ENTROPIA  SEGUNDA DE MARKOV
print("Tercera de Markov : {} bytes".format((rep_mark_3)))#ENTROPIA  TERCERA DE MARKOV
print("--- %s seconds ---" % (time.time() - start_time))
