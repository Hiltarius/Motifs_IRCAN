# create a csv file with the supplementary data on the fastq files in order to merge them afterwards to try visualiting correlation between cluster and suppl info.

accession =["SRR7171680.fastq", "SRR7171678.fastq","SRR7171682.fastq", "SRR7171675.fastq", "SRR7171663.fastq", "SRR7171668.fastq", "ERR251402.fastq",  "SRR7171664.fastq", "ERR1602666.fastq", "ERR1602657.fastq", "SRR7171677.fastq", "ERR1602655.fastq", "ERR251379.fastq", "ERR251346.fastq", "SRR7171672.fastq","ERR251377.fastq",  "ERR251347.fastq",  "ERR1602661.fastq", "ERR1602651.fastq", "ERR1602667.fastq", "ERR1602660.fastq", "ERR251380.fastq","SRR7171683.fastq", "ERR1602658.fastq", "ERR251343.fastq",  "SRR7171676.fastq", "SRR7171665.fastq", "SRR7171662.fastq", "ERR251345.fastq", "ERR251403.fastq","ERR251325.fastq", "ERR1602664.fastq", "ERR1602649.fastq", "ERR1602656.fastq", "ERR1602663.fastq", "ERR251342.fastq","SRR7171674.fastq","ERR1602653.fastq", "ERR251401.fastq", "ERR251404.fastq",  "ERR251326.fastq",  "ERR251327.fastq",  "ERR251348.fastq",  "ERR251378.fastq","ERR251328.fastq",  "SRR7171661.fastq", "SRR7171669.fastq", "SRR7171666.fastq", "ERR1602668.fastq", "ERR251344.fastq",  "ERR251329.fastq","ERR1602662.fastq", "ERR1602652.fastq", "SRR7171671.fastq", "SRR7171667.fastq", "SRR7171673.fastq", "ERR1602650.fastq", "SRR7171679.fastq","SRR7171670.fastq", "ERR1602654.fastq", "ERR1602665.fastq", "ERR1602659.fastq"]

typep=["Xeroderma pigmentosum complement group C","Xeroderma pigmentosum complement group C","Cockayne syndrome type A","Cockayne syndrome type B","Normal","Normal neonatal","blood","Normal","lympho","lympho","Cockayne syndrome type B","lympho","blood","blood","Cockayne syndrome type B","blood","blood","lympho","lympho","lympho","lympho","blood","Cockayne syndrome type A","lympho","blood","Cockayne syndrome type A","Normal","Xeroderma pigmentosum complement group C","blood","blood","blood","lympho","lympho","lympho","lympho","blood","Cockayne syndrome type B","lympho","blood","blood","blood","blood","blood","blood","blood","Xeroderma pigmentosum complement group C","Normal neonatal","Normal","lympho","blood","blood","lympho","lympho","Cockayne syndrome type B","Normal neonatal","Cockayne syndrome type B","lympho","Xeroderma pigmentosum complement group C","Normal neonatal","lympho","lympho","lympho"]
      
print len(typep)
print len(accession)      

"""
def transfo(liste):
    string=".fastq"
    liste = [s + string for s in liste]
    return liste


      
accession = transfo(accession)
print sorted(accession)
"""




def csv_create():
    cpt = len(accession)
    print("lets go")
    csv=open("tablesupldatafibro.csv","w")
    csv.write("accession;type\n")

    row =""
    for i in range(cpt):
        row+=str(accession[i])+";"+str(typep[i])+"\n"
    csv.write(row)
    print (" finit")
           

csv_create()
