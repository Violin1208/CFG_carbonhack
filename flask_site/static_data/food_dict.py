info = {'Lamb': '2.4', 'Lentils': '0.14', 'Beef': '2.35', 'Plant based (vegan) burger': '0.23', 'Trout (farmed)': '0.47', 'Milk (fresh cattle)': '0.11', 'Avocados': '0.05', 'Rice': '0.31', 'Coffee': '1.77', 'Dried and candied fruits, nuts and seeds': '0.28', 'Eggs': '0.48', 'Water': '0.02',
 'Tuna': '0.41', 'Oats': '0.07', 'Cheese (unpasteurised)': '1.23', 'Potatoes': '0.1', 'Cheese: unripened e.g, cottage cheese mozzarella': '1.23', 'Beans': '0.14', 'Egg: Free Range': '0.53', 'Pork': '0.93', 'Trout (wild)': '0.42', 'Tofu': '0.11', 'Mushrooms': '0.4', 'Chicken': '0.66'}

all_items = {'Lamb': '2.4', 'Lentils': '0.14', 'Beef': '2.35', 'Plant based (vegan) burger': '0.23',
             'Trout (farmed)': '0.47', 'Milk (fresh cattle)': '0.11', 'Avocados': '0.05', 'Rice': '0.31',
             'Coffee': '1.77',
             'Dried and candied fruits, nuts and seeds': '0.28', 'Eggs': '0.48', 'Water': '0.02', 'Tuna': '0.41',
             'Oats': '0.07', 'Cheese (unpasteurised)': '1.23', 'Potatoes': '0.1',
             'Cheese: unripened e.g, cottage cheese mozzarella': '1.23', 'Beans': '0.14', 'Egg: Free Range': '0.53',
             'Pork': '0.93', 'Trout (wild)': '0.42', 'Tofu': '0.11', 'Mushrooms': '0.4', 'Chicken': '0.66'}

foods = {'Lamb': '2.4', 'Beef': '2.35', 'Plant based (vegan) burger': '0.23', 'Trout (farmed)': '0.47', 'Eggs': '0.48',
         'Tuna': '0.41', 'Cheese (unpasteurised)': '1.23', 'Cheese: unripened e.g, cottage cheese mozzarella': '1.23',
         'Egg: Free Range': '0.53', 'Pork': '0.93', 'Trout (wild)': '0.42', 'Tofu': '0.11', 'Chicken': '0.66',
         'Avocados': '0.05', 'Dried and candied fruits, nuts and seeds': '0.28', 'Mushrooms': '0.4', 'Potatoes': '0.1',
         'Lentils': '0.14', 'Rice': '0.31', 'Beans': '0.14', 'Oats': '0.07'}

drinks = {'Milk (fresh cattle)': '0.11', 'Coffee': '1.77', 'Water': '0.02'}

def sort_alphab(info):
    sortednames = sorted(info.keys(), key=lambda x: x.lower())
    info_sorted = {}
    for i in sortednames:
        value = info[i]
        info_sorted[i] = value
    return info_sorted
# main code
foods = sort_alphab(foods)
drinks = sort_alphab(drinks)