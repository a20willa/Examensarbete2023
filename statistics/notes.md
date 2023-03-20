# Statistics
## Q&A
**Q:** Should each complete request be counted as a item or should each query count as a item? 

**A:** We fetch all items rather than induvidual ones. There is no gain for meassuring induvidual queries, as the only difference are the coordinates. In that case, if we wanted to know which coordinates would have an effect, we could, but for this thesis it does not matter. We only want to know how the database as a whole peforms, which we do trough this. Besides, ultimately, altough the sum of the comined query time may differ, it does not differ enough to gain any usefull info. 1000 queries takes about 5ms on mongodb, and an induvidual one would be so small that seeing changes would be hard anyways.

## Defenitions
### Standard Error
The standard error is a measure of the variability or spread of a statistic, such as the mean or proportion, calculated from a sample of data. It tells you how much the sample statistic is likely to vary from the true population parameter.

In simpler terms, it's like a measure of how much the sample data can be trusted to represent the entire population. The smaller the standard error, the more precise the estimate of the population parameter is likely to be.

For example, imagine you want to know the average height of all the students in your school. You take a sample of 50 students and calculate the average height from that sample. The standard error tells you how much the sample average is likely to differ from the true population average. A smaller standard error indicates that your sample is more likely to be a good representation of the entire population of students in terms of their height.

### Standard Deviation
Standard deviation is a statistical measure that is used to determine how much the values in a dataset vary from the average, or mean. In other words, it tells you how spread out the data is around the average. The larger the standard deviation, the more spread out the data is; the smaller the standard deviation, the less spread out the data is.

## Charts
We need the following charts:
* LineDiagram - To plot the time for each query
* Standard Error - To see how "accurate" the sample compared to the population
* Standard Deviation  - How much a dataset varies from the mean