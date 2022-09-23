library(ggplot2)
library(RColorBrewer)
library(dplyr)

fimo_out = read.table("Raj_fimo_2.tsv", header = TRUE, sep = "\t", dec = ".")
View(fimo_out)

theTable <- within(fimo_out,motif_alt_id <- factor(motif_alt_id,levels=names(sort(table(motif_alt_id),decreasing=TRUE))))
#ggplot(fimo_out, aes(x=reorder(motif_alt_id, -table(motif_alt_id)[motif_alt_id]))) + geom_bar()
View(theTable)


#v1
pdf(file = "all_RBP_frequency.pdf",width = 8, height = 4) 
ggplot(theTable,aes(x=motif_alt_id), color = motif_alt_id)+geom_bar()+ 
  ggtitle("Human RBP motif occurance across SARS-CoV2")+
  xlab("RBPs")+ 
  theme(axis.text.x = element_text(angle = 90, size=5, hjust = 1))
dev.off()
