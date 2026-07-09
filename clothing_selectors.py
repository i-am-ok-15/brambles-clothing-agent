import json
from weather_analysis import calculate_mean_temp

def get_clothing_options():
    with open("clothing.json", "r") as clothing:
        return json.load(clothing)

def select_headwear(temp, clothing_options):
    options =  clothing_options["body area"]["head"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_bodywear(temp, clothing_options):
    options =  clothing_options["body area"]["body"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_legwear(temp, clothing_options):
    options =  clothing_options["body area"]["legs"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_footwear(temp, clothing_options):
    options =  clothing_options["body area"]["feet"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_handwear(temp, clothing_options):
    options =  clothing_options["body area"]["hands"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_otherwear(temp, clothing_options):
    options =  clothing_options["body area"]["other"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]

def select_bagwear(temp, clothing_options):
    options =  clothing_options["body area"]["bag"]
    max_temp = 0
    for key in options:
        if temp >= float(key):
            max_temp = key
    return options[max_temp]