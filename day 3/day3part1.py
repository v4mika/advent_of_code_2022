from day3helper import get_item_priority

total_priority = 0
with open("input.txt", "r") as rucksacks:
    for rucksack in rucksacks:
        r = rucksack.strip()
        comp_size = int(len(r)/ 2)
        first_comp = set(r[: comp_size])
        second_comp = set(r[comp_size :])
        duplicate = first_comp & second_comp
            
        if duplicate:
            duplicate_item = list(duplicate)[0]
            total_priority += get_item_priority(duplicate_item)

print(total_priority)
rucksacks.close()