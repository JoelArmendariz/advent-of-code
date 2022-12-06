import os
dir = os.path.dirname(__file__)

presents = None

with open(dir + '/presents.txt', 'r') as f:
    presents = f.readlines()

def print_presents():
    print(presents)

def parse_present_dimensions(present):
    return map(int, present.split("x"))

def get_paper_size_for_present(present):
    length, width, height = parse_present_dimensions(present)
    return 2*length*width + 2*width*height + 2*height*length

def get_extra_slack(present):
    length, width, height = parse_present_dimensions(present)
    return min(length * width, width * height, length * height)

def get_total_paper_size():
    total = 0
    for present in presents:
        if not present: continue
        total += get_paper_size_for_present(present) + get_extra_slack(present)
    return total

def get_bow_length(present):
    length, width, height = parse_present_dimensions(present)
    return length * width * height

def get_present_ribbon_length(present):
    length, width, height = parse_present_dimensions(present)
    return length + length + width + width

def get_total_ribbon_length():
    total = 0
    for present in presents:
        if not present: 
            continue
        total += get_present_ribbon_length(present) + get_bow_length(present)
    return total

def calculate_ribbon():
    feet = 0
    for line in presents:
        side_lengths = line.split('x')
        int_list = sorted([int(x) for x in side_lengths])
        smallest_face = int_list[0] * 2 + int_list[1] * 2
        volume = int_list[0] * int_list[1] * int_list[2]
        feet += smallest_face
        feet += volume

    print(feet)

calculate_ribbon()
