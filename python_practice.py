counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
temperture = int(input('What is the temperture outside?'))
if temperture > 80:
    print('Turn on the AC.')
else:
    print('Open a window.')  
counties = ['Arapahow', 'Denver', 'Jefferson'] 
if 'El Paso' in counties:
    print('El Paso is in the list of counties')
else:
    print('El Paso in not on the list of counties')
if 'Arapahoe' in counties and 'El Paso' in counties:
    print ('Arapahoe and El Paso are in the list of counties')
else:
    print ("Arapahoe and El Paso are not in the list of counties.")
x = 0
while x <= 5:
    print(x)
    x = x + 1
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print (county)
for county in counties_dict.keys():
    print (county)
for county, voters in counties_dict.items():
    print(county, 'county has', voters, 'registered voters')