import json

def checkAuthorCommitsDays(dados_api, authorMap, fileLogRaw):
		date = dados_api[i]['commit']['author']['date']
		#author = dados_api[i]['commit']['author']['email']
    for i in range(len(dados_api)):
        
        #author = i['commit']['author']['email']
        #print(author)
        #está reconhecendo dados_api[i] como string
        commit =  dados_api[i].get('commit')
        author = commit.get('author')
        date = author.get('date')
            
            
        day = date.split("T")[0]
        time = date.split("T")[1]
        hour = time.split(":")[0]
            
        #print(day +"\n"+hour+"\n\n")

        d = day + "," + hour + "\n"
        fileLogRaw.write(d)

        '''if not author in authorMap: #lista com os autores e lista com os dias
            authorMap[author] = [day]
        else:
            if not day in authorMap[author]:
                authorMap[author].append(day)
            else:
                authorMap[author][day].append(hour)'''
        if not day in authorMap:
            authorMap[day] = [hour]
        else:
            authorMap[day].append(hour)
        

def computeAuthorRanks(fileActivity, authorMap):
    
    numCommits = []
    for key, value in authorMap.items():
        print(key, len(value))
        numCommits.append(len(value))

    i = 1
    for value in sorted(numCommits,reverse=True):
        fileActivity.write(str(i)+","+str(value)+"\n")
        i += 1


fileJSON = open('data.json', 'r', encoding='utf-8') 
dados_api = json.load(fileJSON)
fileLogRaw = open("logBasicRawData.data", "w")
authorMap = {}
checkAuthorCommitsDays(dados_api, authorMap,fileLogRaw)
fileLogRaw.close()

fileActivity = open("activity.data", "w")
fileActivity.write("Rank,Frequency\n")
computeAuthorRanks(fileActivity, authorMap)
fileActivity.close()