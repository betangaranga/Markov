import unidecode,string,math,unicodedata
 
ABC=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '];

#Fmin=['à','â','ä','æ','ç','è','é','ê','ë','î','ï','ô','œ','ù','û','ü']
#Fmay=['À','Â','Ä','Æ','Ç','È','É','Ê','Ë','Î','Ï','Ô','Œ','Ù,','Û','Ü']

fLow="aaaæçeeeeiioœuuuaaaæçeeeeiioœuuu"
fUp="ÀÂÄÆÇÈÉÊËÎÏÔŒÙÛÜàâäæçèéêëîïôœùûü"
file = open("dante.txt","r",encoding="ISO-8859-1") 
texto_general=file.read()
ftranslator = str.maketrans(fUp,fLow)
x=texto_general.translate(ftranslator)
texto_minusculas=x.lower()
translator = str.maketrans('', '', string.punctuation)
texto_puntuacion=texto_minusculas.translate(translator)
texto = ''.join([i for i in texto_puntuacion if not i.isdigit()])

print (texto)


#para aleman
#Amin=['ä''å''æ''ğ''ë''ö''ø''ş''ü''ÿ''ß']
#Amay=['Ä','Å','Æ','Ğ','Ë','Ö','Ø','Ş','Ü']
#aLow="äåæğëöøşü"
#aUp="ÄÅÆĞËÖØŞÜ"	
#file = open("aleman.txt","r",encoding="utf-8") 
#texto_general=file.read()
#atranslator = str.maketrans(aUp,aLow)
#texto_general.translate(atranslator)
#texto_minusculas=texto_general.lower()
#translator = str.maketrans('', '', string.punctuation)
#texto_puntuacion=texto_minusculas.translate(translator)
