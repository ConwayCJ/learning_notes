test_case = [7,2134,564,12,7,87,1,45,578,45,12,34]

def find_max(nums):
    max = float("-inf")
    for num in nums:
        if num > max:
            max = num
    return max

print(find_max(test_case))