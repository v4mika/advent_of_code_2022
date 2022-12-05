def in_range(begin1, end1, begin2, end2):
    return ((begin1 <= begin2 <= end2 <= end1)
            or (begin2 <= begin1 <= end1 <= end2))
    
def any_overlap(begin1, end1, begin2, end2):
    return begin1 <= begin2 <= end1 or begin2 <= begin1 <= end2
    
def split_section(section):
    section_lst = section.split('-')
    begin = int(section_lst[0])
    end = int(section_lst[1])
    return (begin, end)

    
complete_overlap_counter = 0
any_overlap_counter = 0
with open("input.txt", "r") as input:
    for line in input:
        sections = line.split(',')
        (begin1, end1) = split_section(sections[0])
        (begin2, end2) = split_section(sections[1])
        if any_overlap(begin1, end1, begin2, end2):
            print(begin1, end1, begin2, end2)
            any_overlap_counter += 1
            if in_range(begin1, end1, begin2, end2):
                complete_overlap_counter += 1
            
input.close()
print(any_overlap_counter)
print(complete_overlap_counter)
 