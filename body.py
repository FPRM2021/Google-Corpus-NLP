from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
import re,string
#import connect
import io


def removeval(list1,list2): 
    for i in list1:
        for j.next(i) in list1:
            if j==i:
                list1.pop(j)
                list2.pop(j)

def recorrido():
##    cueck=0
##    dictionary=dict.fromkeys(nltk.words(),None)
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
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "Gag39054",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "bd2")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")

        postgres_insert_query= """select st1.stem, st2.stem, b.valor from bigrama b join 
                                    stems st1 on b.id_stem_1=st1.id_stem join
                                    stems st2 on b.id_stem_2=st2.id_stem join
                                    relacion r1 on st1.id_stem=r1.id_stem join
                                    relacion r2 on st2.id_stem=r2.id_stem
                                    where r1.palabras=%s"""
        ltmp1=[]
        ltmp12=[]
        ltmp2=[]
        ltmp22=[]

        cursor.execute(postgres_insert_query, (word1,))
        fetch1=cursor.fetchall()
        for line in fetch1:
            word=line.split()
            ltmp1.append(word[1])
            ltmp12.append(int(word[2]))
        removeval(ltmp1,ltmp2)

        cursor.execute(postgres_insert_query, (word2,))
        fetch2=cursor.fetchall()
        for line in fetch2:
            word=line.split()
            ltmp2.append(word[1])
            ltmp22.append(int(word[2]))
        removeval(ltmp2,ltmp22)
        
        # X = input("Enter first string: ").lower() 
        # Y = input("Enter second string: ").lower() 
  
        # tokenization 
        #X_list = word_tokenize(X)  
        #Y_list = word_tokenize(Y) 
  
        # sw contains the list of stopwords 
        sw = stopwords.words('english')  
        l1 =[];l2 =[] 
  
        # remove stop words from string 
        #X_set = {w for w in ltmp1 if not w in sw}  
        #Y_set = {w for w in ltmp2 if not w in sw} 
  
        # form a set containing keywords of both strings  
        rvector = ltmp1.union(ltmp2)
        for w in rvector: 
            if w in X_set:
               l1.append(ltmp12)
               ltmp12.pop(0) # create a vector 
            else: l1.append(0) 
            if w in Y_set: 
               l2.append(ltmp22) 
               ltmp22.pop(0)
            else: l2.append(0) 
        c = 0
  
        # cosine formula  
        for i in range(len(rvector)): 
                c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
        print("similarity: ", cosine) 
            
        connection.commit()
    

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL: ", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")