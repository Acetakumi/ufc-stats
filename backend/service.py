import requests
import json

DOMAIN = "https://api.octagon-api.com"

def fetch(url):
    return json.loads(requests.get(url).content)

def fetchRanking():
    return fetch(DOMAIN + "/rankings")

def fetchAllFighters():
    return fetch(DOMAIN + "/fighters")

def fetchFighters(id):
    return fetch(DOMAIN + "/fighter/" + id)

def test():
    rankings = fetchRanking()
    allFighters = fetchAllFighters()
    
    finalList = []
    
    for division in rankings:
        rank = 0
        fightersList = []
        
        if division["id"] != "mens-pound-for-pound-top-rank":
            fightersList.append({
                "name": division["champion"]["championName"],
                "rank": rank,
                "stats": allFighters[division["champion"]["id"]]
            })
        
        for fightersInRanking in division["fighters"]:
            rank += 1
            tempFighter = allFighters[fightersInRanking["id"]]
            
            fightersList.append({
                "name": tempFighter["name"],
                "rank": rank,
                "stats": tempFighter
            })
        
        finalList.append({
            "division": division["categoryName"],
            "fighters": fightersList
        })
    
    return finalList