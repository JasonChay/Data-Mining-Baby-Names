import re
import pickle

dict_all_years = {}

for i in range(1880, 2017):
    f = open("babynames"+str(i)+".html", "r")
    f_contents = f.read()
    names = re.findall(r'<td>(\w+)</td>\s<td>(\w+)?</td>\s<td>(\w+)?</td>', f_contents)
    dict_this_year = {}
    for j in names:
        if j[1] not in dict_this_year:
            dict_this_year[(j[1])] = j[0]
        if j[2] not in dict_this_year:
            dict_this_year[(j[2])] = j[0]
    dict_all_years[i] = dict_this_year
    f.close()

# with open("dict-all-years.pickle", "wb") as f:
#     pickle.dump(dict_all_years, f, protocol=pickle.HIGHEST_PROTOCOL)
