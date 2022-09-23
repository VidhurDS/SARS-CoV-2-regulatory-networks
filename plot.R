data <- as.matrix(read.table("top_mir_expression_merged.txt", header=TRUE, sep="\t"))
heatmap(data)
data2 = normalize.quantiles(data)

library(ggplot2)