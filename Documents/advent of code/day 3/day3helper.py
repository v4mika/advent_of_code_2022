def get_item_priority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    if c.islower():
        return ord(c) - ord('a') + 1      
