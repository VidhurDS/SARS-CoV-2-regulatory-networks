# Libraries
library(ggplot2)
library(dplyr)

# Load dataset from github
data <- read.table("miRNA_frequency_plot_input_4.txt", header=TRUE, sep="\t")
#View(data)

data %>%
  arrange(genome) %>%
  mutate(miRNA = factor(miRNA, levels=c("MIR548K", "MIR4659B", "MIR376C", "MIR376A1", "MIR4662B", "MIR548AS", "MIR548AQ", "MIR548AU", "MIR548AR", "MIR1282", "MIR514A3", "MIR514A2", "MIR920", "MIR5006", "MIR1976", "MIR3972", "MIR5195"))) %>%
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
