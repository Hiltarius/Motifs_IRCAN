import sys
"""
@author guillamaury debras
Create a csv file out of the ncbitableinfo.txt by extracting the desired parameters.
"""
inputp = sys.argv[1]

centre=[]
instrument=[]
popul=[]
sex=[]
library=[]
accession=[]
sample=[]
mbases=[]
with open(inputp) as f :
    cpt = 1
    for line in f:
        line = line.strip().split("\t")
    
        centre.append(line[3])
        instrument.append(line[12])
        library.append(line[15])
        popul.append(line[26])
        sex.append(line[39])
        accession.append(line[23])
        sample.append(line[25])
	mbases.append(line[17])
        
        #print line[20]
library.pop(0)
popul.pop(0)
instrument.pop(0)
centre.pop(0)
sex.pop(0)
accession.pop(0)
sample.pop(0)
mbases.pop(0)



def transfo(liste):
    string=".fastq"
    liste = [s + string for s in liste]
    return liste
     
accession = transfo(accession)


def transfombase(liste):
    myint=1000.0
    liste = [int(s) / myint for s in liste]
    return liste
      
mbases = transfombase(mbases)
print mbases

def csv_create():
    cpt = len(accession)
    print("lets go")
    csv=open("tablesupldata1000genome2.csv","w")
    csv.write("accession;centre;instrument;population;library;sex;sample;Gbases\n")

    row =""
    for i in range(cpt):
        row+=str(accession[i])+";"+str(centre[i])+";"+str(instrument[i])+";"+str(popul[i])+";"+str(library[i])+";"+str(sex[i])+";"+str(sample[i])+";"+str(mbases[i])+"\n"
    csv.write(row)
    print (" finit")
           

csv_create()



