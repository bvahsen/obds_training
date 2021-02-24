###R projects and environments###

#initialise a new project environment
renv::init()

#install packages in the project environment
renv::install('ggplot2')

#Call renv::snapshot() to save the state of the project library to the lockfile(renv.lock)
renv::snapshot()
#this doesn't change it because we haven't made any changes yet

###create a script that loads one of the packages that you just installed
library('ggplot2')

#Call renv::snapshot() again to save the state of the project library to the lockfile(renv.lock)
#cave: important to save the file first
renv::snapshot()
#now it changes it in the renv.lock file