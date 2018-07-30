import sys
"""
@author guillamaury debras
Create a csv file out of the ncbitableinfo.txt by extracting the desired parameters. for the fibro lympho and blood files
"""
inputp = sys.argv[1]

inputp2=sys.argv[2]

inputp3 =sys.argv[3]


instrument=[]
accession=[]
mbases=[]
typep=[]
age=[]
releasedate=[]
sexe=[]

# faire ca fois 3, sois on multiplie par 3 par fonction sois on

#input1 = fibro
with open(inputp) as f :
    cpt = 0
    for line in f:
        line = line.strip().split("\t")
        typep.append(line[14])
        accession.append(line[8])
        mbases.append(line[5])
        instrument.append(line[27])
        releasedate.append(line[7])
        age.append(line[11])
        sexe.append(line[17])
        cpt+=1
        if cpt == 1 :
            mbases.pop(0)
            accession.pop(0)
            typep.pop(0)
            instrument.pop(0)
            releasedate.pop(0)
            age.pop(0)
            sexe.pop(0)


print " finit 1"

#blood = input 2          
with open(inputp2) as f :
    cpt = 0
    lenp = len(accession)
    print lenp
   
    for line in f:
        line = line.strip().split("\t")
        #typep.append(line[27])
        typep.append("whole blood")
        accession.append(line[14])
        mbases.append(line[11])
        #instrument.append(line[28])
        instrument.append("Illumina HiSeq 2000")
        releasedate.append(line[13])
        sexe.append(line[30])
        age.append("unknown")
        
        cpt+=1
        if cpt == 1 :
            mbases.pop(lenp)
            accession.pop(lenp)
            typep.pop(lenp)
            instrument.pop(lenp)
            releasedate.pop(lenp)
            sexe.pop(lenp)
            age.pop(lenp)

print "finit 2"
#lymphoblastoid = input 3         
with open(inputp3) as f :
    cpt = 0
    lenp = len(accession)
    print lenp
   
    for line in f:
        line = line.strip().split("\t")
        #typep.append(line[27])
        typep.append("lymphoblastoid")
        accession.append(line[13])
        mbases.append(line[10])
        #instrument.append(line[28])
        instrument.append("hiseqxten")
        releasedate.append(line[12])
        sexe.append(line[16])
        age.append("unknown")
        cpt+=1
        if cpt == 1 :
            mbases.pop(lenp)
            accession.pop(lenp)
            typep.pop(lenp)
            instrument.pop(lenp)
            releasedate.pop(lenp)
            sexe.pop(lenp)
            age.pop(lenp)

print "finit 3"


            

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

def transfosex(liste):
    for i in range(len(liste)) :
        
        if liste[i] == "male" or liste[i]=="female" :           
            continue
        else :
            liste[i] = ""
            print liste[i]
    return liste
            
         
sexe = transfosex(sexe)
print sexe

def csv_create():
    cpt = len(accession)
    print("lets go")
    csv=open("tablesuplfibrobloodlymphombases_age_date_sexe.csv","w")
    csv.write("accession;instrument;type;date;age;gender;Gbases\n")

    row =""
    for i in range(cpt):
        row+=str(accession[i])+";"+str(instrument[i])+";"+str(typep[i])+";"+str(releasedate[i])+";"+str(age[i])+";"+str(sexe[i])+";"+str(mbases[i])+"\n"
    csv.write(row)
    print (" finit")
           

csv_create()
