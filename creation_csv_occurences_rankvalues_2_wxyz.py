import sys

import os
from itertools import islice
import math
import re
from decimal import Decimal

"""
@author guillamaury debras
#creation_rank_value_2 new way to get the final rankvalue weight
# mettre en input les differents fichiers info d'un dataset 
#recuperation des listes respectives d accession et gbases
#recuperer le nom de chaque fichier resultat d output k_seek_4_2
#transdaridser mbases en gbases
# standardiser les occurrences de chaque fichiers avc les valeurs gabses respectives


"""



inputp = sys.argv[1]

accession=[]
mbases=[]



# data sacaro 
with open(inputp) as f :
    cpt = 0
    for line in f:
        line = line.strip().split("\t")
        accession.append(line[9])
	mbases.append(line[7])
	cpt+=1
	if cpt == 1:
	    mbases.pop(0)
            accession.pop(0)




"""
# 1000genome2
with open(inputp) as f :
    cpt = 0
    for line in f:
        line = line.strip().split("\t")
        accession.append(line[23])
	mbases.append(line[17])
	cpt+=1
	if cpt == 1:
	    mbases.pop(0)
            accession.pop(0)

"""
"""
# faire ca fois 3, sois on multiplie par 3 par fonction sois on

#input1 = fibro
with open(inputp) as f :
    cpt = 0
    for line in f:
        line = line.strip().split("\t")
        accession.append(line[8])
        mbases.append(line[5])
        cpt+=1
        if cpt == 1 :
            mbases.pop(0)
            accession.pop(0)

inputp2=sys.argv[2]

print " finit 1"

#blood = input 2          
with open(inputp2) as f :
    cpt = 0
    lenp = len(accession)
    print lenp
   
    for line in f:
        line = line.strip().split("\t")
        accession.append(line[14])
        mbases.append(line[11])

        cpt+=1
        if cpt == 1 :
            mbases.pop(lenp)
            accession.pop(lenp)


inputp3 =sys.argv[3]

print "finit 2"
#lymphoblastoid = input 3         
with open(inputp3) as f :
    cpt = 0
    lenp = len(accession)
    print lenp
   
    for line in f:
        line = line.strip().split("\t")
        accession.append(line[13])
        mbases.append(line[10])

        cpt+=1
        if cpt == 1 :
            mbases.pop(lenp)
            accession.pop(lenp)
print "finit 3"

"""





def transfombase(liste):
    myint=1000.0
    liste = [int(s) / myint for s in liste]
    return liste
      
mbases = transfombase(mbases)

def transfo(liste):
    string=".fastq"
    liste = [s + string for s in liste]
    return liste
      
accession = transfo(accession)
print accession






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
    # in order to give the same weight to each variable
    # motif between 5 and 20 so 16 differents values so 100/16
    # same operation for repetvalue between 2 and 30 so 100/30 can varry so we put the max instead
    motifvalue=6.25
    repetvalue=100/max(internrepetl)
    
    
    occuvalue = 100000*100/maxoccu
    rankvalue = 100000*100/max(rankingl)
    
    """
    if maxoccu > maxrank :
	print lenmotifl[25]
    	print ("value motif",((lenmotifl2[25]-4)*motifvalue*maxtwo/100 ))
	print "cb de repet",internrepetl[25]
    	print ("value repet",((internrepetl[25]-1)*repetvalue*maxtwo/100))
	print "maxoccu",maxoccu
    	print ("value occu", (occurencesl[25]))
	print "currentrank",(len(rankingl)-25)
	print "maxrank",maxrank
    	print ("value rank",((len(rankingl)-25)*rankvalue*maxtwo/100/100000))
    """
    if maxrank > maxoccu :
    	for i in range(len(lenmotifl)):
        	newvalue = motifw*((lenmotifl2[i]-4)*motifvalue*maxtwo/100 )+ repetx*((internrepetl[i]-1)*repetvalue*maxtwo/100)+occury*(occurencesl[i]*occuvalue*maxoccu/100/100000)+rankz*(len(rankingl)-i)
        	newrankvalue.append(int(math.ceil(newvalue)))

    if maxoccu > maxrank : 
	for i in range(len(lenmotifl)):
		newvalue = motifw*((lenmotifl2[i]-4)*motifvalue*maxtwo/100 )+ repetx*((internrepetl[i]-1)*repetvalue*maxtwo/100)+occury*(occurencesl[i])+rankz*((len(rankingl)-i)*rankvalue*maxtwo/100/100000)
        	newrankvalue.append(int(math.ceil(newvalue)))
		
		
    return newrankvalue




path = os.getcwd()
for input_file in os.listdir(path):
    if input_file.endswith(".total"):
        dico={}
        with open(input_file) as f :
            for line in f:
                data = line.split()
                dico[data[0]]=int(data[1])

        # ajout code pr le rankvalue a la place doccurences get name and maxgabses
        namefile = input_file[:-6]
        maxval = max(mbases)
        maxval = int(maxval)                  
        
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

        #standardiser les occurences
        for i in range(len(accession)) :
            if accession[i] == namefile and mbases[i] < maxval :
                valueinter = mbases[i]*100/maxval
                occurences = [ int(math.ceil(x*100/valueinter)) for x in occurences]
                
        
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
            file.write( "%s    %s\n" % (motifliste[i], newrankvalue[i]))
            #file.write( "%s    %s\n" % (motifliste[i], occurences[i]))
            
        file.close()
	
        #prends le top 100 only et cree un nouveau fichier en enlevant l'ancien
  	
        with open(small_filename,"r") as myfile:
            #num_lines = sum(1 for line in open(small_filename))
            #head=list(islice(myfile,num_lines))
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
    csv = open("table_1111_top1000_rankvalues_2__datasacaro_wxyz.csv","w")
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
