import string,math,time
import collections
import itertools
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
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
texto = ''.join([i for i in texto_puntuacion if not i.isdigit()]).split()
##DEFINIMOS ABECEDARIO
#texto=list("hola yo me llamo pedrito sola")
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y' ,'z' ,'ç', 'æ' ,'œ',' ']
##DEFINIMOS PAREJAS,TERCIAS Y CUARTETO
parejas = [''.join(i) for i in itertools.product(ABC, repeat = 2)]
tercias= [''.join(i) for i in itertools.product(ABC, repeat = 3)]
cuarteto = [''.join(i) for i in itertools.product(ABC, repeat = 4)]
import numpy as np
vectorizer = CountVectorizer(vocabulary=cuarteto)
X = vectorizer.fit_transform(texto)
freq = np.ravel(X.sum(axis=0))
vect = CountVectorizer(stop_words = frozenset(ABC))
dtm = vect.fit_transform(list("hola perrro malditoaaaa"))
print(pd.DataFrame(dtm.toarray(), columns=vect.get_feature_names()))

print("--- %s seconds ---" % (time.time() - start_time))
