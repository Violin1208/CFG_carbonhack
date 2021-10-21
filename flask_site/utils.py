from flask_site.static_data.food_dict import info, foods
from flask import flash

# dictionary contains: key=name of food; value= dictionary of foods+co2
def food_comp(info):
    dic = {name: {key: info.get(key) for key in info.keys()} for name in info.keys()}
    for key in dic.keys():
        newdic = {k: val for k, val in dic.get(key).items() if val < dic[key].get(key)}
        newdic_sorted = dict(sorted(newdic.items(), key=lambda item: item[1]))
        dic[key] = newdic_sorted
    return dic


dictionary = food_comp(foods)


def print_result(choice):
    start_co2 = foods.get(choice)
    print(choice, start_co2, '\n', dictionary[choice])
    print(get_miles(foods.get(choice)), 'miles')
    return start_co2


def get_miles(co2):
    miles = round((float(co2) / 0.392), 3)
    return miles


def calculate_saving(meat, alternative):
    "Based on inputs, calculate co2 saving"
    meat_co2 = get_co2(meat)
    alternative_co2 = get_co2(alternative)
    try:
        return float(meat_co2) - float(alternative_co2)
    except:
        flash(f'An error has occured')
        return 'Error'


def get_co2(food):
    return info.get(food)
