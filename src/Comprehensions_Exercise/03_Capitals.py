cities = input().split(', ')
capitals = input().split(', ')

zipped = list(zip(cities, capitals))
combined = {city: capital for city, capital in zipped}

for k, v in combined.items():
    print(f"{k} -> {v}")
