

library(klaR)
library(ggplot2)


# DEUXIEME TRY CLUSTER
library(cluster)
library("dendextend")
library("ggplot2")
library("reshape2")
library("purrr")
library("dplyr")

# TABLE TOP20 60 data
database = read.csv(file = "table.csv", sep = ";", dec=".",header = TRUE)
#info des top 60 data
database2 = read.csv(file = "tablesupldatafibro.csv", sep = ";", dec=".",header = TRUE)
database = merge(database,database2, by ="accession")

#TABLE 1000GENOME PROJECT
database = read.csv(file = "table1000genome1.csv", sep = ";", dec=".",header = TRUE)
database2 = read.csv(file = "tablesupldata1000genome.csv", sep = ";", dec=".",header = TRUE)
#table 1000genome project part2
database_2 =  read.csv(file = "table1000genome2.csv", sep = ";", dec=".",header = TRUE)
database2_2 = read.csv(file = "tablesupldata1000genome2.csv", sep = ";", dec=".",header = TRUE)

#addition 2 dataframe successif
database = rbind(database,database_2)
database2 = rbind(database2,database2_2)

database = merge(database,database2, by ="accession")


#TABLE TOP50
database = read.csv(file = "table50.csv", sep = ";", dec=".",header = TRUE)
# SI TABLE 50 changer database[,2:51]

#table 80 data top 20
database = read.csv(file = "table80.csv", sep = ";", dec=".",header = TRUE)


database = read.csv(file = "table_sacharo.csv", sep = ";", dec=".",header = TRUE)
databasesup = read.csv(file = "tablesupldata.csv", sep = ";", dec=".",header = TRUE)
database = merge(database,databasesup, by ="accession")
databse= database[,-c(22)]

database<-data.frame(database)


#rownames pr les 60 humans
rownames(database) <- paste(database[,208],database[,210],rownames(database))
#rownames pr les sacaro
rownames(database) <- paste(database[,22],database[,23],database[,24],database[,25],database[,26],database[,27],rownames(database))
,weights=c(20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1)
gower.dist <- daisy(database[,2:21], metric = c("gower") )
gower.dist
# complete agglomerative
aggl.clust.c <- hclust(gower.dist, method = "complete")
plot(aggl.clust.c,
     main = "Agglomerative, complete linkages")
savePlot("aglo60","png")
#complete divisive

#------------ DIVISIVE CLUSTERING ------------#
divisive.clust.c <- diana(as.matrix(gower.dist), 
                        diss = TRUE, keep.diss = TRUE)
plot(divisive.clust.c, main = "Divisive Cluster Diana - gower dist")





savePlot("divisive60","png")
# dendrocolo

# let's start with a dendrogram


### dendo normal 
dendro <- as.dendrogram(divisive.clust.c)

dendro.col <- dendro %>%
  set("branches_k_color", k = 8, value =   c("gold3", "darkslategray4", "darkslategray3","blue","green", "gold3", "darkcyan", "cyan3", "red","cyan","red")) %>%
  set("branches_lwd", 0.9) %>%
  set("labels_colors",
      value = c("darkslategray")) %>% 
  set("labels_cex", 0.6)

ggd1 <- as.ggdend(dendro.col)

ggplot(ggd1, theme = theme_minimal()) +
  labs(x ="Observations", y = "Height", title = "Dendrogram, k = 8")

## fin dendo normal

### TO OBTAIN VIGNETTES TO ASSIGN EACH FACTOR
x = "#ffffff"
i <- 1
listb = list()
while(i<47){
  listb[[i]]<- x
  i <- i+1
}
str(listb)

## dendo labels colored


dend <- as.dendrogram(divisive.clust.c)
dend <- dend %>% 
  set("branches_k_color", k = 8, value =   c("purple", "darkslategray4", "darkslategray3","blue","green", "orange", "darkcyan", "cyan3", "red","cyan","red")) %>%
  #set("branches_lwd", 0.9) %>%
  #set("labels_colors", as.numeric(database[,22]), order_value = TRUE) %>%
  set("labels_cex", .9
  )

par(mar = c(3,1,1,25))

