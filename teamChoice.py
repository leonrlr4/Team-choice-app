from random import choice

numPlayer = int(input('How many player fo you have? '))
players = []
for i in range(0, numPlayer):
    playerName = input("enter player {} :".format(i + 1))
    players.append(playerName)

teamA = []
teamB = []

numPlayers = len(players) // 2
print("There are {} people in one team. ".format(numPlayers))

def addPlayer(team):
    for i in range(0, numPlayers):
        playerA = choice(players)
        players.remove(playerA)
        team.append(playerA)
        i += 1

addPlayer(teamA)
addPlayer(teamB)


print("===============")

print("Team A has member: ")

for i in teamA:
    print(i)

print("===============")

print("Team B has member: ")
for j in teamB:
    print(j)

print("===============")
