###Query distributions and probabilities###
#1For the standard normal distribution: Plot the cumulative distribution function in the range [−5, 5].
q <- seq(-5, 5, by = 0.1)
q
vector_probabilities <- pnorm(q, mean = 0, sd = 1)
vector_probabilities
plot(x = q, y = vector_probabilities)

#2Plot the inverse cumulative distribution function for quantiles in 0.01 increment.
p <- seq(0, 1, by = 0.01)
p
vector_values <- qnorm(p, mean = 0, sd =1)
vector_values
plot(x = p, y = vector_values)

#3Plot the density function in the range [−5, 5]
vector_density <- dnorm(q, mean = 0, sd = 1)
vector_density
plot(x = q, y = vector_density)

#4What is the probability of observing a value greater than 2?
vector_probability_2 <- 1 - pnorm(2, mean = 0, sd = 1)
vector_probability_2

#5What is the probability of observing a value between -2 and 2?
pnorm(2, mean = 0, sd = 1) - pnorm(-2, mean = 0, sd = 1)

#6What is the probability of observing a value more extreme than -2 or 2?
1 - (pnorm(2, mean = 0, sd = 1) - pnorm(-2, mean = 0, sd = 1))