plot(dend,horiz=T)
title=("Satelittes Dendogram with clades differenciation")

n_instr1_types <- length(unique(database[,28]))
col_instr1_type <- colorspace::rainbow_hcl(n_instr1_types, c = 90, l  = 75)[database[,28]]
n_cell1_types <- length(unique(database[,29]))
col_cell1_type <- colorspace::rainbow_hcl(n_cell1_types, c = 90, l  = 75)[database[,29]]
n_instr2_types <- length(unique(database[,30]))
col_instr2_type <- colorspace::rainbow_hcl(n_instr2_types, c = 90, l  = 75)[database[,30]]
n_cell2_types <- length(unique(database[,32]))
col_cell2_type <- colorspace::rainbow_hcl(n_cell2_types, c = 90, l  = 75)[database[,32]]

colored_bars(cbind(col_instr1_type,listb,col_cell1_type,listb,col_instr2_type,listb,col_cell2_type), dend, 
             rowLabels = c(paste0("Center"),"","Sequence","","Population","","Gender"),horiz=TRUE,
             cex.rowLabels = 0.9)

savePlot("dendo_1000genome2_motif_wxyz","png")

#PLot circulaire
# Radial plot looks less cluttered (and cooler)
ggplot(ggd1, labels = T) + 
  scale_y_reverse(expand = c(0.2, 0)) +
  coord_polar(theta="x")

savePlot("circulark7","png")



#add clusternumber to database for later heatmap

#pour agnes c clust.num <- cutree(aggl.clust.c, k = 7)
#pour diana c cutree(as.hclust(res.diana), k = 7)
#clust.num <- cutree(aggl.clust.c,k=7)
clust.num <- cutree(as.hclust(divisive.clust.c), k = 2) 
str(clust.num)
database <- cbind(database, clust.num)

clusplot(database, clust.num, 
         color=TRUE, shade=TRUE, labels=clust.num, lines=0, 
         main = "Customer clusters (k=7)", 
         cex = 0.3)

#Heatmap
#"AAAAAATx2","top1","top2","top3","top4", "top5", "top6","top7", "top8", "top9", "top10","top11", "top12", "top13","top14","top15","top16","top17","top18","top19","top20"

list <-as.character(unique(unlist(database[,2:21])))
list
database[,2]

cust.long <- melt(data.frame(lapply(database, as.character), stringsAsFactors=FALSE), 
                  id = c("accession","clust.num"), factorsAsStrings=T)

cust.long.q <- cust.long %>%
  group_by(clust.num, variable, value) %>%
  mutate(count = n_distinct(accession)) %>%
  distinct(clust.num, variable, value, count)

# heatmap.c will be suitable in case you want to go for absolute counts - but it doesn't tell much to my taste

heatmap.c <- ggplot(cust.long.q, aes(x = clust.num, y =factor(value, levels = c(list), ordered = T))) +
  
  geom_tile(aes(fill = count))+
  scale_fill_gradient2(low = "darkslategray1", mid = "turquoise4", high = "red4")

# calculating the percent of each factor level in the absolute count of cluster members
cust.long.p <- cust.long.q %>%
  group_by(clust.num, variable) %>%
  mutate(perc = count / sum(count)) %>%
  arrange(clust.num)

heatmap.p <- ggplot(cust.long.p, aes(x = clust.num, y = factor(value, levels = c(list), ordered = T))) +
  
  geom_tile(aes(fill = perc), alpha = 0.85)+
  labs(title = "Distribution of motifs characteristics across clusters", x = "cluster", y = NULL) +

  scale_fill_gradient2(low = "darkslategray1",mid = "white", high = "red")

heatmap.p

savePlot("heatmap_1_80_k8","png")

#### fake data


#fonction qui calcule  le motif le plus représenté pour chaque topmotif de chaque type ou chaque cluster 
# faut juste modifier la variable qu'on veut modifier.
best<- aggregate(database[,2:21], list(type = database$type),
          function(x) names(which.max(table(x)))) 

 #traiter en fonction de chaque groupe de clustnum savoir combien ya de memes types de variables dans un cluster


