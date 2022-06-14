from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re,string
#import connect
import io
import psycopg2
import time


def removeval(list1,list2):
    unique1=[]
    unique2=[]
    for i in range(0,len(list1)):
        if list1[i] not in unique1:
            unique1.append(list1[i])
            unique2.append(list2[i])
    list1=unique1.copy()
    list2=unique2.copy()
    
def recorrido():
    for i in range(25,26):
        with io.open('corpus/'+str(i)+".txt","r",encoding="utf8") as openfile, io.open('output'+str(i)+".txt",'w',encoding="utf8") as f_output:
            print("Buscando "+str(i)+".txt")
            try:
                for line in openfile:
                    word=line.split()
                    if(wordnet.synsets(word[0].lower()) and wordnet.synsets(word[1].lower())):
                        f_output.write(line)
            except KeyError:
                continue
            finally:
                openfile.close()
                f_output.close()


def comparacion(word1,word2):
    if(wordnet.synsets(word1.lower()) == wordnet.synsets(word2.lower())):
        print("similarity: ",1)
    else:
        try:
            connection = psycopg2.connect(user = "postgres",
                                          password = "Gag39054",
                                          host = "127.0.0.1",
                                          port = "5432",
                                          database = "bd2")

            cursor = connection.cursor()

            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()

            #postgres_insert_query= """select st1.stem, st2.stem, b.valor from bigrama b join 
                                    #    stems st1 on b.id_stem_1=st1.id_stem join
                                     #   stems st2 on b.id_stem_2=st2.id_stem join
                                      #  relacion r1 on st1.id_stem=r1.id_stem
                                       # where r1.palabras=%s order by valor desc"""
            postgres_insert_query= """select st2.stem, sum(b.valor) 
                                        from bigrama b join 
                                        stems st1 on b.id_stem_1=st1.id_stem join
                                        stems st2 on b.id_stem_2=st2.id_stem join
                                        relacion r1 on st1.id_stem=r1.id_stem
                                        where r1.palabras=%s group by (st2.stem) order by sum(b.valor) desc"""
            ltmp1=[]
            ltmp12=[]
            ltmp2=[]
            ltmp22=[]

            cursor.execute(postgres_insert_query, (word1,))
        
            fetch1=cursor.fetchall() #CONVERSION A LISTA DE TUPLAS DE LOS DATOS DE LA BD
            connection.commit()
            for line in fetch1:
                ltmp1.append(line[0])
                ltmp12.append(int(line[1]))
            #removeval(ltmp1,ltmp12) #eliminar repetidos

            cursor.execute(postgres_insert_query, (word2,))
            fetch2=cursor.fetchall() #CONVERSION A LISTA DE TUPLAS DE LOS DATOS DE LA BD
            connection.commit()
            for line in fetch2:
                ltmp2.append(line[0])
                ltmp22.append(int(line[1]))
            #removeval(ltmp2,ltmp22) #eliminar repetidos
  
            l1 =[];l2 =[] 
  
            # form a set containing keywords of both strings  
            lset1=set(ltmp1)
            lset2=set(ltmp2)
            rvector = lset1.union(lset2)
        
            for w in rvector: 
                if w in lset1:
                    for i in range(0,len(ltmp1)):
                        if w==ltmp1[i]:
                            l1.append(ltmp12[i])
                else: l1.append(0)
            
                if w in lset2:
                    for i in range(0,len(ltmp2)):
                        if w==ltmp2[i]:
                            l2.append(ltmp22[i])
                else: l2.append(0) 
            c=0
            d=0
            e=0
            for i in range(len(rvector)): 
                c+= l1[i]*l2[i]
                d+= l1[i]**2
                e+= l2[i]**2
            cosine = (c / float((d*e)**0.5))
            if(cosine>1):
                cosine=1
            print('similarity: ',cosine)

        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to *PostgreSQL: ", error)
        finally:
            #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()


########

start_time = time.time()
#comparacion ('dog','dogs')
#comparacion ('dog','doggy')
#comparacion ('dog','dogs')
#comparacion ('dog','dogs')
#comparacion ('dog','hound')
comparacion ('doctor','medicine')
#comparacion ('dog','mongrel')
print ("\n My program took", time.time() - start_time, "to run")
