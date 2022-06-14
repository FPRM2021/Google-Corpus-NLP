from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from io import open
import re,string
import nltk
from nltk.collocations import *
from nltk import FreqDist
from nltk.util import ngrams    

from nltk.corpus import stopwords
ignored_words = set(stopwords.words('english'))
print(ignored_words)
from nltk.corpus import brown
print (brown.words())
from nltk.stem import SnowballStemmer
stemmer_english=SnowballStemmer('english')
print (stemmer_english.stem('Working'))

words_list=[]


##1.- FILTRO DE PALABRAS
def del_stopwords(palabras):
    stop_words=set(stopwords.words('english'))
    result=[]
    for pal in palabras.split():
        if(len(pal) is 1 ):
            return
        if(pal not in stop_words):
            result.append(pal)
    return result


def del_stopwords(palabras):
    stop_words=set(stopwords.words('english'))
    result=[]
    for pal in palabras.split():
        if(len(pal) is 1 ):
            return
        if(pal not in stop_words):
            result.append(pal)
    return result


##FUNCION RETORNAR STEM
def get_stem(word):
    stemmer_english=SnowballStemmer('english')
    return stemmer_english.stem(word)

get_stem("Workers")

##1.- funcion de filro final
def first_filtro():
    stop_words=set(stopwords.words('english'))
    for i in range(12,13):
        with open(str(i)+".txt",encoding="utf8") as openfile, open('Filtrado'+str(i)+".txt", "w") as f_output:
            print("Buscando en "+str(i)+".txt")
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


def first_filtrooseanomame():
    stop_words=set(stopwords.words('english'))
    for i in range(12,13):
        with open("copia"+str(i)+".txt",encoding="utf8") as openfile, open('Filtrado2oseanomame'+str(i)+".txt", "w") as f_output:
            print("Buscando en copia"+str(i)+".txt")
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

##2.-PRE CALCULO DE SUMATORIA DEL VALOR DE STEMS SIMILARES
def precalculo(palabra1,palabra2):
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
    ##return suma1
##FUNCION DE CALCULAR EL STEM DE CIERTA PALABRA LEYENDO EL ARCHIVO
##def dosestariabien(bigrama):
    

##FUNCION DE CALCULAR LA SIMILITUD LEY DE COSENOS ENTRE 2 BIGRAMAS
def coseno():
    print("\n")
    bigrama1 = "fat cat"
    bigrama2 = "fat dog"
    b1_x = word_tokenize(bigrama1)
    
    b2_x = word_tokenize(bigrama2)
    
    
    sw = stopwords.words('english')

    print(b1_x)
    print("\n")
    print(b2_x)
    
    l1 =[];l2 =[]
    
    b1_x = {w for w in b1_x
            if not w in sw}
    b2_x = {w for w in b2_x
            if not w in sw}
    
    freq1=nltk.FreqDist(b1_x)
    freq2=nltk.FreqDist(b2_x)

    for k,v in freq2.items():
        print (k,v)
    print("\n")

    for k,v in freq1.items():
        print (k,v)
    
    rvector = b1_x.union(b2_x)

    print("\n")
    print(b1_x)
    print("\n")
    print(b2_x)
   
    print("\n")
    print(rvector)
    
    for w in rvector: 
        if w in b1_x: l1.append(1) 
        else: l1.append(0) 
        if w in b2_x: l2.append(1) 
        else: l2.append(0)
        
    print("\n")
    print(l1)
    print("\n")
    print(l2)
    c = 0
    d = 0
    e = 0
    
    for i in range(len(rvector)): 
        c+= l1[i]*l2[i]
        d+= l1[i]**2
        e+= l2[i]**2
    d=float(d**0.5)
    e=float(e**0.5)
    cosine=float(c/(d*e))
    print("\n")
    print(b1_x)
    print("\n")
    print(b2_x)
    print("\n")
    print(cosine)

coseno()
