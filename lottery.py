import sys
import json
import urllib2
import random


def fetch_data():
    with open('tickets.json', 'r') as f:
        tickets = json.loads(f.read())
        return [(d['username'], d['lottery_tickets']) for d in tickets]


def random_sample(users):
    total = 0
    for item, weight in users:
        total += weight
        if weight > random.random() * total:
            chosen = (item, weight)
    return chosen


def draw(users):
    user = random_sample(users)
    users.remove(user)
    return user


if __name__ == '__main__':
    random.seed(sys.argv[1])

    users = fetch_data()

    jackpot_winner = draw(users)[0]

    winners = list()

    for _ in range(100):
        winners.append(draw(users)[0])

    print(json.dumps(dict(winners=winners, jackpot_winner=jackpot_winner), sort_keys=True))
