###Testing & Multiple testing correction###
#1For each gene (i.e. row) in logcounts.csv , use cell_metadata.csv and a statistical test of your
#to identify gene differentially expressed in cells infected with Salmonella relative to the
#control uninfected cells.
data.logc <- read.csv("data/logcounts.csv", row.names = 1) #row.names = 1 is needed for the gene ID to be the name of the row names
View(data.logc)

data.logc = as.matrix(data.logc)

data.cellm <- read.csv("data/cell_metadata.csv", row.names = 1)
View(data.cellm)

#we'll transpose it first, so we can then combine it
data.logc_transposed <- t(data.logc)
View(data.logc_transposed)

#check if the order of the names match, and then make sure they are equal
all(row.names(data.logc_transposed) == row.names(data.cellm))
cell_names <- row.names(data.logc_transposed)
data.cellm <- data.cellm[cell_names, ]

#we'll now combine it, so the groups of treatment are added to the individual cells (NO IDEA WHY WE NEED THE INFECTION HERE, FOR AN OBSCURE REASON WE ALSO NEED as.data.frame here)
data.combined <- cbind(Infection = data.cellm, as.data.frame(data.logc_transposed))
View(data.combined)

#now we can run a t-test for just one gene
t.test(ENSG00000131203 ~ Infection, data = data.combined)




#solution without dataset combining and no transposing because we ran into an issue above
data.logc <- read.csv("data/logcounts.csv", row.names = 1) #row.names = 1 is needed for the gene ID to be the name of the row names
View(data.logc)
data.cellm <- read.csv("data/cell_metadata.csv", row.names = 1)
View(data.cellm)

data.logc = as.matrix(data.logc)

test_row <- function(index, matrix) {
  test_data <- data.frame(
    value = as.numeric(matrix[index, ]),
    group = data.cellm$Infection)
  out <- wilcox.test(value ~ group, test_data)
  out$p.value
}

#just to test that the function works
X <- test_row(1, data.logc)
X

#we now create a rowselect thing which contains the number of all rows as a vector
rowselect <- seq(1, nrow(data.logc), 1) 
rowselect 

#numeric can be used to create a vector of length 1 with the value 0
#we now apply the function (test_row) to iterate over rows = genes (defined in rowselect) in our log count file, 
#matrix is required for the function and is data.logc in our case
p_values <- vapply(rowselect, test_row, FUN.VALUE = numeric(1), matrix = data.logc) 
p_values

#2visualise a bar plot of the p-values


