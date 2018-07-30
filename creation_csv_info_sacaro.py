# create a csv file with the supplementary data on the fastq files in order to merge them afterwards to try visualiting correlation between cluster and suppl info.
import sys

accession =["ERR1308614","ERR1309319","ERR1309153","ERR1309309","ERR1309425","ERR1308681","ERR1309094","ERR1308592","ERR1308770","ERR1309039","ERR1309405","ERR1309481","ERR1309373","ERR1308919","ERR1309216","ERR1309331","ERR1308950","ERR1308715","ERR1308915","ERR1309458","ERR1309162","ERR1309496","ERR1308955","ERR1308936","ERR1309521","ERR1309160","ERR1308745","ERR1309087","ERR1308911","ERR1308607","ERR1308872","ERR1309199","ERR1308868","ERR1309167","ERR1308750","ERR1308893","ERR1309305","ERR1308934","ERR1309511","ERR1309262","ERR1309464","ERR1309434","ERR1308720","ERR1309135","ERR1308671","ERR1309227","ERR1308931","ERR1309003","ERR1308705","ERR1309338","ERR1309082","ERR1308603","ERR1308665"]

standard=["ABR","BNV","BPB","BPT","BLT","BNL","ABE","ASG","AHR","ALG","CEN","AHA","CHS","CHT","ABD","CDC","CDD","CDE","ACD","ANC","ANK","AVI","ANF","ANG","AFH","AEP","CEV","CGN","BEH","ACM","BHR","BHS","BEF","CEK","CEL","ACK","ABM","AHM","AQA","AQD","ATQ","CGD","CGE","AID","AIE","ALT","BBK","ALS","BBH","BPQ","BQN","CBI","ACP"]
ecolo=["soil","soil","wine","wine","wine","soil","clinical","clinical","clinical","fruit","fruit","fruit","clinical","clinical","clinical","tree","tree","tree","tree","tree","tree","soil","soil","soil","distillery","distillery","distillery","fermentation","fermentation","fermentation","fermentation","fermentation","fermentation","fermentation","fermentation","palmwine","industrial","industrial","industrial","industrial","industrial","fruit","fruit","human","human","flower","flower","flower","flower","wine","wine","wine","wine"]
geo=["finland","turku_finland","i_italy","r_italy","slovenia","sweden","unknown","italy","romania","equador","unknown","costarica","france","france","USA","russia1","russia1","russia2","USA","USA","USA","USA","USA","USA","unknown","unknown","china","saig_southvi","taiwan","indonesia","laos","laos","china","tailand","tailand","ivorycoast","spain","spain","spain","spain","spain","UCD","UCD","unknow","portugal","zslovakia","zslovakia","lslovakia","lslovakia","malta","slovenia","exyugo","russia"]
clade=["eu","eu","eu","eu","eu","eu","eu","eu","eu","mosair3","mosair3","mosair3","mosair3","mosair3","mosair3","mosair3","mosair3","mosair3","NAoak","NAoak","NAoak","NAoak","NAoak","NAoak","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","asiaferm","alpechin","alpechin","alpechin","alpechin","alpechin","alpechin","alpechin","alpechin","alpechin","eu_sub1","eu_sub1","eu_sub1","eu_sub1","eu_sub1","eu_sub1","eu_sub1","eu_sub1"]


def transfo(liste):
    string=".fastq"
    liste = [s + string for s in liste]
    return liste
    

inputp = sys.argv[1]


## sacaro download accession and gbases from file
# ajouter

# faire ca fois 3, sois on multiplie par 3 par fonction sois on

#input1 = fibro
mbases=[]
accessionfile=[]
with open(inputp) as f :
    cpt = 0
    for line in f:
        line = line.strip().split("\t")
        accessionfile.append(line[9])
        mbases.append(line[7])
        cpt+=1
        if cpt == 1 :
            mbases.pop(0)
            accessionfile.pop(0)



for i in range(len(accession)):
	



def transfombase(liste):
    myint=1000.0
    liste = [int(s) / myint for s in liste]
    return liste
      
mbases = transfombase(mbases)
 

accession = transfo(accession)


def csv_create():
    cpt = len(accession)
    print("lets go")
    csv=open("tablesupldata.csv","w")
    csv.write("accession;standard_name;ecological;goegraphical;clades\n")

    row =""
    for i in range(cpt):
        row+=str(accession[i])+";"+str(standard[i])+";"+ str(ecolo[i])+";"+str(geo[i])+";"+ str(clade[i])+"\n"
    csv.write(row)
    print (" finit")
           

csv_create()
        
        
