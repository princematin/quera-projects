def good_fruits(fruits: tuple[dict]) -> dict[str, int]:
    good_fruits_dict = dict()
    for item in fruits:
        fruit_name = item["name"]
        if item["shape"] == 'sphere':
            if item["volume"] <= 500 and item["volume"] >= 100:
                if item["mass"] >= 300 and item["mass"] <= 600:
                    if fruit_name not in good_fruits_dict:
                        good_fruits_dict[fruit_name] = 0
                    good_fruits_dict[fruit_name] += 1
    return good_fruits_dict

# print(good_fruits((
#     {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
#     {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
#     {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
#     {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})))