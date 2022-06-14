from nltk.corpus import words as nltk
from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer
import re,string


def oof():
    stop_words=set(stopwords.words('english'))
    ext=".txt"
    for i in range(1,6):
        with open(str(i)+ext,encoding="utf8") as openfile, open('output'+str(i)+ext, 'w') as f_output:
            print("Buscando "+str(i)+ext)
            for line in openfile:
                line_words = set(word_tokenize(line))
                dictionary=dict.fromkeys(nltk.words(),None)
                word=line.split()
                stop_words_present = line_words & stop_words
                
                if stop_words_present:
                    print(".")
                else:
                    try:
                        x=dictionary[word[0]]
                        y=dictionary[word[1]]
                        f_output.write(line)
                        continue
                    except KeyError:
                        continue
stemmer_english=SnowballStemmer('english')
def prueba_snowball(ga):
    return stemmer_english.stem(ga)

def cueck(palabra1,palabra2):
    a_palabra1=palabra1.split()
    a_palabra2=palabra2.split()
    suma1=0
    suma2=0
    for i in range(1,2):
        with open(str(i)+".txt",'r') as openfile:
            for line in openfile:
                word=line.split()
                stem1=prueba_snowball(word[0])
                stem2=prueba_snowball(word[1])
                ##print(word[0], a_palabra1[0])
                ##print(word[1], a_palabra1[1])
                ##print(stem2==prueba_snowball(a_palabra1[1]))
                ##print(stem1==prueba_snowball(a_palabra1[0]))
                ps1=prueba_snowball(a_palabra1[0])
                ps2=prueba_snowball(a_palabra1[1])
                ps3=prueba_snowball(a_palabra2[0])
                ps4= prueba_snowball(a_palabra2[1])
                if(ps1==stem1 and ps2==stem2):
                    suma1=suma1+int(word[2])
                if(ps3==stem1 and ps4==stem2):
                    suma2=suma2+int(word[2])
    
    print(suma1)
    print(suma2)

palabra1="Apple Jack"
palabra2="Apple Jam"
a=palabra1.split()
print(a)
b=prueba_snowball(a[0])
c=prueba_snowball(a[1])
print(b)
print(c)
if(prueba_snowball('apples')==b):
    print("Son iguales nomames")
#cueck("Apple Jack","Apple Jam")
cueck(palabra1,palabra2)

#print(prueba_snowball('apples'))

#perr brav
#perr y brav
#cueck(["Apple", "Jack"],["Apple","Jam"])
#cueck("Apple Jack","Apple Jam")
###################main

#oof
