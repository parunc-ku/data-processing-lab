import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

for items in cities:
    if items["country"] == "Germany":
        print(items["city"])

# Print all cities in Spain with a temperature above 12°C

for items in cities:
    if items["country"] == "Spain":
        if float(items["temperature"]) >= 12:
            print(items["city"])

# Count the number of unique countries

print(len({city['country'] for city in cities}))

# Print the average temperature for all the cities in Germany

german_temps = [float(c['temperature']) for c in cities if c['country'] == 'Germany']
print(sum(german_temps) / len(german_temps))

# Print the max temperature for all the cities in Italy

italy_temps = [float(c['temperature']) for c in cities if c['country'] == 'Italy']
print(max(italy_temps))