###Statistical tests###
#The iris data set gives the measurements in centimeters of the variables sepal length and width and
#petal length and width, respectively, for 50 􀃙owers from each of 3 species of iris.

#1Use the summary() function to view some information about each column.
summary(iris)

#2Visualise the distribution of Sepal.Length , stratified by species.
#we want all plots in the same window, so we separate into different grids using par(), 2,2 creates a grid of 2 by 2
par(mfrow=c(2,2))
hist(iris[iris$Species == 'setosa', ]$Sepal.Length, breaks = 10, labels = FALSE, main = NULL, col = 'red')
hist(iris[iris$Species == 'versicolor', ]$Sepal.Length, breaks = 10, labels = FALSE, main = NULL, col = 'green')
hist(iris[iris$Species == 'virginica', ]$Sepal.Length, breaks = 10, labels = FALSE, main = NULL, col = 'blue')
par(mfrow=c(1,1))

#plot.new creates a completely new canvas = window
plot.new()
#we need this so that the x axis is adjusted, we first check the range of iris$Sepal.Length using the command below:
#range(iris$Sepal.Length), this gives us 4.3 and 7.9
plot.window(xlim = c(4, 8), ylim = c(0, 2))
#if you want to add lines to an existing plot, you have to use the line command
lines(density(iris[iris$Species == 'setosa', ]$Sepal.Length), col = 'red', main = NULL)
#alternative way to write this, and perhaps more understandable (because want to extract all rows (first bit) that contain setosa, and then the corresponding Sepal.Lengths)
#lines(density(iris[iris$Species == 'setosa', 'Sepal.Length']), col = 'red', main = NULL)
lines(density(iris[iris$Species == 'versicolor', ]$Sepal.Length), col = 'green', main = NULL)
lines(density(iris[iris$Species == 'virginica', ]$Sepal.Length), col = 'blue', main = NULL)
#now we will create the x-axis (1)
axis(side = 1, at = seq(4, 8))
#now we will create the y-axis (2)
axis(side = 2, at = seq(0, 2, 0.2))

#3Is Sepal.Length length normally distributed? Overall? Within each species?
#first test if the whole sepal length is normally distributed
shapiro.test(iris$Sepal.Length)
#the result is p-value = 0.01018, so we reject the null hypothesis, i.e. it is not normally distributed as a whole
shapiro.test(iris[iris$Species == 'setosa', ]$Sepal.Length)
shapiro.test(iris[iris$Species == 'versicolor', ]$Sepal.Length)
shapiro.test(iris[iris$Species == 'virginica', ]$Sepal.Length)
#but the individual data sets all have a high p-value (here often p > 0.1 is used), i.e. they are normally distributed, so that is really what we care about
plot(density(iris$Sepal.Length))

#4Is there a significant variation of Sepal.Length between the various species?
#as the individual data sets seem to be normally distributed, we can run an ANOVA
anova_iris <- aov(Sepal.Length ~ Species, data = iris) #we don't need to put iris before the Sepal.Length and Species here, because we give the dataframe afterwards
summary(anova_iris)
kruskal.test(Sepal.Length ~ Species, data = iris) 

#post hoc Tukey test for multiple comparisons
tukey_test <- TukeyHSD(anova_iris)
tukey_test
View(tukey_test$Species)
#the result is padj very close to 0 for all comparisons, so they are significantly different from each other
