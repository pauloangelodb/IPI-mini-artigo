# a API lê exatamente 6000 commits

#conta a quantidade de commits por hora e imprime no arquivo:

def countHours(fileActivity, hourMap):
    
    horas =sorted(hourMap, reverse=True)

    for i in hourMap:

        
        fileActivity.write(str(hourMap.index(i))+","+str(i)+"\n")
        
                
def checkHours(dados_api, hourMap, fileLogRaw, fileActivity):
    
    hourMap = [0]*24

    for i in dados_api:
        
        #author = i['commit']['author']['email']
        #print(author)
        if type(i)==dict:
            commit =  i['commit']
            author = commit.get('author')
            date = author.get('date')


            day = date.split("T")[0]
            time = date.split("T")[1]
            hour = time.split(":")[0]

            #print(day +"\n"+hour+"\n\n")

            #d = day + "," + hour + "\n"
            

            hourMap[int(hour)] += 1
            
            fileLogRaw.write(hour +","+ str(hourMap[int(hour)])+"\n")
    soma =0
    for i in hourMap:
        soma += i
    print (soma)            
            
    countHours(fileActivity, hourMap)
            
        
fileJSON = open('data.json', 'r', encoding='utf-8') 
dados_api = json.load(fileJSON)
fileLogRaw = open("logBasicRawCH.data", "w")
hourMap = []
arqTeste2 = open("teste2.data", "w")
arqTeste2.write("Hora, quantidade\n")

checkHours(dados_api, hourMap,fileLogRaw, arqTeste2)
fileLogRaw.close()
arqTeste2.close()



