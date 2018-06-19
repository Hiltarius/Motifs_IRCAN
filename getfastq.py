#@author Guillamaury Debras
# The script called getfastq aims to get fastqfiles from a list using the fastq commands and then applys the perl script called k_seek_4.pl to extract a list of repetitive sequences, once this is completed, the downloaded fastq files is destroyed to free the space usage.

import subprocess as sp
import multiprocessing
import time
import sys
input_f = sys.argv[1]

# Because we cannot take random files and because the automated research is not trustworthy we decided to select manually each files and put them into a list.
"""
listfile = ["SRR7171661","SRR7171662","SRR7171663","SRR7171664","SRR7171665","SRR7171666","SRR7171667","SRR7171668","SRR7171669","SRR7171670","SRR7171671","SRR7171672","SRR7171673","SRR7171674","SRR7171675","SRR7171676","SRR7171677","SRR7171678","SRR7171679"]
"""

#second set of 20 data -> Human Genome Diversity Project
"""
listfile =["ERR1602668","ERR1602667","ERR1602666","ERR1602665","ERR1602664","ERR1602663","ERR1602662","ERR1602661","ERR1602660","ERR1602659","ERR1602658","ERR1602657","ERR1602656","ERR1602655","ERR1602654","ERR1602653","ERR1602652","ERR1602651","ERR1602650","ERR1602649"]
"""
"""
#third set of 20 data -> siera leone
listfile=["ERR251380","ERR251379","ERR251378","ERR251377","ERR251404","ERR251403","ERR251402","ERR251401","ERR251329","ERR251328","ERR251327","ERR251326","ERR251325","ERR251348","ERR251347","ERR251346","ERR251345","ERR251344","ERR251343","ERR251342"]
"""
"""
#fourth set of 20 data => papio anubis
listfile=["SRR6956852","SRR6956853","SRR6956854","SRR6956855","SRR6956856","SRR6956857","SRR6956858","SRR6956859","SRR6956860","SRR6956861","SRR6956862","SRR6956863","SRR6956864","SRR6956865","SRR6956866","SRR6956867","SRR6956868","SRR6956869","SRR6956870","SRR6956871"]
"""
#fifth set of data => S. cerevisiae 1011 genome project
"""
listfile=["ERR1308614","ERR1309319","ERR1309153","ERR1309309","ERR1309425","ERR1308681","ERR1309094","ERR1308592","ERR1308770","ERR1309039","ERR1309405","ERR1309481","ERR1309373","ERR1308919","ERR1309216","ERR1309331","ERR1308950","ERR1308715","ERR1308915","ERR1309458","ERR1309162","ERR1309496","ERR1308955","ERR1308936","ERR1309521","ERR1309160","ERR1308745","ERR1309087","ERR1308911","ERR1308607","ERR1308872","ERR1309199","ERR1308868","ERR1309167","ERR1308750","ERR1308893","ERR1309305","ERR1308934","ERR1309511","ERR1309262","ERR1309464","ERR1309434","ERR1308720","ERR1309135","ERR1308671","ERR1309227","ERR1308931","ERR1309003","ERR1308705","ERR1309338","ERR1309082","ERR1308603","ERR1308665"]
"""
"""
#data human cokayne a sample 2 and 3
listfile=["SRR7171683","SRR7171682"]
"""

#download from txt file
listfile=[]

with open(input_f) as f :
    for line in f:
	
        listfile.append(line)


listfile = list(map(lambda x:x.strip(),listfile))


ncpu = 20

def commandline(accession):
    
    sp.call(['fastq-dump',accession])

    return 0 
def split_process(liste,cpu):
    
    pool = multiprocessing.Pool(processes=cpu)

    pool.map(commandline,liste)
    
    

split_process(listfile,ncpu)



"""
def commandline(accession):
     sp.call(['fasq-dump','accession'])

def split_process(filelist,cpu):
    
    procss=[]
    

    pool = multiprocessing.Pool(processes=cpu)
    pool.map(commandline,listfile)
    pool.close()
    pool.join()
"""




