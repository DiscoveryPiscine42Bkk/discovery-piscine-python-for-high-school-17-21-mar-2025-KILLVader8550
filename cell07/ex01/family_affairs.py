#!/usr/bin/env python3 

def find_the_redheads (dupont_family):
    new_list = []
    for key, value in dupont_family.items():
        if value == 'red':
            new_list.append(key)
    return new_list

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))