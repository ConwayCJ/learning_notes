test_case = [7,2134,564,12,7,87,1,45,578,45,12,34]

def sum(nums):
    count = 0
    for num in nums:
        count += num
    return count

print(sum(test_case))