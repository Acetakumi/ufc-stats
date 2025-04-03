import requests
import json

DOMAIN = "https://api.octagon-api.com"

def fetch(url):
    return json.loads(requests.get(url).content)


def fetchRanking():
    return fetch(DOMAIN + "/rankings")

def fetchFighters(id):
    return fetch(DOMAIN + "/fighter/" + id)

def getDivName(index):
    divisonName = fetchRanking()[index]["categoryName"]
    print(divisonName)
    
def getChampionName(index):
    champion = {
        "championName" : fetchRanking()[index]["champion"]["championName"],
        } 
    print(champion)
    
    
def getallfighters(index) :
    
    rank = 0
    fightersName = []
    if (index != 0) :
        fightersName = [{
            
            "rank" : rank,
            "name" : fetchRanking()[index]["champion"]["championName"],
            "stats" : fetchFighters(fetchRanking()[index]["champion"]["id"])
        }]
        rank += 1
    
    
    
    
    for i in range (0,15,1) :
        fightersName.append({
            
            "rank" : rank,
            "name" : fetchRanking()[index]["fighters"][i]["name"],
            "stats" : fetchFighters(fetchRanking()[index]["fighters"][i]["id"])
        })
        rank +=1
        
    
    fightersfinal = {
        
        "division": fetchRanking()[index]["categoryName"],
        "fighters" : fightersName
    }

    
    return fightersfinal

def buildFighter () : 
    final = []
    rankings = fetchRanking()
    
    for i in range(0,len(rankings),1) :
        final.append(getallfighters(i))
        print(final)
    
    return final
    
    



 
        
        
           



    
    


