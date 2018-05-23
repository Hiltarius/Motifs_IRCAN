# parse the output in order to sort the tandems according to their counts

from itertools import islice
import sys
import re
import os
## Big file parsing
input_file = sys.argv[1]

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

## Top 100 parsing file  
with open(small_filename,"r") as myfile:
    head=list(islice(myfile,100))
      
top100_file = 'top100_sort_{}.txt'.format(input_file)

with open(top100_file,"w") as f2 :
    for item in head:
        f2.write(item)

# separate the number of time the motif is repeated on itself and the motif itself
top100_file1 = 'top_100_sort_{}.txt'.format(input_file)
with open(top100_file, 'r') as input_file1, open(top100_file1, 'w') as output_file:
    for line in input_file1:
   
	data = line.split('x')
        for item in data :
            output_file.write(" "+item)
      


#create custom outputfile
def customfile(f,s):
    kmer=0
    repeat=0
    yn = raw_input("do you want to keep only certain length of kmer y/n ?\n")
    if yn == "y" :
        kmer = input(" what is the minimun length of unit satellite you want example ATGG = 4 ?\n")
    yn2 = raw_input("do you want to fix a minimun number of repetition per satellite ? y/n ?")
    if yn2 == "y" :
        repeat = input(" what is the minimun repetition you want per satellite example ATTATTATT = 3 * ATT?\n")
    top100_file_perso = 'custom_minkmer_minrep{}.txt'.format(s)
    if kmer != 0 or repeat !=0 :
        with open(top100_file1, 'r') as f, open(top100_file_perso, 'w') as out:
            out.write(" unit sequence   repetition of the sequence  occurences of the repeated sequences  \n")
            for line in f:
                data= line.split()
                #print data
                if len(data[0]) >= kmer and int(data[1]) >= repeat :
                    #print data[0]
                    #print data[1]
                    out.write(line)        
        print "\n             parsing completed, you can obtain top 100 output at \n"
        print  "            ",top100_file1,"           \n"     
            
    print "\n             parsing completed, you can obtain top 100 customed parsing at \n"
    print  "            ",top100_file_perso,"           \n"

    print "\n             parsing completed, you can obtain the whole output at\n"
    print  "            ",small_filename,"           \n"

         
customfile(top100_file1,input_file)

os.remove(top100_file)



    
