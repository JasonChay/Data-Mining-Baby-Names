import requests
for i in range(1880, 2017):
    r = requests.post("https://www.ssa.gov/cgi-bin/popularnames.cgi",{"year": str(i) ,"top": "1000"})
    f = open("babynames"+ str(i) +".html", "wb")
    f.write(r.content)
    f.close()
    print(i)
