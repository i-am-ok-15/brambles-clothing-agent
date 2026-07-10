import json


def get_clothing_options():
    with open("clothing.json", "r") as clothing:
        return json.load(clothing)


def select_clothing(temp, clothing_options):
    clothing_items = ["head", "body", "legs", "feet", "hands", "other", "bag"]
    clothing = {}
    for item in clothing_items:
        options = clothing_options["body area"][item]
        max_temp = 0
        for key in options:
            if temp >= float(key):
                max_temp = key
        clothing[item] = options[max_temp]
    return clothing
