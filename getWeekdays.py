import datetime
import json

def checkWeekDays(dados_api, weekMap, fileLogRaw, fileActivity):
    
    data =[]
    contaWD = 7*[0]

    for i in dados_api:
        
        if type(i)==dict:
            
            date2 =  i['commit']['author']['date']
            #formato: "2021-04-14T17:55:56Z"
            
            date1 = date2.split("T")[0]
            year = date1.split("-")[0]
            if year =="2021":
                month = date1.split("-")[1]
                day = date1.split("-")[2]
                data.append([year,month,day])
    
    for commit in sorted(data,reverse=True):
        
        wd = datetime.date(int(commit[0]),int(commit[1]),int(commit[2])).weekday()
        #print(commit[0],commit[1],commit[2], wd)
        fileLogRaw.write(commit[0]+"-"+commit[1]+"-"+commit[2]+ " "+str(wd)+"\n")
        contaWD[wd] += 1
    
    for i in range(len(contaWD)):
        fileActivity.write(str(i)+","+str(contaWD[i])+"\n")
                

fileJSON = open('data.json', 'r', encoding='utf-8') 
dados_api = json.load(fileJSON)
fileLogRaw = open("logBasicRawDataWD.data", "w")
weekMap = []
fileActivity = open("activityWD.data", "w")
fileActivity.write("Dia,Frequencia\n")
checkWeekDays(dados_api, weekMap,fileLogRaw, fileActivity)
fileLogRaw.close()
fileActivity.close()
