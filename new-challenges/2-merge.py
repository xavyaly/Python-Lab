#!/usr/bin/python3

city1 = {"mum": 1, "kol": 2, "del": 3}
city2 = {"pat": 1, "ran": 5, "sri": 6}

cities = { **city1, **city2 }

print(cities)


# $ ./2-merge.py 
# {'mum': 1, 'kol': 2, 'del': 3, 'pat': 1, 'ran': 5, 'sri': 6}