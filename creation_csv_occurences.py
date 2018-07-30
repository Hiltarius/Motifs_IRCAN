#@author guillamaury debras
#creation d'un csv a partir de fichiers output de l'outil k_seek_4_2.pl
#recuperation du top 50,stockage des motifs et occurences
#recherche de 20 memes motifs dans le jeu commun selectionne ( sinon impossible #de clusteriser des motifs present dans un fichier mais pas dans les autres )


import os
from itertools import islice
import sys
import re


# parse the output in order to sort the tandems according to their counts
# on prends le top 50 pr voir une marge de maneouvre pour ola recherche des 20 memes motifs intra jeu de don#nees.


##### GET TOP 20 FILES #####


path = os.getcwd()
for input_file in os.listdir(path):
    if input_file.endswith(".total"):
        dico={}
        with open(input_file) as f :
            for line in f:
                data = line.split()
                dico[data[0]]=int(data[1])


        small_filename = 'total_sort_{}.txt'.format(input_file)

        file = open(small_filename,'w')

        for key, value in sorted(dico.iteritems(), key=lambda x: int(x[1]),reverse=True):   
            file.write( "%s    %s\n" % (key, value))

        file.close()

  
        with open(small_filename,"r") as myfile:
            head=list(islice(myfile,100))
      
        top50_file = 'top50_sort_{}.txt'.format(input_file)

        with open(top50_file,"w") as f2 :
            for item in head:
                f2.write(item)

        os.remove(small_filename)


        
#### DATA BASE CSV CREATION #####
bigdatabase={}
database = {}
listedb=[]
for input_file in os.listdir(path):
    if input_file.startswith("top50_"):
        with open(input_file) as f:
            liste =[]
            listeoccu=[]
            for line in f :
                data = line.split()
                liste.append(data[0])
                listeoccu.append(data[1])
            cpt=1
	    
            input_file = input_file[11:]
            input_file = input_file[:-10]
            database[input_file]={}
            bigdatabase[input_file]={}
            for i in liste :
                
        
                bigdatabase[input_file][i]=listeoccu[cpt-1]
                database[i]=listeoccu[cpt-1]
                cpt+=1
            listedb.append(database)
            database={}
            
#print bigdatabase
#print listedb

#recherche de  memes motifs dans tous les dictionnaires en partant des plus grandes occurences

keys = listedb[0].keys()
for dico in listedb[1:]:
    keys = [k for k in keys if k in dico]

    
result = [(k) for k in keys]
#result = [(k, [d[k] for d in listedb]) for k in keys]

#On a la liste des motifs similaires dans tous les echantillons.
# il faut maintenant creer le csv associe via le dico bigdatabase


def creation_csv(db,listmotif):
    
    lenl=len(listmotif)
    print("csv creation")
    csv = open("table_occurence.csv","w")
    firstline = ("accession;")
    for i in listmotif :
        firstline+=i+";"
    firstline = firstline[:-1]
    firstline+= "\n"
    csv.write(firstline)
    
    for key in db.keys():
        row=str(key)+";"
        for i in range(lenl):
            row+=db[key][listmotif[i]]+";"
        row = row[:-1]
        row+="\n"
        csv.write(row)
                   

creation_csv(bigdatabase,result)
  






