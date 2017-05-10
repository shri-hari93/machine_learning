dataset = read.csv('Data.csv') #you dont have to distinguish between dependent and independent variables

#Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age) #na.rm = true to calculate mean for the non missing data
dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)
                                                                                              
