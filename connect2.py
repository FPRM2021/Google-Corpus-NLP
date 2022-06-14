import psycopg2
from nltk.corpus import words as nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
import re,string
import io

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

    postgres_insert_query1= """INSERT INTO stems (stem) VALUES (%s) ON CONFLICT (stem) DO NOTHING"""
    postgres_insert_query2= """INSERT INTO bigrama (id_stem_1, id_stem_2, valor) VALUES ((SELECT st.id_stem FROM stems st WHERE st.stem LIKE %s), (SELECT st.id_stem FROM stems st WHERE st.stem LIKE %s),%s)"""
    postgres_insert_query3= """INSERT INTO relacion (id_stem,palabras) VALUES ((SELECT st.id_stem FROM stems st WHERE st.stem LIKE %s),%s) ON CONFLICT (palabras) DO NOTHING"""
    ext=".txt"
    line="hola"
    ps = PorterStemmer()
    for i in range(8,9):
        with open('filtrados/outputs'+str(i)+ext, 'r', encoding="ANSI") as openfile:
            for line in openfile:
                word=line.split()
                stm1=ps.stem(word[0].lower())
                stm2=ps.stem(word[1].lower())
                record_to_insert1 = (stm1,)
                record_to_insert12 = (stm2,)
                record_to_insert2 = (stm1, stm2, int(word[2]))
                record_to_insert3 = (stm1, word[0].lower())
                record_to_insert32 = (stm2, word[1].lower())

                cursor.execute(postgres_insert_query1, record_to_insert1)
                cursor.execute(postgres_insert_query1, record_to_insert12)
                cursor.execute(postgres_insert_query2, record_to_insert2)
                cursor.execute(postgres_insert_query3, record_to_insert3)
                cursor.execute(postgres_insert_query3, record_to_insert32)
            connection.commit()
        openfile.close()
    

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL: ", error)
finally:
    #closing database connection.
        if(connection):
            print(line,'\t')
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")