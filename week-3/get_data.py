import urllib.request as request
import json
import csv
# data website
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# load .json data
with request.urlopen(src) as response:
    data = json.load(response)
attraction_list = data["result"]["results"]
# filter by xpostDate
filtered_list=list(filter(lambda attraction: int(attraction["xpostDate"][:4])>=2015, attraction_list)) 
# print(filtered_list[0])
# write csv
with open("data.csv", "w", encoding = "UTF8") as file:
    writer=csv.writer(file)
    for attraction in filtered_list:
        # write 景點名稱，區域，經度，緯度，第一張圖檔網址
        writer.writerow([attraction["stitle"], 
                         attraction["address"][5:8], 
                         attraction["longitude"], 
                         attraction["latitude"], 
                         f'https{attraction["file"].split("https")[1]}'])