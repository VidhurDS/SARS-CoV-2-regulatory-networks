# Libraries
library(ggplot2)
library(dplyr)

# Load dataset from github
data <- read.table("mir_binding_out_v2.txt", header=TRUE, sep="\t")
View(data)

data %>%
  arrange(genome) %>%
  mutate(miRNA = factor(miRNA, levels=c("hsa-miR-3591-3p", "hsa-miR-499b-3p", "hsa-miR-194-5p", "hsa-miR-520d-5p", "hsa-miR-1468-3p", "hsa-miR-548aj-5p", "hsa-miR-548x-5p", "hsa-miR-548g-5p", "hsa-miR-548f-5p", "hsa-miR-499a-3p", "hsa-miR-29a-3p", "hsa-miR-21-3p", "hsa-miR-3529-3p", "hsa-miR-5197-3p", "hsa-miR-548aj-3p", "hsa-miR-374a-3p", "hsa-miR-451b", "hsa-miR-2054", "hsa-miR-5688", "hsa-miR-8054", "hsa-miR-559", "hsa-miR-548j-3p"))) %>%
  ggplot( aes(x=genome, y=miRNA, fill=miRNA)) +
  geom_violin(show.legend = FALSE) +
  xlab("SARS-CoV-2 Genome (Normalized length)") + ylab("Human miRNAs")+
  stat_summary(fun=median, geom="point", size=2, color="red", show.legend = FALSE)

####
new_data = data[order(data$genome),]
View(new_data)
p= ggplot(new_data, aes(genome, miRNA, fill=miRNA)) +
  geom_violin(stat="identity", show.legend = FALSE) +
  scale_x_continuous()+
  stat_summary(fun=median, geom="point", size=2, color="red", show.legend = FALSE)
p
