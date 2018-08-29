
#in order to properly display the paramters of the algorithm output
# we will display the motif its repetition the length of the final motif and the occurences of it

import sys
import os
input_file1 = sys.argv[1]


dico={}
with open(input_file1) as f :
    for line in f:
        data = line.split()
        dico[data[0]]=int(data[1])


small_filename = 'total_sort_{}.txt'.format(input_file1)

file = open(small_filename,'w')

for key, value in sorted(dico.iteritems(), key=lambda x: int(x[1]),reverse=True):
    
        file.write( "%s    %s\n" % (key, value))

file.close()
motif=[]
motif_repet = []
occurences=[]
t_motif=[]
# separate the number of time the motif is repeated on itself and the motif itself
final_file = 'final_file_{}.txt'.format(input_file1)
with open(small_filename, 'r') as input_file1, open(final_file, 'w') as output_file:
    for line in input_file1:
        
	#data = line.split('x')
        data = line.strip().split("    ")
        occurences.append(data[1])
        gg =data[0].split('x')
        motif.append(gg[0])
        motif_repet.append(gg[1])

cptlen = len(occurences)


#rajouter variable taille motif total

for i in range(cptlen) :
   vlen = int(len(motif[i]))
   repet = int(motif_repet[i])
   v_motif = vlen*repet
   t_motif.append(v_motif)


name =sys.argv[1]
name = name[:-12]
name= name+".csv"




def csv_create():
    cpt = len(motif)
    print("lets go")
    csv=open(name,"w")
    csv.write("Motif;Repetition;Taille Motif;Occurences\n")

    row =""
    for i in range(cpt):
       
        row+=str(motif[i])+";"+str(motif_repet[i])+";"+str(t_motif[i])+";"+str(occurences[i])+"\n"
    csv.write(row)
    print (" finit")
           

csv_create()

os.remove(small_filename)
os.remove(final_file)
    
