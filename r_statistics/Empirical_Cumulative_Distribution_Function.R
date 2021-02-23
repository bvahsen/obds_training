###Compute an Empirical Cumulative Distribution Function###
#1Use the ecdf() function to compute the empirical cumulative distribution function for the variable Sepal.Length in the iris data set.
#the ecdf is an inspection tool that gives you a function of the dataset, so you can plot it

iris
iris_ecdf <- ecdf(iris$Sepal.Length)


#2Use the plot() function to visualise the empirical cumulative distribution function.
plot(iris_ecdf)

#3Use the knots() function on the ecdf output and compare this with the list of unique values for the variable Sepal.Length.
knots(iris_ecdf)
#this can also be achieved using a combination of the sort and the unique function
sort(unique(iris$Sepal.Length))

#we can use this to calculate the probability of having a sepal length of 6 and below:
iris_ecdf(6)
