import math
def log_scale(data, base):
    list = []
    for d in data:
        list.append(math.log(d,base))
    return list

print(log_scale([1, 10, 100, 1000], 10)) # expect: [0.0, 1.0, 2.0, 2.9999999999999996]