input_file = "data/old/wiki-topcats-categories.txt"
output_file = "data/wiki-brazilian-categories.txt"
category_to_ids = {}
ids_related_to_brazil = set()

with open(input_file, "r") as file:
    for line in file:
        category, *ids = map(str.strip, line.split('; '))
        
        if "brazil" in category.lower() and ids:
            category_to_ids[category] = ids
            ids_related_to_brazil.update(ids)

with open(output_file, "w") as output_file:
    for category, ids in category_to_ids.items():
        output_file.write(f"{category}; {' '.join(ids)}\n")