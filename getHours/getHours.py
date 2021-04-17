#gethours

# a API lê exatamente 6000 commits, porém utilizaremos apenas 5678, referentes ao ano de 2021

#conta a quantidade de commits por hora e imprime no arquivo:

def countHours(fileActivity, hourMap):
    
    horas =sorted(hourMap, reverse=True)

    for i in range(len(hourMap)):

        fileActivity.write(str(i)+","+str(hourMap[i])+"\n")
        
        
                
def checkHours(dados_api, hourMap, fileLogRaw, fileActivity):
    
    hourMap = [0]*24

    for i in dados_api:
        
        if type(i)==dict:
            
            date = i['commit']['author']['date']
            day = date.split("T")[0]
            year = day.split("-")[0]
            #print(year)
            if year =="2021":
                
                #Formato: "2021-04-14T17:55:56Z"
               
                time = date.split("T")[1]
                hour = time.split(":")[0]
                
                hourMap[int(hour)] += 1

                fileLogRaw.write(hour +","+ str(hourMap[int(hour)])+"\n")
    
    countHours(fileActivity, hourMap)
            
        
fileJSON = open('data.json', 'r', encoding='utf-8') 
dados_api = json.load(fileJSON)
fileLogRaw = open("logBasicRawCH.data", "w")
hourMap = []
arqHours = open("commitHours.data", "w")
arqHours.write("Hora, Frequencia\n")
checkHours(dados_api, hourMap,fileLogRaw, arqHours)
fileLogRaw.close()
arqHours.close()
