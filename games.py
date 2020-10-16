import requests

class Game:

    def find_game_ids(self, accId, key, num_games):
        i = 0
        GAMEID = []
        num_games = 20
        url_match_list = ('https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/' + (accId) + '?queue=420&endIndex=20&api_key=' + (key))
        response2 = requests.get(url_match_list)
        # Adding 20 games into the list
        while num_games > 0:
            GAMEID.append('https://na1.api.riotgames.com/lol/match/v4/matches/'+str(response2.json()['matches'][i]['gameId']) + '?api_key=' + (key))
            i += 1
            num_games = num_games - 1

        return GAMEID

    def game_data(self, game_list, key, sumName, num_games):

        wins = []
        deaths = []
        deaths = []
        kills = []
        assists = []
        visions = []
        csTotal = []
        # Finding the data of said summoner in each game id
        for urls in game_list:
            response = requests.get(urls)
            resp_json = response.json()
            Loop = 0
            index = 0
            while Loop <= 10:

                if resp_json['participantIdentities'][index]['player']['summonerName'] != sumName:
                    Loop = Loop+1
                    index = index+1
                elif resp_json['participantIdentities'][index]['player']['summonerName'] == sumName:

                    deaths.append(resp_json['participants'][index]['stats']['deaths'])
                    kills.append(resp_json['participants'][index]['stats']['kills'])
                    assists.append(resp_json['participants'][index]['stats']['assists'])
                    visions.append(resp_json['participants'][index]['stats']['visionScore'])
                    csTotal.append(resp_json['participants'][index]['stats']['totalMinionsKilled'])
                    wins.append(resp_json['participants'][index]['stats']['win'])

                    break
        # Finding avg of each stat
        deaths = sum(deaths)/num_games
        kills = sum(kills)/num_games
        assists = sum(assists)/num_games
        visions = sum(visions)/num_games
        csTotal = sum(csTotal)/num_games
        wins = sum(wins)/num_games
        stat_list = []
        stat_list.append(deaths) #0
        stat_list.append(kills) #1
        stat_list.append(assists) #2
        stat_list.append(visions) #3
        stat_list.append(csTotal) #4
        stat_list.append(wins) #5

        return stat_list
