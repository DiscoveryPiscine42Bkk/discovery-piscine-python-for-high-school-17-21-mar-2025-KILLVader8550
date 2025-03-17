#!/usr/bin/env python3 

def array_of_names (persons):
    new_arr = []
    for key, value in persons.items():
        new_arr.append(key.title() + " " + value.title())
    return new_arr

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))