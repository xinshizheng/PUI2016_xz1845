# HW4 Assignment 1
by nm2773

## Verify null and alternative hypothesis
xz1845 formulated the null hypothesis as "The mean bike trip duration by older people (Age>45) is equal or longer than the mean bike trip duration by younger people (Age <= 45)", but in the alternative hypothesis, she/he formulated it as:

H1: mean_older <= mean_younger

which is false because she/he **includes** equal sign in it, thus it is not complementing null hypothesis. The alternative hypothesis has to be

H1: mean_older < mean_younger

## Does the data support the project?
Each ride has the associated birth year and trip duration of the rider, thus the data support the project. 
It is better to show the distribution of each group, to determine which test is sufficient. Also, it is also better to explain why 45 was chosen as the threshold and all the assumption behind the hypothesis.

## Choose a statistical test.
Because she/he is going to compare 2 independent groups along with 1 dependent variable (mean of bike trip durations), I suggest **t-test**. Now, it depends on the variance of the groups. If the parent of each group has the same variance, she/he can use **independent t-test**, otherwise if the variances are different, she/he might use **welch t-test**.
