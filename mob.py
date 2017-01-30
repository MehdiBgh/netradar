import csv
i=0

def my_min_function(somelist):
    min_value = None
    for value in somelist:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value

def my_max_function(somelist):
    max_value = None
    for value in somelist:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    return max_value


def search(file, key):
    dw_list = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (len(row[key]) >2 ):
                dw_list.append((row[key]))
                
    for car in dw_list:
        if ("/" in car):
            new=car.split("/")[2]
            dw_list.remove(car)
            dw_list.append(new)
    return dw_list

def stats(dw_list):            
    dw_list= map(float, dw_list)
    mean= sum(dw_list)/(len(dw_list))
    min=my_min_function(dw_list)
    max=my_max_function(dw_list)
    return mean, min, max
        

dw_list=search("cm.csv", "latency")
(mean, min, max)=stats(dw_list)
print "min = " + str(min) +  "  max = " + str(max) + "  mean = " + str(mean)+ "  number of measures " + str(len(dw_list))




#Cel vs wifi data

dic={}
with open("cm.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (len(row["downlink"]) >2 ):
                 dic[i]=row["downlink"]
            i=i+1

for k in dic.keys():
    if ("/" in dic[k]):
         new=dic[k].split("/")[2]
         dic[k]=new

dicw={}
j=0
with open("cm.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dicw[j]=row["radiotech"]
            j=j+1

dic_wifi=[]
dic_cel=[]
for i in dic.keys():
    if int(dicw[i])==0:
        dic_wifi.append(dic[i])
    else:
        dic_cel.append(dic[i])
    
    


(mean, min, max)=stats(dic_wifi)
#print "for wifi : min = " + str(min) +  "  max = " + str(max) + "  mean = " + str(mean)+ "  number of measures " + str(len(dic_wifi))
(mean, min, max)=stats(dic_cel)
#print "for cel data : min = " + str(min) +  "  max = " + str(max) + "  mean = " + str(mean) + "  number of measures " + str(len(dic_cel))
