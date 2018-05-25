# coding: utf-8
# @autheur guillamaury debras
# script permettant de générer un fichier csv contenant la totalité des fichiers de sorties de l'algorithme K_seek_4.pl.
# le fichier csv comprends le numéro d'accession de chaque fichier avec 20 paramètres, chaque paramètre représentant la position de chaque motif parmis le top 20
#Ceci afin de pouvoir obtenir un cluster des différents motifs affichés en fonction du top 20 des motifs.
#Les paramètres etant de l'ordre catégorical, il faudra réaliser un clustering adapté ( extension de l'algorithme k means)



import os
from itertools import islice
import sys
import re

# parse the output in order to sort the tandems according to their counts



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
            head=list(islice(myfile,20))
      
        top20_file = 'top20_sort_{}.txt'.format(input_file)

        with open(top20_file,"w") as f2 :
            for item in head:
                f2.write(item)

        os.remove(small_filename)



    


#### DATA BASE CSV CREATION #####
database = {}

for input_file in os.listdir(path):
    if input_file.startswith("top20_"):
        with open(input_file) as f:
            liste =[]
            for line in f :
                data = line.split()
                liste.append(data[0])
            cpt=1
	    
            input_file = input_file[11:]
            input_file = input_file[:-10]
            database[input_file]={}
            for i in liste :
                
	        #print i 
                print input_file
                database[input_file]["top"+str(cpt)]=i
                
                cpt+=1
            print database[input_file]

def creation_csv(db):
    
    print("csv creation")
    csv =open("table.csv", "w")
    csv.write("accession;top1;top2;top3;top4;top5;top6;top7;top8;top9;top10;top11;top12;top13;top14;top15;top16;top17;top18;top19;top20\n")
    cpt = 20
    for key in db.keys():
        
        row=str(key)+";"

        for i in range(cpt) :
            row +=db[key]["top"+str(i+1)]+";"
        row = row[:-1]    
        row += "\n"
        csv.write(row)
  
    
    
    
creation_csv(database)





