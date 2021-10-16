#To create a string
d = """Lamb
Beef
Pork
Tuna
Trout (farmed)
Trout (wild)
Chicken
Tofu
Plant based (vegan) burger
Cheese (unpasturised)
Cheese: unripened e.g, cottage cheese mozzarella
Beans
Eggs
Egg: Free Range
Avocados
Potatoes
Rice
Dried and candied fruits, nuts and seeds
Lentils
Mushrooms
Oats
Coffee
Water
Milk (fresh cattle)
"""

#To split based on the new lines and assign the items as values in the key list
keys = []
for i in d.split('\n'):
    print(i)
    keys.append(i)

#To create the second list
d = """2.4kg CO2e(24kg CO2e/kg)
2.35kg CO2e(23.45kg CO2e/kg)
0.93kg CO2e(9.3kg CO2e/kg)
0.41kg CO2e(4.08kg CO2e/kg)
0.47kg CO2e(4.72kg CO2e/kg)
0.42kg CO2e(4.15kg CO2e/kg)
0.66kg CO2e(6.57kg CO2e/kg)
0.11kg CO2e(1.07kg CO2e/kg)
0.23kg CO2e(2.29kg CO2e/kg)
1.23kg CO2e(12.27kg CO2e/kg)
1.23kg CO2e(12.27kg CO2e/kg)
0.14kg CO2e(1.35kg CO2e/kg)
0.48kg CO2e(4.77kg CO2e/kg)
0.53kg CO2e(5.3kg CO2e/kg)
0.05kg CO2e(0.54kg CO2e/kg)
0.1kg CO2e(1.02kg CO2e/kg)
0.31kg CO2e(3.08kg CO2e/kg)
0.28kg CO2e(2.81kg CO2e/kg)
0.14kg CO2e(1.35kg CO2e/kg)
0.4kg CO2e(3.97kg CO2e/kg)
0.07kg CO2e(0.73kg CO2e/kg)
1.77kg CO2e(17.72kg CO2e/kg)
0.02kg CO2e(0.2kg CO2e/kg)
0.11kg CO2e(1.13kg CO2e/kg)
"""
#Split based on the new lines and assign them as values in the vals list 
vals = []
for i in d.split('\n'):
    print(i)
    #to ignore from kg
    vals.append(i.split('kg')[0])

#Dictionary comprehension
d = {k:v for k,v in zip(keys,vals)}
print(d)