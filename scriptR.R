

library(klaR)
library(ggplot2)
#database = read.csv(file = "table.csv", sep = ";", dec=".",header = TRUE)
#database<-data.matrix(database[,2:21])
#database
#result <- kmodes(database, 3, iter.max = 10, weighted = FALSE)

#result

#plot(database,col=result$cluster)
#plot(jitter(database), col= result$cluster)

#plot(jitter(x), col = cl$cluster) points(cl$modes, col = 1:5, pch = 8)

# DEUXIEME TRY CLUSTER
library(cluster)

database = read.csv(file = "table.csv", sep = ";", dec=".",header = TRUE)
database<-data.frame(database)

#database <- database[,2:21]
#matrice dissimilarité
gower.dist <- daisy(database[,2:21], metric = c("gower"))

# complete agglomerative
aggl.clust.c <- hclust(gower.dist, method = "complete")
plot(aggl.clust.c,
     main = "Agglomerative, complete linkages")

#complete divisive
#------------ DIVISIVE CLUSTERING ------------#
divisive.clust.c <- diana(as.matrix(gower.dist), 
                        diss = TRUE, keep.diss = TRUE)
plot(divisive.clust.c, main = "Divisive")

# dendrocolo

# let's start with a dendrogram
library("dendextend")
library("ggplot2")
library("reshape2")
library("purrr")
library("dplyr")
dendro <- as.dendrogram(divisive.clust.c)

dendro.col <- dendro %>%
  set("branches_k_color", k = 5, value =   c("gold3", "darkslategray4", "darkslategray3", "gold3", "darkcyan", "cyan3", "gold3")) %>%
  set("branches_lwd", 0.6) %>%
  set("labels_colors", 
      value = c("darkslategray")) %>% 
  set("labels_cex", 0.5)

ggd1 <- as.ggdend(dendro.col)

ggplot(ggd1, theme = theme_minimal()) +
  labs(x ="Observations", y = "Height", title = "Dendrogram, k = 5")

savePlot("dendo60","png")

#PLot circulaire
# Radial plot looks less cluttered (and cooler)
ggplot(ggd1, labels = T) + 
  scale_y_reverse(expand = c(0.2, 0)) +
  coord_polar(theta="x")

savePlot("circular","png")



#add clusternumber to database for later heatmap

#pour agnes c clust.num <- cutree(divisive.clust.c, k = 5)
#pour diana c cutree(as.hclust(res.diana), k = 4)

clust.num <- cutree(as.hclust(divisive.clust.c), k = 5) 
database <- cbind(database, clust.num)

clusplot(database, clust.num, 
         color=TRUE, shade=TRUE, labels=0, lines=0, 
         main = "Customer clusters (k=7)", 
         cex = 0.3)

#Heatmap
#"AAAAAATx2","top1","top2","top3","top4", "top5", "top6","top7", "top8", "top9", "top10","top11", "top12", "top13","top14","top15","top16","top17","top18","top19","top20"

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
  geom_hline(yintercept = 3.5) + 
  geom_hline(yintercept = 10.5) + 
  geom_hline(yintercept = 13.5) + 
  geom_hline(yintercept = 17.5) + 
  geom_hline(yintercept = 21.5) + 
  scale_fill_gradient2(low = "darkslategray1", mid = "yellow", high = "turquoise4")

heatmap.p



#### fake data




test = distinct(database, top1)
test

list <- unique(list("GAATGx4","TTCCAx3","CCCCCAGCx2","AATGGx2","AAAAAATx2","ggbogoss","ggbogoss"))

list <-as.character(unique(unlist(database[,2:21])))
list

