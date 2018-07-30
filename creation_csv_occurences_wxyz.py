#@author guillamaury debras
#creation d'un csv a partir de fichiers output de l'outil k_seek_4_2.pl
#recuperation du top 100 ,stockage des motifs et occurences, taille et rang
#effectuer un nouveau top 100 en donnant du poids a chaque facteur selon la foem y = a*x + b*z + c*w + d * v
#recherche de memes motifs dans le jeu commun selectionne ( sinon impossible #de clusteriser des motifs present dans un fichier mais pas dans les autres )


import os
from itertools import islice
import sys
import re


def weight(motifw,repetx,occury,rankz,lenmotifl,internrepetl,occurencesl,rankingl):
    maxoccu = max(occurencesl)
    maxrank = max(rankingl)
    listmax=[]
    listmax.append(maxrank)
    listmax.append(maxoccu)    
    maxtwo= max(listmax)
    #get the len from motif list
    lenmotifl2 = []
    for i in lenmotifl:
        value = len(i)
        lenmotifl2.append(value)
    #convert str into int    
    internrepetl = [int(i) for i in internrepetl]

    #try having each factor at the same order lvl to not impact between eachother 
    adjustmotif = maxtwo
    adjustrep= maxtwo
    
    adjustrank = len(lenmotifl2)*5/100
    newrankvalue=[]
    
    for i in range(len(lenmotifl)):
        newvalue = motifw*(lenmotifl2[i]+adjustmotif)+ repetx*(internrepetl[i]+adjustrep)+occury*occurencesl[i]+rankz*(len(rankingl)-i)
        newrankvalue.append(newvalue)

    return newrankvalue





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

        motifliste=[]
        
        lenmotif=[]
        internrepet=[]
        occurences=[]
        ranking=[]
        #newrankvalue=[]
        for key, value in sorted(dico.iteritems(), key=lambda x: int(x[1]),reverse=True):
            occurences.append(value)
            motifliste.append(key)
        lenm = len(motifliste)
        cpt=1
        for i in range(lenm):            
            ranking.append(cpt)
            cpt+=1

        lenmotif = [i.split('x')[0] for i in motifliste]
        internrepet = [i.split('x')[1] for i in motifliste]

        #get the newlist with value from equation
        
        newrankvalue = weight(1,1,1,1,lenmotif,internrepet,occurences,ranking)
        #print newrankvalue
	#print motifliste
        
        #sort every lists according to newvaluelist
        
        zipped = list(zip(newrankvalue, motifliste, occurences))
	zipped.sort(reverse=True)
        #write the new list order into file
        newrankvalue, motifliste, occurences = zip(*zipped)
	#print "newsorted"
	#print newrankvalue
	#print motifliste
        for i in range(len(motifliste)):
        
            file.write( "%s    %s\n" % (motifliste[i], occurences[i]))
            
        file.close()

        #prends le top 100 only et cree un nouveau fichier en enlevant l'ancien
  
        with open(small_filename,"r") as myfile:
            head=list(islice(myfile,1000))
      
        top50_file = 'top50_sort_{}.txt'.format(input_file)

        with open(top50_file,"w") as f2 :
            for item in head:
                f2.write(item)

        os.remove(small_filename)



        
#creation DATABASE
        
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
    csv = open("table_occurence_wxyz.csv","w")
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
