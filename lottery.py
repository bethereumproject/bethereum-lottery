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

    top_500 = list()
    top_2000 = list()

    for _ in range(500):
        top_500.append(draw(users))

    for _ in range(2000):
        top_2000.append(draw(users))

    remainder = users

    print(json.dumps(dict(top_500=top_500, top_2000=top_2000, remainder=remainder), sort_keys=True))
