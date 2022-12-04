from day3helper import get_item_priority

def find_badge(rucksack_1, rucksack_2, rucksack_3):
    r1 = set(rucksack_1.strip())
    r2 = set(rucksack_2.strip())
    r3 = set(rucksack_3.strip())
    badge = get_item_priority(list(r1 & r2 & r3)[0])
    return badge

input = open("input.txt", "r")
rucksacks = input.readlines()
num_groups = int(len(rucksacks) / 3)

badge_priority = 0
for i in range(num_groups):
    ind = 3 * i
    badge = find_badge(rucksacks[ind], rucksacks[ind + 1], rucksacks[ind + 2])
    badge_priority += badge
input.close()
print(badge_priority)

