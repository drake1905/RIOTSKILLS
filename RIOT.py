import requests



#ASKING USER FOR SUMMONER NAME


sumName = input('Enter summoner name:')


#COLLECTING DATA TO BE INSERTING FOR MATCHLIST DATABASE


url=('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+(sumName)+'?api_key='+(key))


response=requests.get(url)

accId=(response.json()['accountId'])


#COLLECTING DATA FOR THE NEXT DATABASE API


url2=('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+(accId)+'?queue=420&endIndex=20&api_key='+(key))
response2=requests.get(url2)


i=0
GAMEID = []
Idgame=20

#COLLECTS GAME ID'S FOR NEXT DATABASE FOR 20 GAMES


while Idgame>0:
    GAMEID.append(response2.json()['matches'][i]['gameId'])
    i=i+1
    Idgame=Idgame-1















#COLLECTING DATA FROM GAME 1


class GAME1():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[0])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0


    #THIS COLLECT THE ID NUMBER OF THE PLAYER NAME THAT WAS INSERTED


    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
            
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']






#COLLECTING DATA FROM GAME 2    


class GAME2():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[1])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 3


class GAME3():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[2])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']






#COLLECTING DATA FROM GAME 4


class GAME4():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[3])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 5


class GAME5():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[4])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 6


class GAME6():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[5])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 7


class GAME7():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[6])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 8


class GAME8():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[7])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 9


class GAME9():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[8])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 10


class GAME10():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[9])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']








#COLLECTING DATA FROM GAME 11


class GAME11():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[10])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 12


class GAME12():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[11])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 13


class GAME13():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[12])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 14


class GAME14():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[13])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 15


class GAME15():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[14])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 16


class GAME16():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[15])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 17


class GAME17():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[16])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 18


class GAME18():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[17])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 19


class GAME19():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[18])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']







#COLLECTING DATA FROM GAME 20


class GAME20():
    url3=('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(GAMEID[19])+'?api_key='+(key))
    response3=requests.get(url3)
    Loop=0
    index=0
    while Loop<=10:

        if response3.json()['participantIdentities'][index]['player']['summonerName']!=sumName:
            Loop= Loop+1
            index=index+1
        elif response3.json()['participantIdentities'][index]['player']['summonerName']==sumName:
            break
    kills=response3.json()['participants'][index]['stats']['kills']
    deaths=response3.json()['participants'][index]['stats']['deaths']
    timer=response3.json()['gameDuration']
    assists=response3.json()['participants'][index]['stats']['assists']
    visions=response3.json()['participants'][index]['stats']['visionScore']
    csTotal=response3.json()['participants'][index]['stats']['totalMinionsKilled']
            



#Object from each game class


game1= GAME1()
game2= GAME2()
game3= GAME3()
game4= GAME4()
game5= GAME5()
game6= GAME6()
game7= GAME7()
game8= GAME8()
game9= GAME9()
game10= GAME10()


#Calcuating the average of 10 games for each stat


killsAvg= (game1.kills+game2.kills+game3.kills+game4.kills+game5.kills+game6.kills+game7.kills+game8.kills+game9.kills+game10.kills)/10
assistsAvg=(game1.assists+game2.assists+game3.assists+game4.assists+game5.assists+game6.assists+game7.assists+game8.assists+game9.assists+game10.assists)/10
deathsAvg=(game1.deaths+game2.deaths+game3.deaths+game4.deaths+game5.deaths+game6.deaths+game7.deaths+game8.deaths+game9.deaths+game10.deaths)/10
visionsAvg=(game1.visions+game2.visions+game3.visions+game4.visions+game5.visions+game6.visions+game7.visions+game8.visions+game9.visions+game10.visions)/10
csAvg=(game1.csTotal+game2.csTotal+game3.csTotal+game4.csTotal+game5.csTotal+game6.csTotal+game7.csTotal+game8.csTotal+game9.csTotal+game10.csTotal)/10

print('His average kills is '+str(killsAvg)+' in the last 10 games')
print('His average assists is '+str(assistsAvg)+' in the last 10 games')
print('His average deaths is '+str(deathsAvg)+' in the last 10 games')
print('His average visions is '+str(visionsAvg)+' in the last 10 games')
print('His average csing is '+str(csAvg)+' in the last 10 games')












    
    

    













