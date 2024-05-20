run_cases = [
    ([1, 2], [[1, 2], [2], [1], []]),
    ([1, 2, 3], [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]),
]

def power_set(input_set):
    if len(input_set) == 0: return [[]]

    list = [] 

    first_element = input_set[0]
    subset = power_set(input_set[1:])

    for entry in subset:
        list.append([first_element] + entry) # [] + []
        list.append(entry)
    return list

for case in run_cases:
    print(power_set(case))