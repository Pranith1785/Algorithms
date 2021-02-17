### Problem Statement
'''
Find the tournament winner, given the competitions b/w teams and results of each round.
Each round is held b/w Home team and Away team
Ex : Competitions  = [[a,b],[b,c],[c,d]]
     results = [0, 1,0]
Note : 1. Only one winner in each round
       2. results[i] is for compettitons[i], where 0 represents Away team(b) is won and
                                                   1 represents Home team(a) is won 
'''

## Solution 1
## Time - O(n) - number of matches/competitions
## Space - O(m) - number of teams
def tournamentWinner(competitions, results):

    team_result_count = {}
    for match in range(0,len(results)):
        
        winner = competitions[match][1] if results[match] == 0 else competitions[match][0]

        if winner not in team_result_count:
            team_result_count[winner]  = 0

        team_result_count[winner] += 1

    return max(team_result_count, key=team_result_count.get)

## Solution 2
## Time - O(n)
## Space - O(k)
def tournamentWinner2(competitions,results):

    BestTeam = ""
    team_result_count = {BestTeam:0}
    for idx, match in enumerate(competitions):
        home_team , away_team = match

        winner = home_team if results[idx] == 1 else away_team

        if winner not in team_result_count:
            team_result_count[winner]  = 0

        team_result_count[winner] += 1

        if team_result_count[winner] > team_result_count[BestTeam]:
            BestTeam = winner
    
    return BestTeam



if __name__ == "__main__":
    competitionsArray = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    resultsArray = [0, 0, 1]
    print(tournamentWinner2(competitionsArray, resultsArray))
