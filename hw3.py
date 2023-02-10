Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> # import pandas and numpy

import pandas as pd

import numpy as np

# create a numpy array

# which will store the cumulative miles

cum_miles = np.array([55, 120, 150, 210, 287, 300])

# convert it into panda series

cum_series = pd.Series(cum_miles)

# now create another array to store the miles covered each day

# the first day mile will be same as the cumulative miles

each_Day = np.array([cum_series[0]])

# iterate the series

for i in range(1, len(cum_series)):

# the miles for current day wil be cumulative mile till that day - previous day mile

each_Day = np.append(each_Day, cum_series[i]-cum_series[i-1])

# finally convert the new array into series and display it

print("Miles each day:")

print(pd.Series(each_Day))
[DEBUG ON]
>>> 