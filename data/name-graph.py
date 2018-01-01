import pickle
import sys

with open("dict-all-years.pickle", "rb") as f:
    dict_all_years = pickle.load(f)

test_name = sys.argv[1]
x = []
y = []
for year in dict_all_years:
    x.append(year)
    if test_name in dict_all_years[year]:
        y.append(dict_all_years[year][test_name])
    else:
        y.append(1000)

import matplotlib.pyplot as plt

plt.title("Popularity of Name '{}'".format(test_name))
plt.axis([1880, 2016, 1, 1000])
plt.xlabel("Year")
plt.ylabel("Rank")
plt.plot(x,y)
plt.gca().invert_yaxis()
plt.show()
