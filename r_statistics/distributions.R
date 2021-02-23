###Distributions###
#1Generate a vector of 1000 normally distributed values with mean 10 and standard deviation 5.
norm_dist <- rnorm(n = 1000, mean = 10, sd = 5)

#2Inspect the output of the summary() function for that vector.
summary(norm_dist)

#3Compute the mean and standard deviation for those values.
mean(norm_dist)
sd(norm_dist)

#4Compute the deciles (i.e. 10 evenly spaced quantiles) for those values.
quantile(norm_dist, probs = seq(0, 1, 0.1))

#5Visualise the distribution of those values as a histogram.
hist(norm_dist, breaks = 50)
#breaks tells us the number of bins in the graph

#6Visualise as vertical lines on the histogram: the mean (red solid), median (red dashed), one standard
#deviation from the mean (blue solid), and one median absolute deviation from the median (blue dashed).
#no need to generate hist again, can use abline
abline(v = mean(norm_dist), col = "red")
abline(v = median(norm_dist), col = "red", lty = 2)
abline(v = mean(norm_dist) + sd(norm_dist), col = "blue")
abline(v = mean(norm_dist) - sd(norm_dist), col = "blue")
#now the median absolute deviation
abline(v = median(norm_dist) + mad(norm_dist), col = "blue", lty = 2)
abline(v = median(norm_dist) - mad(norm_dist), col = "blue", lty = 2)

#7Generate a new vector with a lot more values (e.g., one million). Draw again a histogram. How does
#the distribution compare with more data points?
norm_dist_2 <- rnorm(n = 1000000, mean = 10, sd = 5)
hist(norm_dist_2, breaks = 50)

#We can also plot both graphs at the same time (whole plotting window has been divided into two grids)
par(mfrow = c(2, 1))
hist(norm_dist, breaks = 50)
hist(norm_dist_2, breaks = 50)
par(mfrow = c(1, 1)) #this resets the settings, so for the next graph it will be back to the default settings

