library(ggplot2)
library(dplyr)
install.packages("RColorBrewer")
library(RColorBrewer)
RBP_freq = read.table("RBP_frequency.txt", header = TRUE, sep = "\t", dec = ".")
cutoff = 18
top_RBP = data.frame(top_n(RBP_freq, cutoff, Frequency))
sorted_top_RBP = top_RBP[order(-top_RBP$Frequency),]
s2 = sorted_RBP_freq
View(s2)

p = ggplot(sorted_top_RBP, aes(x=reorder(RBP, -Frequency), y=Frequency), fill= factor(RBP))+
  xlab("RBPs")+ 
  theme(axis.text.x = element_text(angle = 45, hjust = 1))+
  ggtitle("Human RBP motif occurance across SARS-CoV2")+
  geom_bar(aes(fill = reorder(RBP, -Frequency)),stat = "identity",show.legend = FALSE) + 
  scale_fill_manual(values = colorRampPalette(brewer.pal(11,"RdYlGn"))(26))

pdf(file = "Top_25percent_RBP_frequency.pdf",width = 6, height = 4) 
p
dev.off()


#+ 
#ggtitle("Human RBP Binding motif occurance across SARS-CoV2")+
#  xlab("RBPs")+ 
#  theme(axis.text.x = element_text(angle = 90, size=5, hjust = 1))
#RBP_freq = data.frame(read.table("RBP_frequency.txt", header = TRUE, sep = "\t", dec = "."))
#View(order(RBP_freq$Frequency))
#sorted_RBP_freq = RBP_freq[order(-RBP_freq$Frequency),]
#View(sorted_RBP_freq)
