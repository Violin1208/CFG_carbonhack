from flask_site.static_data.food_dict import info
from flask import flash


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
