#!/usr/bin/env python3

def famous_births(dict):
    for i in dict:
        value = dict[i]
        print(f"{value['name']} is a great scientist in {value['date_of_birth']}")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)


