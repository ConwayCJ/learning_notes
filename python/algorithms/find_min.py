test_case = [7,2134,564,12,7,87,1,45,578,45,12,34]

def find_minimum(nums):
    min = float("inf")

    for num in nums:
        if num < min:
            min = num
    return min

print(find_minimum(test_case))