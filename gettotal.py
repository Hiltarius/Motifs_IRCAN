#@author Guillamaury Debras
# The script called gettotal aims to get an output as a txt file using the k_seek_4.pl script. this getotal script'll take a list of previous downloaded fastqfiles and multiprocess them.

import subprocess as sp
import multiprocessing
import time

"""
#first 20 data -> pigmentos cockayne
listfile = ["SRR7171661","SRR7171662","SRR7171663","SRR7171664","SRR7171665","SRR7171666","SRR7171667","SRR7171668","SRR7171669","SRR7171670","SRR7171671","SRR7171672","SRR7171673","SRR7171674","SRR7171675","SRR7171676","SRR7171677","SRR7171678","SRR7171679","SRR7171680"]
"""

#second set of 20 data sierra leone
listfile =["ERR1602668","ERR1602667","ERR1602666","ERR1602665","ERR1602664","ERR1602663","ERR1602662","ERR1602661","ERR1602660","ERR1602659","ERR1602658","ERR1602657","ERR1602656","ERR1602655","ERR1602654","ERR1602653","ERR1602652","ERR1602651","ERR1602650","ERR1602649"]

ncpu = 20


def addfastq(list):
    string = ".fastq"
    my_new_list = [x + string for x in list]
   
    return my_new_list



def commandline(accession):
    
    sp.call(['perl','k_seek_4.pl',accession,accession])

    return 0 
def split_process(liste,cpu):
    
    pool = multiprocessing.Pool(processes=cpu)

    pool.map(commandline,liste)
    
    
listfileq =addfastq(listfile)

split_process(listfileq,ncpu)
