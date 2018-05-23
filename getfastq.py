#@author Guillamaury Debras
# The script called getfastq aims to get fastqfiles from a list using the fastq commands and then applys the perl script called k_seek_4.pl to extract a list of repetitive sequences, once this is completed, the downloaded fastq files is destroyed to free the space usage.

import subprocess as sp
import multiprocessing
import time
# Because we cannot take random files and because the automated research is not trustworthy we decided to select manually each files and put them into a list.

listfile = ["SRR7171661","SRR7171662","SRR7171663","SRR7171664","SRR7171665","SRR7171666","SRR7171667","SRR7171668","SRR7171669","SRR7171670","SRR7171671","SRR7171672","SRR7171673","SRR7171674","SRR7171675","SRR7171676","SRR7171677","SRR7171678","SRR7171679"]
ncpu = 3
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
def commandline(accession):
    
    sp.call(['fastq-dump',accession])

    return 0 
def split_process(liste,cpu):
    
    pool = multiprocessing.Pool(processes=cpu)

    pool.map(commandline,liste)
    
    

split_process(listfile,ncpu)


