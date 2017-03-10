#data frames - collecting vectors of the same length, elements inside can be of different data types

author <- c("Austin","Limmy","Larsson","Bronte")  #c() assign
dates <- c("1903-05-10", "2015-10-07", "2005-03-26","1898-07-18")
year <- as.Date(dates)
gender <- c("F","M","M","F")
id <- c(290,87,230,120)
authorlist_df <- data.frame(author,year,gender,id)
authorlist_df
str(authorlist_df)
authorlist_df$year
names(authorlist_df) #names of the dimensions
rownames4 <- c("ID1", "ID2", "ID3", "ID4")
rownames(authorlist_df) <-
authorlist_df
dim(authorlist_df)[1] #nrow()
dim(authorlist_df)[2] #ncol()
#dimensions are defined as rows by columns
# Print out the values located in the third column
authorlist_df[,3]
# Print out the values located on the first and second row, 1st column
authorlist_df[1:2,1]

authorlist_df$id[3] <-90
authorlist_df

mean(authorlist_df$id)

authorlist_df <- data.frame("name" = c("Jane",NA,"Stieg","Charlotte"), authorlist_df) #add new column
authorlist_df <- data.frame(authorlist_df,"age" = c(78,43,56,87))
numbers <- subset(authorlist_df,select=c("age","id")) #2 ways of subsetting
authorlist_df[,c("age","id")]
meancol<-apply(numbers,2,mean)
as.array(meancol)

authorlist_df[,c("age","id")]
subset(authorlist_df,authorlist_df$age<60 & authorlist_df$id>=88)
subset(authorlist_df,author=='Limmy')
authorlist_df[grep("4", authorlist_df$age),]
authorlist_df[grep("lotte", authorlist_df$name),]
factor(gender)
levels(authorlist_df$gender)
class(authorlist_df$year)
class(authorlist_df$gender)
newrow <- data.frame("Emma","Cline","2016-05-10","F",54,32)
names(newrow) <-NULL
names(newrow) <- names(authorlist_df) #new row has to inherit the same header names
identical(names(newrow),names(authorlist_df)) #now TRUE
authorlist_df <-rbind(authorlist_df,newrow)
rownames(authorlist_df)<- c(rownames4,"ID5")
authorlist_df$age <- as.numeric(authorlist_df$age)
authorlist_df[order(authorlist_df$age,decreasing=TRUE),] #by default - ASC, comma the most important thing the last comma it say that the called function should be applied on every row.


#When you have multiple values, spread out over multiple columns, for the same instance, your data is in the “wide” format.
#On the other hand, when your data is in the “long” format if there is one observation row per variable. You therefore have multiple rows per instance.
> observations_long #one row for each value that you have in the Type variable. A lot of statistical tests favor this format.
  Subject Gender   Test Result
1       1      M   Read     10
2       2      F  Write      4
3       1      M  Write      8
4       2      F Listen      6
5       2      F   Read      7
6       1      M Listen      7
> observations_wide # each column represents a unique pairing of the various factors with the values - exhausting info about one variable
  Subject Gender Read Write Listen
1       1      M   10     8      7
2       2      F    7     4      6

#The former is preferred when you work with simple data frames, while the latter is more often used on more complex ones, mostly because there’s a difference in
#the possibilities that both functions offer.

#The stack() function basically concatenates or combines multiple vectors into a single vector, along with a factor that indicates where each observation originates from.
#To go from wide to long format, you will have to stack your observations, since you want one observation row per variable, with multiple rows per instance
long_format <- stack(observations_wide,
                     select=c(Read,
                              Write,
                              Listen))
There are two main options that you can choose here: you can use the stack() function or you can try using the reshape() function.


#To go from long to wide format, you will need to unstack your data, which makes sense because you want to have one row per instance with each value present
#as a different variable.
#Note here that you want to disentangle the Result and Test columns
wide_format <- unstack(observations_long,
                       Result ~ Test)

# Import `reshape2`
library(reshape2)

# Convert to a wide format with `dcast()`
long_reshaped2wide <- dcast(observations_long,
                        Subject + Gender ~ Test,
                        value.var="Result")

# Reshape to wide format
reshape2wide <- reshape(observations_long,
                        timevar = "Test",
                        idvar = c("Subject", "Gender"),
                        direction = "wide")
