# Simulate a sports tournament

import csv
import sys
import random

# Number of simulations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    filename = sys.argv[1]
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for team in reader:
            team['rating'] = int(team['rating'])
            teams.append(team)

    counts = {}

    # TODO: Simulate N tournaments and keep track of win counts for each team
    # DE aca hasta el line40 lo hice yo

    # set counter at 0 for each Country in Counts Dictionary
    for team in teams: # CADA DICCIONARIO EN LA LISTA TEAMS
        counts[(team['team'])] = 0

    # Simulate N times the tournament
    for i in range(N):
        # extract the name from the list and the from de the Dictionary
        champion = (simulate_tournament(teams)[0]['team'])
        (counts[champion]) += 1
    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"] # arg 1254
    rating2 = team2["rating"] # bra 1384
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = [] 
    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]): #true arg
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])
    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    # De aca hasta el line 72 lo hice yo
    winners = simulate_round(teams)
    while len(winners)!= 1:
        winners = simulate_round(winners)
    return winners


if __name__ == "__main__":
    main()