#############
##########
#### deuxieme test matrice en fonction des occurences

database = read.csv(file = "table_occurence1000g1.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occurence1000g1et2.csv", sep = ";", dec=".",header = TRUE)

database_2 =  read.csv(file = "table1000genome2.csv", sep = ";", dec=".",header = TRUE)
database2 = read.csv(file = "tablesupldata1000genome2.csv", sep = ";", dec=".",header = TRUE)
#data genome2
database = read.csv(file = "table_occurence_motif_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occurence_occu_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occurence_repet_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
#data fibro,lympho,blood occurences
database = read.csv(file = "table_occurence_motif_fibrolympblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occurence_occu_fibrolympblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occurence_repet_fibrolympblood_wxyz.csv", sep = ";", dec=".",header = TRUE)

# data avc newrankvalue as value
# no need de diviser par gbases c deja fait via ce script
database = read.csv(file = "table_occu_rankvalues_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_repet_rankvalues_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_motif_rankvalues_wxyz.csv", sep = ";", dec=".",header = TRUE)

# data avc newrankvalue as value
# no need de diviser par gbases c deja fait via ce script
database = read.csv(file = "table_motif_rankvalues_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_occu_rankvalues_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_repet_rankvalues_1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
#data avc newrankvalue_2 as value
database = read.csv(file = "table_all_1111_rankvalues_2__1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_1511_rankvalues_2__1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_5111_rankvalues_2__1000genome2_wxyz.csv", sep = ";", dec=".",header = TRUE)

database = read.csv(file = "table_all_1122_rankvalues_2__fibrolymphoblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_1151_rankvalues_2__fibrolymphoblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_5111_rankvalues_2__fibrolymphoblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_1511_rankvalues_2__fibrolymphoblood_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_all_rankvalues_2__fibrolymphoblood_wxyz.csv", sep = ";", dec=".",header = TRUE)

database = read.csv(file = "table_1111__rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_1511__rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_5111__rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_1151__rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)

database = read.csv(file = "table_1511_top1000_rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_5111_top1000_rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_1151_top1000_rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)
database = read.csv(file = "table_1111_top1000_rankvalues_2__datasacaro_wxyz.csv", sep = ";", dec=".",header = TRUE)


database2 = read.csv(file = "tablesuplfibrobloodlymphombases.csv", sep = ";", dec=".",header = TRUE)
#INFO AVC 3 PARA EN +
database2 = read.csv(file = "tablesuplfibrobloodlymphombases_age_date_sexe.csv", sep = ";", dec=".",header = TRUE)
database2 = read.csv(file = "tablesuplsacaro.csv", sep = ";", dec=".",header = TRUE)



td = length(database)
if (td > 41 ) {
  database = database[,1:41]
}


database = merge(database,database2, by ="accession")
td = length(database)
td
#############
# pour script occurences only
#divide every counts per number of Gbases version occurences / nb bases
test =database[,2:(td-6)] / database$Gbases
test = ceiling(test)
database[,2:(td-6)]=test
### test pr monter tout au max gbases essai semble bon version rapporter occurences par max taille fichier
maxval = max(database[,td])

for(i in 1:length(database$Gbases)){
  if (database$Gbases[i] < maxval) {
    valueinter = database$Gbases[i]*100/maxval
    database[i,2:(td-6)] <- ceiling(database[i,2:(td-6)]*100/valueinter)  
  } 
}
#############
      
rownames(database) <- paste(database[,(td-2)],rownames(database))
database = data.frame(database)



### TO OBTAIN VIGNETTES TO ASSIGN EACH FACTOR
x = "#ffffff"
i <- 1
listb = list()
while(i<td+1){
  listb[[i]]<- x
  i <- i+1
}
#newlist for gender without color on undetermined sexe
col_cell_type3<- list()
colormale <- "#00ccff"
colorfemale <- "#ff6699"
nocolor <- "#ffffff"
for (i in 1:length(database$gender)){
  if (database[i,(td-1)] =="male"){
    col_cell_type3[[i]] = colormale    
  }
  else if (database[i,(td-1)] =="female"){
    col_cell_type3[[i]] = colorfemale    
  }
  else {
    col_cell_type3[[i]] =  nocolor    
  }
}


#n_instr_types <- length(unique(database[,td-5]))
#col_instr_type <- colorspace::rainbow_hcl(n_instr_types, c = 90, l  = 75)[database[,td-5]]
n_cell_types <- length(unique(database[,td-4]))
col_cell_type <- colorspace::rainbow_hcl(n_cell_types, c = 90, l  = 75)[database[,td-4]]
n_instr_types2 <- length(unique(database[,td-3]))
col_instr_type2 <- colorspace::rainbow_hcl(n_instr_types2, c = 90, l  = 75)[database[,td-3]]
n_cell_types2 <- length(unique(database[,td-2]))
col_cell_type2 <- colorspace::rainbow_hcl(n_cell_types2, c = 90, l  = 75)[database[,td-2]]
#n_cell_types3 <- length(unique(database[,td-1]))
#col_cell_type3 <- colorspace::rainbow_hcl(n_cell_types3, c = 90, l  = 75)[database[,td-1]]


dist.dist <- daisy(database[,2:(td-6)], metric = c("euclidean"))

aggl.clust.c <- hclust(dist.dist, method = "complete")

divisive.clust.c <- diana(as.matrix(dist.dist),
                          diss=FALSE, keep.diss = TRUE)

### tester si par cluster on a les memes parametres
clust.num <- cutree(as.hclust(divisive.clust.c), k = 2) 
str(clust.num)
database <- cbind(database, clust.num)

##########


# get info du nombre de fois qu'on retrouve each parametre par cluster
infoperclust <- database %>% group_by(gender, clust.num) %>% summarise(count=n())
# calcul du total d'individus par cluster
sumperclust = data.frame(aggregate(infoperclust$count, by=list(clust.num=infoperclust$clust.num), FUN=sum))
# regrouper les dataframe
resultclust = merge(infoperclust,sumperclust, by ="clust.num")
#faire la frequence
resultclust[,3] = resultclust[,3]/resultclust[,4]*100


for(i in 1:length(resultclust$count)){
  if (resultclust[i,3] > 95 ){
    message(" the Cluster ",resultclust[i,1]," has ",resultclust[i,3], " % of its individuals with the parameter " ,resultclust[i,2])
  }
}
################


## dendo labels colored

dend <- as.dendrogram(divisive.clust.c)
dend <- dend %>% 
  #set("branches_k_color", k = 5, value =   c("purple", "darkslategray4", "darkslategray3","blue","green", "orange", "darkcyan", "cyan3", "red","cyan","red")) %>%
  set("branches_lwd", 0.9) %>%
  #set("labels_colors", as.numeric(database[,36]), order_value = TRUE) %>%
  set("labels_cex", .9)

par(mar = c(10,5,1,5))
plot(dend)
#horiz=T
#coloredbars for 1000genome2
#colored_bars(cbind(col_instr_type,listb,col_cell_type,listb,col_instr_type2,listb,col_cell_type2), dend, 
 #           rowLabels = c(paste0("Center "),"", "Instr","","Population","","Gender"),horiz=TRUE,
  #         cex.rowLabels = 0.9)

#coloredbars for lymphobloodfibro
#colored_bars(cbind(col_instr_type,listb,col_cell_type,listb,col_instr_type2,listb,col_cell_type2,listb,col_cell_type3), dend, 
 #         rowLabels = c(paste0("Sequencing "),"", "Cellular","","date","","age","","gender"),horiz=FALSE,
  #         cex.rowLabels = 0.9)
#coloredbars for datsacaro
colored_bars(cbind(col_cell_type,listb,col_instr_type2,listb,col_cell_type2), dend, 
         rowLabels = c(paste0("ecological "),"","geographical","","clade"),horiz=FALSE,
           cex.rowLabels = 0.9)

title("")

database
savePlot("dendo_sacaro_1111_top1000_rankvalue_2_wxyz","png")
savePlot("dendo_60_occurences","png")

###
# rbind(data frame A, data frame B) pr adiitionner plusieurs dataframes entres pr le 1000genomeproject


