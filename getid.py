import requests

def id_collected(sumName, key):
    # COLLECTING DATA TO BE INSERTING FOR MATCHLIST DATABASE
    url = ('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+(sumName)+'?api_key='+(key))
    response = requests.get(url)
    print (response)
    if response.status_code == 200:
        accId = (response.json()['accountId'])
        return accId
    else: 
        accId = 'NO'
        return accId
