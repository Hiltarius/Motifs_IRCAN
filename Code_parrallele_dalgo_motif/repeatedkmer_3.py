import os,sys,itertools
from itertools import (takewhile,repeat)
import time
import threading, multiprocessing
from multiprocessing import Process, Manager
import subprocess, tempfile
import shutil
#Program allowing to parse fastqfiles reads and output every permutations of given length k
#with their respective count
#Paramaters length of fastq reads,kmer length, % of coverage per read, name of fastqfile
#@author : Guillamaury Debras
#@supervisor : Olivier Croce

def Presentation():
    
    print("Hello, the command takes 4 arguments\n")
    print("first argument is the lenth of one read \n")
    print("second argument is the intial kmer length you want to search \n")
    print("third argument is the minimum  % of repeated kmer u want per read \n")
    print("fourth argument is the Fastq file you wanna parse \n")

Presentation()
    
len_read = int(sys.argv[1])
motifl = sys.argv[2]
motifl=int(motifl)
cover = sys.argv[3]
input_file = sys.argv[4]



# create the dictionnary of every possible kmers from the minimum % coverage read user wants.
# return the updated dictionnary
# list= permutation of motifs
# pour chaque objet dans la list 
def create_dico():
    base = 'ATCG'
    dico = Manager().dict()
    kmerlist= list(itertools.product(base,repeat=motifl))
    i = int(len_read)*int(cover)/100
    for j in kmerlist:
        motif = "".join(j)
        result= create_kmer(motif,i)
        print result
        dico[result]=0
     
    return dico

#create the repeated sequence for the given % of read we want
# return a string matching the given size we want of the repeated sequence

def create_kmer(moti,lenm):

    lenmotif =len(moti)
    taille = lenm/lenmotif
    taille += 1
    list = []
    i=0
    while i < taille :
        list.append(moti)
        i+=1
    kmer = "".join(list)
    while len(kmer)>lenm:
        kmer =kmer[:-1]


    return kmer


### algo Boyer Moore
#pre algorithm
#return a list of the suffix
def KMPpre(gene,pattern) :
 
    Bord =[-1] 
    j = 0
    for i in range(len(pattern)):
        while j >-1 :
            j = Bord[j]
           
        j +=1
        Bord.append(j)
    #print Bord
    return Bord


# research algorithm
# return the updated dictionnary with the different occurences as value
def KMrech(gene,pattern,liste):
    
    j = 0  
    result=[]   
    for i in range(len(gene)):
    
        while j >-1 and pattern[j] != gene[i]:
            j = liste[j]          
        j +=1
        if j== len(pattern):        
            dicoresult[pattern]+=1
            j = liste[j]
            print (i-len(pattern)+1)
    return dicoresult


## parsing throught every sequence at a time
#Solutions:

#Convert DictProxy to dict first then loop.
#good_d = dict(d)
#for k in good_d:
    
def Kmerprocess(input):
    cpt=0
    good_dico = dict(dicoresult)
    with open(input) as fileobject:
        for line in fileobject:
            pre = KMPpre(line,keylenght)
            cpt+=1
            print("finished",cpt)
            #for key in dicoresult:
            for key in good_dico:
                          
                KMrech(line,key,pre)


# allow us to get the number of lines of the file in order to properly cut of the splitbigfile function
#get the len of the file in order to  splitfiles
def file_len(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE, 
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])

#create temporary folder with files in it to avoid bugs
#split file into a number of files egal to cpu users wants to use

def splitbigfile(inputbig,cpunum,allline):
    print("Preparing files, please wait")
    list = []
    lines_per_file = allline/cpunum
    smallfile = None
    with open(inputbig) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = 'guiguifile_{}.txt'.format(lineno + lines_per_file)
                list.append(small_filename)
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
    print("Files prepared, ready to process")
    return list

#multiprocess on multiple files not multithread so transforming dict in to
#Manager().dict
## cant looper over manager dict so u have to
#Solutions:
#Convert DictProxy to dict first then loop.
#good_d = dict(d)
#for k in good_d:
# i did
def split_process(filelist,cpu):

    procss=[]
    
    pool = multiprocessing.Pool(processes=cpu)
    pool.map(Kmerprocess, [x for x in filelist])
    pool.close()
    pool.join()


#define number of cpu users want
def cpucount():
    numbercpuall = multiprocessing.cpu_count()
    while True :
        try :
            print "you have",numbercpuall,"at your disposal\n"
            cpu =input("how many cpu you want to use ?\n")
        except ValueError:
            print(" Are you sure you didn't do a mistake there sir ? try again pls.\n")
            continue
        except NameError :
            print(" I need a number not a letter\n")
            continue
        except SyntaxError :
            print(" I need a number sir\n")
            continue
        if cpu <=0:
            print("Sorry response must not be negative or equals to 0\n")
            continue
        if cpu > numbercpuall :
            print(" You can't use more cpu than you have, try again..\n")
        else : break
        
    return cpu

### destroy all small files with used before including the copy

def destroysmall():
    
    cwd = os.getcwd()
    my_dir = cwd
    for fname in os.listdir(my_dir):
        if fname.startswith("guiguifile"):
            os.remove(os.path.join(my_dir, fname))
        if fname.startswith("filetosplit"):
            os.remove(os.path.join(my_dir, fname))



#copy the entire input with only sequence in order to split without issues
def copy_sequencefile(fileinput):
    print("Curating file in progress, please wait...")
    file = open("filetosplit.txt",'w')
    
    with open(fileinput) as fileobject:
        for count, line in enumerate(fileobject, start=1):
            if count%4==2:
                file.write(line)
    print("curating sucessfull")
    return "filetosplit.txt"
 
# write the results key:value in a txt file    
def write_results(motifl):
    print("Writing results in progress...")
    lname =[]
    lname.append('kmer_length_')
    motifs=str(motifl)
    lname.append(motifs)
    lname.append("_coverage_")
    lname.append(cover)

    lname.append("%_result.txt")
    lna = "".join(lname)
    
    file = open(lna,'w')
    file.write("\n        ######   Repeatedkmer program results for a reads coverage at "+cover+" #####\n\n")
    file.write(" ######   This allows you to count the number of repeated sequences that cover "+cover+"% for each read #####\n\n")
    file.write("Kmer    :  final count\n\n")
    good_dico = dict(dicoresult)
    for key, value in sorted(good_dico.iteritems(), key=lambda x: int(x[1]),reverse=True):
        file.write( "%s  :  %s\n" % (key[0:motifl], value))
    
    print("         ####### Thank you for using our program #######\n")
    print("         ####### You can find your results at ########\n")
    print(  "               "+lna+"\n"     )


### pipe functions

dicoresult = create_dico()
keylenght = dicoresult.keys()[0]
input_file2 = copy_sequencefile(input_file)
numbercpu=cpucount()
lenfile= file_len(input_file2)
listfiles = splitbigfile(input_file2,numbercpu,lenfile)
split_process(listfiles,numbercpu)    
destroysmall()
write_results(motifl)




        


