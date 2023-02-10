# import pandas and numpy

import pandas as pd

import numpy as np

# create a numpy array

# which will store the cumulative miles

cum_miles = np.array([55, 120, 150, 210, 287, 300])

# convert it into pand

cum_series = pd.Series(cum_miles)

# another array to store the miles covered each day


each_Day = np.array([cum_series[0]])

# iterate the series

for i in range(1, len(cum_series)):

# the miles for current day wil be cumulative mile till that day - previous day mile

each_Day = np.append(each_Day, cum_series[i]-cum_series[i-1

                                                        
#new array into series and display it

print("Miles each day:")

print(pd.Series(each_Day))
