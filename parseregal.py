import sys


file1 = sys.argv[1]
file2 = sys.argv[2]

# Push top 5 then top 20 motifs in a list to compare
#single list pushing to get top kmer
def getlist(file,top):
    liste = []
    cpt=1
    with open(file) as f :
       
        for line in f:
             data =line.split( )
             if cpt <= top :
                 #print data[0]
                 liste.append(data[0])
                 cpt+=1
    return liste
                
top5_1 =getlist(file1,5)
top5_2 = getlist(file2,5)
top20_1 = getlist(file1,20)
top20_2 = getlist(file2,20)
#compare the rank of each kmer
def identical_hm(L1,L2,top):
    cpt =0
    if top ==5 :
        cpt_ad =20
    if top == 20 :
        cpt_ad = 5
    for i in range(top):
       
        if L1[i] == L2[i]:
            
            cpt= cpt+cpt_ad
    print cpt,"% of the top",top, " satellites are on the same order of occurences.\n"
    if top ==5:
        return (cpt/20)*2


#get the kmer with their repetive units
def presence_(file):
    list = []
    cpt =1
    with open(file) as f :
        
        
        for line in f :
            data= line.split()
            if cpt <= 20 :
                ndata = data[0]+data[1]
                list.append(ndata)
                cpt +=1

    return list

listcomp1 = presence_(file1)
listcomp2 = presence_(file2)

def top20_presence_(lt1,lt2):
    cpt = 0
    for i in lt1 :
        if i in lt2 :
            cpt +=1
    print "\nThe top 20 satellites of the 2 files share ",cpt,"same repetitive sequences.\n"
    cpt1=0

    for i in lt1[0:5]:
  
        if i in lt2[0:5] :
                cpt1+=1
    print "The top 5 satellites of the 2 files share ",cpt1,"same repetitive sequences.\n"
    return cpt*4.5

count_90 = top20_presence_(listcomp1,listcomp2)
count_10  = identical_hm(top5_1,top5_2,5)


howmuch2 = identical_hm(top20_1,top20_2,20)


print "The 2 files have a score of similarities of",count_90+count_10-1,"%\n" 







